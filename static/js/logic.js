function createMap(subLocations) {

  // Create the tile layer that will be the background of our map.
  var streetmap = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  });


  // Create a baseMaps object to hold the streetmap layer.
  var baseMaps = {
    "Street Map": streetmap
  };

  // Create an overlayMaps object to hold the bikeStations layer.
  var overlayMaps = {
    "Sub Locations": subLocations
  };

  // Create the map object with options.
  var map = L.map("map-id", {
    center: [37.09, -95.71],
    zoom: 5,
    layers: [streetmap, subLocations]
  });

  // Create a layer control, and pass it baseMaps and overlayMaps. Add the layer control to the map.
  L.control.layers(baseMaps, overlayMaps, {
    collapsed: false
  }).addTo(map);
}

function createMarkers(response) {

  // Pull the "locations" property from response.data.
  var locations = response.data.locations;

  // Initialize an array to hold markers.
  var subMarkers = [];

  // Loop through the locations array.
  for (var index = 0; index < locations.length; index++) {
    var location = locations[index];

    // For each station, create a marker, and bind a popup with the station's name.
    var subMarker = L.marker([location.lat, location.lng])
      .bindPopup("<h3>Age: " + location.age + "<h3>Services: " + location.services + "</h3>");

    // Add the marker to the bikeMarkers array.
    subMarkers.push(subMarker);
  }

  // Create a layer group that's made from the bike markers array, and pass it to the createMap function.
  createMap(L.layerGroup(subMarkers));
}


// Perform an API call to the Citi Bike API to get the station information. Call createMarkers when it completes.
d3.json("https://raw.githubusercontent.com/NikkiDao/Neilson_data/main/data/Neilson_edit.json").then(createMarkers);
