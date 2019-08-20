//creating empty layergroup for later adding to map
//base map

var statesLayer = new legend.layerGroup;

//light tile layer
var lightMap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  maxZoom: 18,
  id: "mapbox.light",
  accessToken: API_KEY
});

//create map with layer
var map =  L.map("map", {
    center: [38.6270, -90.1994], //st. louis
    zoom: 3,
    layers: [earthquakeLayer]
});

//Add lightMap and satelliteMap tiles to the map
lightMap = lightMap.addTo(map);

//overlay object
var overlayMaps = {
    "states": statesLayer,
};
//basemap object
var baseMaps = {
    "Light": lightMap,
};

  //add base and overlay layers
L.control.layers(baseMaps, overlayMaps, {
    collapsed: false
}).addTo(map);

var states = "us-states.json"

// fetch GEOJson data for the states layer wuth geometry
d3.json(states, function(statesData){
  createMap(statesData);
});

function createMap(statesData) {
	L.geoJson(data, {
		onEachFeature: function (feature, layer) {
      layer.bindPopup("<h3>Location: "+feature.properties.place + "</h3>"
      )},
	}).addTo(statesLayer);

	//legend
    var legend = L.control({position: "bottomright"});
    legend.onAdd = function() {
		var div = L.DomUtil.create("div", "legend");
	};
	legend.addTo(map);

};