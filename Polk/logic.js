//base map
var statesLayer = new L.layerGroup();

    // Create the tile layer that will be the background of our map
var lightmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/light-v9/tiles/256/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"http://openstreetmap.org\">OpenStreetMap</a> contributors, <a href=\"http://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"http://mapbox.com\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.light",
    accessToken: API_KEY
});

  // Create a baseMaps object to hold the lightmap layer
var map =  L.map("map", {
    "Light Map": lightmap,
    center: [38.6270, -90.1994], //st. louis
    zoom: 3,
    layers: [statesLayer]
});

//Add lightMap tiles to the map
lightMap = lightMap.addTo(map);

//overlay object
var overlayMaps = {
    "States": statesLayer,
};
//basemap object
var baseMap = {
    "Light": lightMap,
};

// Create a layer control, pass in the baseMaps and overlayMaps. Add the layer control to the map
L.control.layers(baseMaps, overlayMaps, {
    collapsed: false
}).addTo(map);

//Create an overlayMaps object to hold the states polygon layer from choropleth
//work on this
var link = 'https://leafletjs.com/examples/choropleth/us-states.js'

//fetch GEOJson data foor the statesLayer
d3.json(link, function(data){
    createMap(data);
    });
    
    function createMap(data) {
        L.geoJson(data, {
            onEachFeature: function (feature, layer) {
                layer.bindPopup("<h3>Average Age: "+feature.properties.avgAge +
                                "</h3><h3>Policy Type: "+feature.properties.metalLevel +
            }               
        }).addTo(statesLayer);  
    }

.addTo(map);

// method that we will use to update the control based on feature properties passed
//need help with this
info.update = function (props) {
	this._div.innerHTML = '<h4>Average Age and Policy Type by State </h4>' +  (props ?
		'<b>' + avgAge.pname + '</b><br />' + props.density + ' people / mi<sup>2</sup>'
		: 'Hover over a state');
};

info.addTo(map);

//hover

function highlightFeature(e) {
	info.update(layer.feature.properties);
}

function resetHighlight(e) {
	info.update();
}

//legend

var legend = L.control({
    position: 'bottomright'
});

legend.onAdd = function (map) {
	var div = L.DomUtil.create('div', 'info legend');
};