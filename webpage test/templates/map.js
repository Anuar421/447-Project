


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

	

	// get color depending on population density value
	function getColor(name) {

		//find the covid data for that county
		//covid_cases = ;

		$.ajax({
			type: "POST",
			url: "/shading/",
			data: {data: name}
		  }).done(function( o ) {
			//were done;
		  });
		
		  /*
		var order = document.getElementById({county_cases}).value;
		
		console.log();
		  */
		return  covid_cases > 30000  ? 'red' :
				covid_cases > 10000  ? '#BD0026' :
				covid_cases > 5000   ? '#E31A1C' :
				covid_cases > 1000   ? '#FC4E2A' :
				covid_cases > 500    ? '#FD8D3C' :
				covid_cases > 100    ? '#FEB24C' :
				covid_cases > 10     ? '#FED976' :
										  'white';
	}

	function style(feature) {
		return {
			weight: 2,
			opacity: 1,
			color: 'white',
			dashArray: '3',
			fillOpacity: 0.7,
			fillColor: 'red'//getColor(feature.properties.name) //pass in covid cases to shade
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


	//get county name and state in future
	function getCountyCases(e,county_name) {

		/*
		$.ajax({
			url : "/find-date/",
			type: 'POST',
			
			data: {'click_Data':county_name},

			success: function(){
				console.log("success county cases");
				},
			error: function(error){
					console.log(error);
				}
		});
		
		
		*/
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