var services = [
    {
        "name": "Hospitales",
        "label": "hospital",
        "url": "http://www.sigmayores.csic.es/ArcGIS/services/Rec-Sanitarios/MapServer/WMSServer?",
        "format": "image/png",
        "styles": "default,default",
        "layers": "Centros_salud,Hospitales",
        "version": "1.1.1",
        "opacity": 1,
        "z-index": 2
    }, {
        "name": "Fire risks",
        "label": "fire",
        "url": "http://wms.magrama.es/sig/Biodiversidad/Incendios/wms.aspx?",
        "format": "image/png",
        "styles": "default",
        "layers": "Frecuencia+de+Incendios+Forestales",
        "version": "1.1.1",
        "opacity": 0.5,
        "z-index": 0
    }, {
        "name": "Flooding risks",
        "label": "flooding",
        "url": "http://156.35.98.27/cgi-bin/safepoint?",
        "format": "image/png",
        "styles": "default",
        "layers": "FloodingRisk",
        "version": "1.1.0",
        "opacity": 0.7,
        "z-index": 1
    }
];

$(function () {
    addWmsLayers();
})

function addWmsLayers() {
    var container = $('#wms-layers');
    container.empty();

    services.forEach(function (service, index) {
        container.append('<li data-id="' + index +
            '"><span class="icon icon-' + service['label'] +
            '"></span>' + service['name'] + '</li>');
    });
}

function loadWmsLayer(id) {
    var service = services[id];
    loadWMS(service['url'], service['format'], service['layers'], service['styles'], service['version'], service['opacity'], service['z-index']);
}

function unloadWmsLayer(id) {
    var service = services[id];
    map.overlayMapTypes.setAt(service['z-index'], null);
}

function loadWMS(baseURL, format, layers, styles, version, opacityLevel, zIndex) {
    var tileHeight = 256;
    var tileWidth = 256;

    var wmsParams = [
        "REQUEST=GetMap",
        "SERVICE=WMS",
        "SRS=EPSG:4326",
        "FORMAT=" + format,
        "LAYERS=" + layers,
        "STYLES=" + styles,
        "VERSION=" + version,
        "TRANSPARENT=TRUE",
        "WIDTH=" + document.getElementById("map").offsetWidth,
        "HEIGHT=" + document.getElementById("map").offsetHeight
    ];

    var overlayOptions = {
        getTileUrl: function (coord, zoom) {
            if (zoom < 5) {
                return null;
            }

            var proj = map.getProjection();
            var zfactor = Math.pow(2, zoom);
            var top = proj.fromPointToLatLng(new google.maps.Point(coord.x * tileWidth / zfactor, coord.y * tileHeight / zfactor));
            var bot = proj.fromPointToLatLng(new google.maps.Point((coord.x + 1) * tileWidth / zfactor, (coord.y + 1) * tileHeight / zfactor));
            var bbox;
            if (version.split('.')[1] == '1') {
                bbox = top.lng() + "," + bot.lat() + "," + bot.lng() + "," + top.lat();
            } else {
                bbox = bot.lat() + "," + top.lng() + "," + top.lat() + "," + bot.lng();
            }

            return baseURL + wmsParams.join("&") + "&BBOX=" + bbox;
        },
        tileSize: new google.maps.Size(tileWidth, tileHeight),
        opacity: opacityLevel
    };
    var overlayWMS = new google.maps.ImageMapType(overlayOptions);
    map.overlayMapTypes.push(null);
    map.overlayMapTypes.setAt(zIndex, overlayWMS);
}
