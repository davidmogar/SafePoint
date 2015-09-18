var autocompleteService;
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
$('#search').keyup(function() {
  var searchIcon = $('#search-button');
  value = $(this).val();

  if (value.length === 0) {
    searchIcon.removeClass('active');
    autocompleteService.getQueryPredictions({ input: value }, displayAutocompleteSuggestions);
  } else {
    searchIcon.addClass('active');
  }
});

function displayAutocompleteSuggestions(predictions, status) {
  if (status == google.maps.places.PlacesServiceStatus.OK) {
    predictions.forEach(function(prediction) {
      var li = document.createElement('li');
      li.appendChild(document.createTextNode(prediction.description));
      document.getElementById('autocomplete-results').appendChild(li);
    });
  }
}

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
}
