var autocompleteService;
var clickListenerHandle;
var geocoder;
var heatmap;
var map;
var minZoomLevel = 3;
var selectingPlace = true;
var userMarker;
var userId;

function setUserId(id) {
  userId = id;
}


/* Show the sidebar if the user clicks the hamburger icon */
$('#menu-button').click(function() {
  if ($('#sidebar-lock-button').hasClass('icon-open-lock')) {
    $('#sidebar').addClass('show');
    showScrim();
  }
});

/* Hide the sidebar if the user clicks outside of it */
$(document).mouseup(function(e) {
    var container = $('#sidebar, #add-report-modal');
    if (!container.is(e.target) && container.has(e.target).length === 0) {
        closeSidebar();
        closeAddReportModal();
        if (!selectingPlace) {
          showSearchBar();
        }
    }
  });

/* Change search icon color when the user is typing */
$('#search').keyup(function(event) {
  var searchIcon = $('#search-button');
  value = $(this).val();

  if ($('#results').children().length > 0 &&
      (event.keyCode == '38' || event.keyCode == '40')) {
    navigateAutocompleteList(event.keyCode);
  } else if (event.keyCode != 27){
    if (value.length === 0) {
      closeResultsPanel();
      searchIcon.removeClass('active');
    } else {
      if (event.keyCode == '13') {
        var liSelected = $('#results li.selected');
        if (liSelected.length) {
          value = $('#results li.selected span.place-text').text();
          $('#search').val(value);
        }
        centerMapOnAddress(value);
      } else {
        searchIcon.addClass('active');
        autocompleteService.getQueryPredictions({ input: value }, displayAutocompleteSuggestions);
      }
    }
  }
});

$(document).keyup(function(e) {
  if (e.keyCode == 27) closeResultsPanel();
});

/* If the user clicks over an autocomplete result, center the map in that place */
$('body').on('click', 'ul#results li', function() {
  var address = $(this).text();
  $('#search').val(address);
  centerMapOnAddress(address);
});

/* If the user clicks on the search button, center the map in the place set on the input field */
$('#search-button').click(function() {
  centerMapOnAddress($('#search').val());
});

/* Add event to let the user change the map type */
$('#map-type li').click(function() {
  var li = $(this);

  var index = li.index();
  if (index == 1) {
    li.toggleClass('enabled');
    toggleHeatmap();
  } else {
    li.siblings('.enabled:not(:nth-of-type(2))').removeClass('enabled');
    li.addClass('enabled');
    changeMapType(index);
  }

  closeSidebar();
});

/* Control behaviour of categories on click */
$('body').on('click', '#reports-categories li', function() {

  /* Close sidebar and toggle category */
  closeSidebar();
  var li = $(this);
  li.toggleClass('enabled');

  /* Update map markers */
  var categoryId = li.data('id');
  if (li.hasClass('enabled')) {
    displayReports(categoryId);
  } else {
    clearReports(categoryId)
  }
});

/* Control behaviour of wms layers on click */
$('body').on('click', '#wms-layers li', function() {
  /* Close sidebar and toggle category */
  closeSidebar();
  var li = $(this);
  li.toggleClass('enabled');

  /* Update map markers */
  var wmsLayerId = li.data('id');
  if (li.hasClass('enabled')) {
    loadWmsLayer(wmsLayerId);
  } else {
    unloadWmsLayer(wmsLayerId)
  }
});

/* Start report creation when the user clicks over the report button */
$('#add-report-button').click(function() {
  map.setOptions({ streetViewControl: false });
  closeSidebar();
  hideSearchBar();
  showInfoPanel();
  enableClickPlacement();
});

/**
 * Cancels the report creation and show back the UI.
 */
function cancelReport() {
  clearUserMarker();
  disableClickPlacement();
  hideInfoPanel();
  hideScrim();
  $('#add-report-modal').removeClass('show');
  showSearchBar();
}

/**
 * Centers the map on the specified address, if exists.
 */
function centerMapOnAddress(address) {
  closeResultsPanel();

  geocoder.geocode( { 'address': address}, function(results, status) {
    if (status == google.maps.GeocoderStatus.OK) {
      map.setCenter(results[0].geometry.location);
    }
  });
}

/**
 * Changes the map type.
 */
function changeMapType(type) {
  switch(type) {
    case 0:
      map.setMapTypeId(google.maps.MapTypeId.SATELLITE);
      break;
    case 2:
      map.setMapTypeId(google.maps.MapTypeId.ROADMAP);
      break;
    case 3:
      map.setMapTypeId(google.maps.MapTypeId.TERRAIN);
      break;
  }
}

/**
 * Clear the marker placed by the user (if exists).
 */
function clearUserMarker() {
    if (userMarker) {
      userMarker.setMap(null);
      userMarker = null;
    }
}

/**
 * Closes the modal to add reports.
 */
function closeAddReportModal() {
  $('#add-report-modal').removeClass('show');
  $('#add-report-modal textarea').val('');
  $('#add-report-modal select').val(1);
  hideScrim();
}

/**
 * Close the results panel, clearing the previous results.
 */
function closeResultsPanel() {
  var resultsList = $('ul#results');
  resultsList.empty();
  resultsList.removeClass('expanded');
}

/**
 * Closes the sidebar.
 */
function closeSidebar() {
  if ($('#sidebar-lock-button').hasClass('icon-open-lock')) {
    $('#sidebar').removeClass('show');
    hideScrim();
  }
}

/**
 * Centers the map in the user location if geoLocation is available.
 */
function centerMapOnUserLocation() {
  if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(function(position) {
      initialLocation = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
      map.setCenter(initialLocation);
      map.setZoom(15);
    });
  }
}

/**
 * Disables click over the map.
 */
function disableClickPlacement() {
  google.maps.event.removeListener(clickListenerHandle);
  selectingPlace = false;
}

/**
 *Shows a panel in the search bar with suggested places.
 */
function displayAutocompleteSuggestions(predictions, status) {
  if (status == google.maps.places.PlacesServiceStatus.OK) {
    var resultsList = $('ul#results');
    resultsList.empty();

    if (predictions.length > 0) {
      resultsList.addClass('expanded');
      predictions.forEach(function(prediction) {

        /* Get input value to highlight that text on results */
        var highlightedText = $('#search').val();
        resultsList.append('<li><span class="place-icon"></span><span class="place-text">' +
            highlightWords(prediction.description, highlightedText) + '</span></li>');
      });
    } else {
      resultsList.removeClass('expanded');
    }
  }
}

/**
 * Enables click over the map, letting the user to place a marker.
 */
function enableClickPlacement() {
  clickListenerHandle = google.maps.event.addListener(map, 'click', function(event) {
    placeUserMarker(event.latLng);
  });

  selectingPlace = true;
}

/**
 * Get data from add report modal and send it to the callback function.
 */
function getAddReportModalData(callback) {
  var address = $('#address').val();
  if (!address) {
    callback();
  } else {
    geocoder.geocode( { 'address': address }, function(results, status) {
      if (status == google.maps.GeocoderStatus.OK) {
        var latitude = results[0].geometry.location.lat();
        var longitude = results[0].geometry.location.lng();
        var description = $('#add-report-modal textarea').val();
        var category = $('#add-report-modal select').val();

        callback({ lat: latitude, lng: longitude, category_id: category, description: description });
      }
    });
  }
}

/**
 * Returns an array with all the markers coordinates. Only markers of
 * enabled categories are used.
 */
function getHeatmapPoints() {
  points = [];
  $('#reports-categories li.enabled').each(function() {
    var reports = markers[$(this).data('id')];
    if (reports) {
      reports.forEach(function(marker) {
        points.push(marker.getPosition());
      });
    }
  });
  return points;
}

/**
 * Hides the info panel.
 */
function hideInfoPanel() {
  $('#info-panel').removeClass('show');
}

/**
 * Hides the scrim.
 */
function hideScrim() {
  $('#scrim').removeClass('show');
}

/**
 * Hides the search bar.
 */
function hideSearchBar() {
  $('#search-bar').removeClass('show');
  closeResultsPanel();
}

/**
 * Hides all the elements of the UI.
 */
function hideUI() {
  hideInfoPanel();
  hideSearchBar();
  closeSideBar();
}

/**
 * Find a given word in a line and highlight it.
 */
function highlightWords(line, word) {
  var regex = new RegExp('(' + word + ')', 'gi');
  return line.replace(regex, '<span class="highlight">$1</span>');
}

/**
 * Initializes the map and the needed services.
 */
function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: { lat: 0, lng: 0 },
    mapTypeControl: false,
    zoom: minZoomLevel,
    minZoom: minZoomLevel
  });

  centerMapOnUserLocation();
  initMapAuxiliarComponents();
}

/**
 * Initializes Google Maps services and visualizations.
 */
function initMapAuxiliarComponents() {
  autocompleteService = new google.maps.places.AutocompleteService();
  geocoder = new google.maps.Geocoder();
  heatmap = new google.maps.visualization.HeatmapLayer();
  setStreetViewListener();
}

/**
 * Handles navigation over the autocomplet list.
 */
function navigateAutocompleteList(keyCode) {
  var current = $('#results li.selected');

  switch (keyCode) {
    case 38: // Up arrow
      navigateAutocompleteListUp(current);
      break;
    case 40: // Down arrow
      navigateAutocompleteListDown(current);
      break;
  }
}

/**
 * Select the next element of the autocomplete list if there is one.
 */
function navigateAutocompleteListDown(current) {
  if (current.length) {
    var next = current.next();
    if (next.length) {
      current.next().addClass('selected');
      current.removeClass('selected');
    }
  } else {
    current.removeClass('selected');
    $('#results li:first-of-type').addClass('selected');
  }
}

/**
 * Select the previous element of the autocomplete list if there is one.
 */
function navigateAutocompleteListUp(current) {
  var prev = current.prev();
  if (prev.length) {
    current.removeClass('selected');
    prev.addClass('selected');
  }
}

/**
 * Opens the modal used to add new reports.
 */
function openAddReportModal() {
  clearUserMarker();
  disableClickPlacement();
  hideInfoPanel();
  showScrim();
  $('#add-report-modal').addClass('show');
}


/**
 * Add a marker in the position selected by the user.
 */
function placeUserMarker(location) {
  if (userMarker) {
    userMarker.setPosition(location);
  } else {
    userMarker = new google.maps.Marker({
      animation: google.maps.Animation.BOUNCE,
      draggable: true,
      map: map,
      position: location
    });

    updateAddressInputValue(location)
  }
}

/**
 * Adds an event to streetview to control when to hide UI elements.
 */
function setStreetViewListener() {
  google.maps.event.addListener(map.getStreetView(), 'visible_changed', function() {
    if (this.getVisible()) {
      hideUI();
    } else {
      showUI();
    }
  });
}

/**
 * Shows info panel.
 */
function showInfoPanel() {
  $('#info-panel').addClass('show');
}

/**
 * Shows search bar.
 */
function showSearchBar() {
  $('#search-bar').addClass('show');
}

/**
 * Shows scrim.
 */
function showScrim() {
  $('#scrim').addClass('show');
}

/**
 * Shows UI components.
 */
function showUI() {
  showSearchBar();
}

/**
 * Toggles heatmap visibility.
 */
function toggleHeatmap() {
  heatmap.setData(getHeatmapPoints());
  heatmap.setMap(heatmap.getMap()? null : map);
  toggleReports();
}

/**
 * Toggles sidebar lock, what fixed the sidebar to the left and
 * shrink the content to fit.
 */
function toggleSidebarLock() {
  var lock = $('#sidebar-lock-button');
  lock.toggleClass('icon-open-lock');
  lock.toggleClass('icon-close-lock');
  lock.hasClass('icon-open-lock') ? closeSidebar() : hideScrim();
  $('#wrapper').toggleClass('shrink');
}

/**
 * Get the address of the given coordinates and
 * updates the modal window input with it.
 */
function updateAddressInputValue(location) {
  geocoder.geocode({'location': location}, function(results, status) {
    if (status === google.maps.GeocoderStatus.OK) {
      if (results[0]) {
        $('#address').val(results[0].formatted_address);
      }
    }
  });
}
