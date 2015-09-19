var autocompleteService;
var geocoder;
var map;
var minZoomLevel = 3;

/* Show the sidebar if the user clicks the hamburger icon */
$('#menu-button').click(function() {
  $('#sidebar').addClass('show');
  $('#scrim').addClass('visible');
});

/* Hide the sidebar if the user clicks outside of it */
$(document).mouseup(function(e) {
    var container = $('#sidebar');
    if (!container.is(e.target) && container.has(e.target).length === 0) {
        container.removeClass('show');
        $('#scrim').removeClass('visible');
    }
});

/* Change search icon color when the user is typing */
$('#search').keyup(function(event) {
  var searchIcon = $('#search-button');
  value = $(this).val();

  if (value.length === 0) {
    closeResultsPanel();
    searchIcon.removeClass('active');
  } else {
    if (event.keyCode == '13') {
      centerMapOnAddress(value);
    } else {
      searchIcon.addClass('active');
      autocompleteService.getQueryPredictions({ input: value }, displayAutocompleteSuggestions);
    }
  }
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

/**
 * Close the results panel, clearing the previous results.
 */
function closeResultsPanel() {
  var resultsList = $('ul#results');
  resultsList.empty();
  resultsList.removeClass('expanded');
}

/**
 * Centers the map on the specified address, if exists.
 */
function centerMapOnAddress(address) {
  closeResultsPanel();

  geocoder.geocode( { 'address': address}, function(results, status) {
    if (status == google.maps.GeocoderStatus.OK) {
      map.setCenter(results[0].geometry.location);
      var marker = new google.maps.Marker({
          map: map,
          position: results[0].geometry.location
      });
    }
  });
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
        var normalText = prediction.description.substring(highlightedText.length);
        resultsList.append('<li><span class="place-icon"></span><span class="place-text"><span class="highlight">' + highlightedText + '</span>' + normalText + '</span></li>');
      });
    } else {
      resultsList.removeClass('expanded');
    }
  }
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

  if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(function(position) {
      initialLocation = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
      map.setCenter(initialLocation);
      map.setZoom(15);
    });
  }

  autocompleteService = new google.maps.places.AutocompleteService();
  geocoder = new google.maps.Geocoder();
}
