var restUrl = 'http://156.35.95.67/safepoint/';
markers = {};

$(function() {
  addCategories();
});

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

function clearReports(category) {
  var categoryMmarkers = markers[category];
  if (categoryMmarkers != null) {
    categoryMmarkers.forEach(function(marker) {
        marker.setMap(null);
    });
  }
  markers[category] = [];

  if (heatmap.getMap()) {
    heatmap.setData(getHeatmapPoints());
  }
}

function toggleReports() {
  for (var key in markers) {
    markers[key].forEach(function(marker) {
      marker.setMap(marker.getMap()? null : map);
    });
  }
}

function displayReports(category) {
  var heatmapActive = heatmap.getMap() != null;
  var url = restUrl + "categories/" + category + "/reports";
  markers[category] = [];

  $.get(url, function(data) {
    var reports = jQuery.parseJSON(data);
    reports.forEach(function(report) {
      var marker = new google.maps.Marker({
        animation: google.maps.Animation.DROP,
        icon: 'img/markers/' + category + '.png',
        map: heatmapActive? null : map,
        position: new google.maps.LatLng(report.lat, report.lng)
      });
      var infowindow = new google.maps.InfoWindow({
        content: '<p>' + report.description + '</p>'
      });
      marker.addListener('click', function() {
        infowindow.open(map, marker);
      });
      markers[category].push(marker);
    });

    if (heatmapActive) {
      heatmap.setData(getHeatmapPoints());
    }
  });
}
