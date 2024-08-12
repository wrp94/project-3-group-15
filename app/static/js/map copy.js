


// GOAL 1
// Can I render a basic base map? - Set up Leaflet correctly
// Can we fetch the data that we need to plot?

document.addEventListener('DOMContentLoaded', function() {
  // Sample Data (Replace with your data)
  let data = [
      { latitude: 40.7128, longitude: -74.0059 },
      // Add more data points as needed
  ];

  // Create Map Function
  function createMap(data) {
      let map = L.map('map-container').setView([40.7128, -74.0059], 5);

      let street = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
          attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      }).addTo(map);

      let markers = L.markerClusterGroup();
      let heatArray = [];

      data.forEach(function(row) {
          let latitude = row.latitude;
          let longitude = row.longitude;

          if (latitude && longitude) {
              let point = [latitude, longitude];
              let marker = L.marker(point);
              markers.addLayer(marker);

              heatArray.push(point);
          }
      });

      let heatLayer = L.heatLayer(heatArray, { radius: 25, blur: 20 });

      let baseLayers = {
          Street: street
      };

      let overlayLayers = {
          Markers: markers,
          Heatmap: heatLayer
      };

      L.control.layers(baseLayers, overlayLayers).addTo(map);
  }

  createMap(data); // Call the createMap function with your data
});