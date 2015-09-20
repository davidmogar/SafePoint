var restUrl = 'http://156.35.95.67/safepoint/';
var markers = {};

$(function() {
  addCategories();
});

/**
 * Fetch categories and add them to the sidebar.
 */
function addCategories() {
  var url = restUrl + "categories";
  $.get(url, function(data) {
    var container = $('#reports-categories');
    container.empty();

    var categories = jQuery.parseJSON(data);
    categories.forEach(function(category) {
      var className = category.name.toLowerCase();
      container.append('<li data-id="' + category.id +
          '"><span class="icon icon-' + className +
          '"></span>' + category.name + '</li>');
    });
  });
}

/**
 * Clear from the map all the reports of the given category.
 */
function clearReports(category) {
  var categoryMmarkers = markers[category];
  if (categoryMmarkers != null) {
    categoryMmarkers.forEach(function(marker) {
        marker.setMap(null);
    });
  }
  markers[category] = [];

  /* Update heatmap if needed */
  if (heatmap.getMap()) {
    heatmap.setData(getHeatmapPoints());
  }
}

/**
 * Creates a marker for a given report.
 */
function createMarker(report, icon, map) {
  var marker = new google.maps.Marker({
    animation: google.maps.Animation.DROP,
    icon: icon,
    map: map,
    position: new google.maps.LatLng(report.lat, report.lng)
  });
  var date = new Date(report.time).toGMTString();
  var infowindow = new google.maps.InfoWindow({
    content: report.description + '<span class="date">' + date + '</span><p><button>Delete my report</button></p>'
  });
  marker.addListener('click', function() {
    infowindow.open(map, marker);
  });
  return marker;
}

/**
 * Creates a marker icon for the given category.
 */
function createMarkerIcon(category) {
  return new google.maps.MarkerImage('img/markers/' + category + '.png',
      new google.maps.Size(24, 24),
      new google.maps.Point(0, 0), // Origin
      new google.maps.Point(12, 12)); // Center
}

/**
 * Fetch reports for a given category and creates
 * a marker for each one.
 */
function displayReports(category) {
  var heatmapActive = heatmap.getMap() != null;
  var url = restUrl + "categories/" + category + "/reports";
  markers[category] = [];

  $.get(url, function(data) {
    var markerIcon = createMarkerIcon(category);
    jQuery.parseJSON(data).forEach(function(report) {
      markers[category].push(createMarker(report, markerIcon, heatmapActive? null : map));
    });

    /* Update heatmap if needed */
    if (heatmapActive) {
      heatmap.setData(getHeatmapPoints());
    }
  });
}

/**
 * Toggles reports visibility, clearing them from the map.
 */
function toggleReports() {
  for (var key in markers) {
    markers[key].forEach(function(marker) {
      marker.setMap(marker.getMap()? null : map);
    });
  }
}
