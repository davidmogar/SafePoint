markers = {};

function selectCategory(id) {
    var url = "http://156.35.95.67/safepoint/categories/" + id + "/reports";
    $.get(url, function (data) {
        var reports = jQuery.parseJSON(data);
        console.log(reports)
        reports.forEach(function (report) {
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(report.lat, report.lng),
                map: map,
                animation: google.maps.Animation.DROP
            });
            markers[id] = [];
            markers[id].push(marker);
        });
    });
}

function clearCategory(id) {
    var categoryMarkers = markers[id];
    if (categoryMarkers != null) {
        categoryMarkers.forEach(function(marker) {
            marker.setMap(null);
        })
    }
    markers[id] = [];
}