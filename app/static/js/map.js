
// GOAL 1
// Can I render a basic base map? - Set up Leaflet correctly
// Can we fetch the data that we need to plot?

function createMap(data) {
    // STEP 1: Init the Base Layers
  
    // Define variables for our tile layers.
    let street = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    })
  
    let topo = L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
      attribution: 'Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)'
    });

    // Step 2: Create the Overlay layers
  let markers = L.markerClusterGroup();
  let heatArray = [];

  for (let i = 0; i < data.length; i++){
    let row = data[i];
    let latitude = row.latitude;
    let longitude = row.longitude;
    let education = row.education

    // create marker
    if (row) {
        // extract coord
        let point = [latitude, longitude];
        console.log(row)
        // make marker
        let marker = L.marker(point);
        let popup = `<h1>${education}</h1>`;
        marker.bindPopup(popup);
        markers.addLayer(marker);

         // add to heatmap
        heatArray.push(point);
    }
  }

        // create layer
    let heatLayer = L.heatLayer(heatArray, {
            radius: 25,
            blur: 20
        });

      // Step 3: BUILD the Layer Controls

  // Only one base layer can be shown at a time.
  let baseLayers = {
    Street: street,
    Topography: topo
  };

  let overlayLayers = {
    Markers: markers,
    Heatmap: heatLayer
  }


  // Step 4: INIT the Map
  d3.select("#map-container").html("");

  //rebulid map

  d3.select("#map-container").html("<div id='map'></div>");


  let myMap = L.map("map", {
    center: [13, 77.5],
    zoom: 9,
    layers: [street, markers]
  });


  // Step 5: Add the Layer Control filter + legends as needed
  L.control.layers(baseLayers, overlayLayers).addTo(myMap);

}
function init() {
    // set default values
    let occupation = d3.select("#occupation").property("value");

    update(occupation);
}

function update(newOccupation) {
    // update 
        let url = `/api/v1.0/get_map/${newOccupation}`;
        d3.json(url).then(function(data) {
            createMap(data);
     })};


d3.select("#filter").on("click", init);

init();