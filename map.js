


		var map = L.map('map').setView([37.8, -125], 5);

		L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
		maxZoom: 18,
		attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, ' +
			'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
		id: 'mapbox/light-v9',
		tileSize: 512,
		zoomOffset: -1
	}).addTo(map);


	// control that shows state info on hover **************************************************//
	var info = L.control();

	info.onAdd = function (map) {
		this._div = L.DomUtil.create('div', 'info');
		this.update();
		return this._div;
	};

	info.update = function (props) {
		this._div.innerHTML = '<h4>Covid Data</h4>' +  (props ?
			'County Name: <b>' + props.name + '</b><br />' + 'Add General Covid Data Here' + ' ex: people infected'
			: 'Hover over a state or click on it info');

		
	};

	info.addTo(map);

	//end of adding state info on hover
	//***************************************************************************************//



	//This is for styling the geojson
	function style(feature) {
		return {
			weight: 2,
			opacity: 1,
			color: 'white',
			dashArray: '3',
			fillOpacity: 0.7,
			fillColor: 'red'
		};
	}

	function highlightFeature(e) {
		var layer = e.target;

		layer.setStyle({
			weight: 5,
			color: '#666',
			dashArray: '',
			fillOpacity: 0.7
		});

		if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
			layer.bringToFront();
		}

		info.update(layer.feature.properties);
	}


	//Formatting and Adding the Geojson
	var geojson;

	function resetHighlight(e) {
		geojson.resetStyle(e.target);
		info.update();
	}

	function zoomToFeature(e) {
		map.fitBounds(e.target.getBounds());
	}



	function onEachFeature(feature, layer) {

		layer.bindPopup('County Name: ' + feature.properties.name + '</b><br /> Place General County Data Here');

		layer.on({
			mouseover: highlightFeature,
			mouseout: resetHighlight,
			click: zoomToFeature
		});


	}


	//This should add the files from CA to the Map
	
	geojson = L.geoJson(caCounties, {
		style: style,
		onEachFeature: onEachFeature
	}).addTo(map);

/*
//checkbox functions
function countyLines()
{
	var check = document.getElementById("cb1");

	if(check.checked == true)
	{
		//we update!
	}
}

function juvenileInstitutions()
{
	var check = document.getElementById("cb2");

	if(check.checked == true)
	{
		//we update!
	}
}

function adultInstitutions()
{
	var check = document.getElementById("cb3");

	if(check.checked == true)
	{
		//we update!
	}
}

function displayStats(props)
{
	var county = document.getElementById("stats");
	county = props.name;
}*/