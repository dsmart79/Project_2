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

var counties = "./static1/geojson1/states_county.json"
var states = "./static1/geojson1/modifiedStates.json"

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

// fetch GEOJson data for the counties layer
d3.json(counties, function (statesCountyData) {
  createMap(statesCountyData);
});
//fetch metal level and ... for each year in 
d3.json()

function createMap(statesCountyData) {
  L.geoJson(statesCountyData, {
    onEachFeature: function (features, layer) {
      layer.bindPopup("<h3>" + features.properties.NAME + "</h3>")},
  }).addTo(countyLayer);
};

// fetch GEOJson data for the states layer
d3.json(states, function (statesData) {
  createMap(statesData);
});

  function createMap(statesData) {
    L.geoJson(statesData, {
      onEachFeature: function (features, layer) {
      layer.bindPopup("<h3>" + features.properties.name + 
                      "</h3><h3>State Count: "+feature.properties.state_count15 +"</h3>")
      },
    }).addTo(statesLayer);
  }  

  //adding color scale
  function getColor(sc) {
    return sc > 5000 ? '#084594' :
           sc > 3000  ? '#2171b5' :
           sc > 1000  ? '#4292c6' :
           sc > 800  ? '#6baed6' :
           sc > 400   ? '#9ecae1' :
           sc > 100   ? '#c6dbef' :
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
      fillOpacity: 0.7
    };
  }
    L.geoJson(statesData, {style: style, onEachFeature: onEachFeature
    }).addTo(statesLayer);

  //add heighlight feature with event lister mouseover
  function highlightFeature(e) {
    var layer = e.target;
    
    layer.setStyle({
      weight: 5,
      color: '#666',
      dashArray: '',
      fillOpacity: 0.7
    });
    // if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
    //   layer.bringToFront();
    // }
  }
  //reset function
  function resetHighlight(e) {
    geojson.resetStyle(e.target);
  }
  //zoom into state
  function zoomToFeature(e) {
    map.fitBounds(e.target.getBounds());
  }
  //mouse over highlight and click to zoom
  function onEachFeature(features, layer) {
    layer.on({
      mouseover: highlightFeature,
      mouseout:resetHighlight,
      click:zoomToFeature
  });

    // fix point to states and then zoom and then point to counties
       pointToLayer: function(feature, latlng) {
        
      }
    //legend
    var legend = L.control({
      position: "bottomright"
    });
    legend.onAdd = function () {
      var div = L.DomUtil.create("div", "legend");
      //add colors legend for states
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
