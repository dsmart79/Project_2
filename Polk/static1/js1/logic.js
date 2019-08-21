//creating empty layergroup for later adding to map
//https://www.tutorialspoint.com/leafletjs/leafletjs_layers_group.htm
// import statesCountyData from "./static/states_county.js";

//light tile layer
var lightMap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"http://openstreetmap.org\">OpenStreetMap</a> contributors, <a href=\"http://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"http://mapbox.com\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.light",
  accessToken: 'pk.eyJ1IjoiZHNtYXJ0NzkiLCJhIjoiY2p6MGlra3llMDFpdTNicno2Z3NucWR6diJ9.SDgl9Y-y-_J6nWuy2wmUiQ'
});

var statesLayer = new L.layerGroup();
var countyLayer = new L.layerGroup();

//create map with layer
var map = L.map("map", {
  center: [38.6270, -90.1994], //st. louis
  zoom: 3,
  layers: [lightMap, statesLayer]
});

var counties = "./static/geoJson/states_county.json"
var states = "./static/geoJson/us_states.json"

//basemap object
var baseMaps = {
  "Light": lightMap
};

//overlay object
var overlayMaps = {
  "States": statesLayer,
  "Counties": countyLayer
};

//add base and overlay layers
L.control.layers(overlayMaps).addTo(map);

// fetch GEOJson data for the earthquake layer
d3.json(counties, function (statesCountyData) {
  createMap(statesCountyData);
});

//template literal substituted here change popup in html
function createMap(statesCountyData) {
  L.geoJson(statesCountyData, {
    onEachFeature: function (features, layer) {
      layer.bindPopup("<h3>" + features.properties.NAME + "<h3>")
      //                         "</h3><h3>Magnitude: "+feature.properties.mag +
      //                         "</h3><h3>DateTime: "+ new Date(feature.properties.time)+"</h3>")


    },
    //fix point to states and then zoom and then point to counties
    //     pointToLayer: function (feature, latlng) {
    //         return new L.circleMarker(latlng, {
    //             radius: feature.properties.mag*5,
    //             fillColor: circleColor(feature.properties.mag),
    //             fillOpacity: 0.8,
    //             color: "black",
    //             weight: .5
    //         })
    //     }
  }).addTo(countyLayer);


  // fetch GEOJson data for the earthquake layer
  d3.json(states, function (statesData) {
    createMap(statesData);
  });

  function createMap(statesData) {
    L.geoJson(statesData, {
      onEachFeature: function (features, layer) {
        layer.bindPopup("<h3>" + features.properties.name + "<h3>")


      },
    }).addTo(statesLayer);

    //legend
    var legend = L.control({
      position: "bottomright"
    });
    legend.onAdd = function () {
      var div = L.DomUtil.create("div", "legend");
      // var magnitudes = [1,2,3,4,5,5.1];
      // var colors = magnitudes.map(d=>circleColor(d));
      // labels=[];

      // var legendInfo = "<h3><center>Magnitude</center></h3>" +
      //     "<div class=\"labels\">" +
      //     "<div class=\"min\">"+"<" + magnitudes[0].toFixed(1)+ "</div>" +
      //     "<div class=\"max\">"+">"+magnitudes[magnitudes.length-2].toFixed(1) +"</div>"+
      //     "</div>"

      // div.innerHTML = legendInfo;
      // // set up legend color bar

      //     magnitudes.forEach(function(limit, index) {
      //         labels.push("<li style=\"background-color: " + colors[index] + "\"></li>"); 
      //     })
      //     div.innerHTML += "<ul>"+ labels.join("") + "</ul>";
      //     return div;
    };
    // legend.addTo(map);
  };
};