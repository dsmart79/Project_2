//creating empty layergroup for later adding to map
//https://www.tutorialspoint.com/leafletjs/leafletjs_layers_group.htm

import API_KEY from "./config.js"

var statesCountyLayer = new L.layerGroup();

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
    layers: [statesCountyLayer]
});

//Add lightMap tiles to the map
lightMap = lightMap.addTo(map);


//overlay object
var overlayMaps = {
    "States": statesCountyLayer
};
//basemap object
var baseMaps = {
    "Light": lightMap
};

//add base and overlay layers
L.control.layers(baseMaps, overlayMaps, {
    collapsed: false
}).addTo(map);

// fetch GEOJson data for the earthquake layer
d3.json(states, function(statesCountyData){
  createMap(statesCountyData);
});

//template literal substituted here change popup in html
function createMap(statesCountyData) {
    L.geoJson(statesCountyData, {
      onEachFeature: function (features, layer) {
        layer.bindPopup(`Location: ${features.properties.name}`
    //                         "</h3><h3>Magnitude: "+feature.properties.mag +
    //                         "</h3><h3>DateTime: "+ new Date(feature.properties.time)+"</h3>")
    
        )},
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
  }).addTo(statesLayer);

    
// fetch GEOJson data for the earthquake layer
d3.json(counties, function(countyData){
  createMap(countyData);
});
    
function createMap(countyData) {
    L.geoJson(countyData, {
      onEachFeature: function (features, layer) {
        layer.bindPopup("<h3>County: "+county

        )},
  }).addTo(countyLayer);

    //legend
    var legend = L.control({position: "bottomright"});
    legend.onAdd = function() {
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
}};