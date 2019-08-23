//creating empty layergroup for later adding to map
//https://www.tutorialspoint.com/leafletjs/leafletjs_layers_group.htm
// import statesCountyData from "./static/states_county.js";

var statesLayer = new L.layerGroup();
// var countyLayer = new L.layerGroup();

//light tile layer
var lightMap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"http://openstreetmap.org\">OpenStreetMap</a> contributors, <a href=\"http://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"http://mapbox.com\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.light",
  accessToken: 'pk.eyJ1IjoiZHNtYXJ0NzkiLCJhIjoiY2p6MGlra3llMDFpdTNicno2Z3NucWR6diJ9.SDgl9Y-y-_J6nWuy2wmUiQ'
});

//create map with layer
var map = L.map("map", {
  center: [38.6270, -90.1994], //st. louis
  zoom: 3,
  layers: [statesLayer, lightMap]
});

var states = "static/geoJson/modifiedStates1.json"
// var counties = "static/geoJson/states_county.json"

//overlay object
var overlayMaps = {
  "States": statesLayer,
  // "Counties": countyLayer
};

//add base and overlay layers
L.control.layers(overlayMaps).addTo(map);

//adding color scale
function getColor(sc) {
  return sc > 5000 ? '#084594' :
    sc > 3000 ? '#2171b5' :
      sc > 1000 ? '#4292c6' :
        sc > 800 ? '#6baed6' :
          sc > 400 ? '#9ecae1' :
            sc > 100 ? '#c6dbef' :
              '#eff3ff';
}
//fill color based on state_count15 if available
function style(feature) {
  return {
    fillColor: getColor(feature.properties.state_count15),
    weight: 2,
    opacity: 1,
    color: 'black',
    dashArray: '3',
    fillOpacity: 0.3
  };
}
//add heighlight feature with event lister mouseover
function highlightFeature(e) {
  var layer = e.target;

  layer.setStyle({
    weight: 5,
    color: '#fff',
    dashArray: '',
    fillOpacity: 0.7
  });
}

function resetHighlight(e) {
  geojson.resetStyle(e.target);
}

function zoomToFeature(e) {
  map.fitBounds(e.target.getBounds());
}
// fetch GEOJson data for the states layer
d3.json(states, function (statesData) {
  createMapStates(statesData);
});

function createMapStates(statesData) {
  L.geoJson(statesData, {
    style: style, highlightFeature: highlightFeature,
    onEachFeature: function (features, layer) {
      layer.bindPopup("<h3>" + features.properties.name +
        "</h3><h3>State Count: " + features.properties.state_count15 + "</h3>")
    },
  }).addTo(statesLayer);
};

// fetch GEOJson data for the states layer
// d3.json(counties, function (countyData) {
//   createMapCounties(countyData);
// });

// function createMapCounties(countyData) {
//   L.geoJson(countyData, {
//     onEachFeature: function (features, layer) {
//       layer.bindPopup("<h3>" + features.properties.NAME + "<h3>")
//     },
//   }).addTo(countyLayer);

// };