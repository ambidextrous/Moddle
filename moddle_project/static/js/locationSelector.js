function initMap() {
	
	var userLat = parseFloat(document.getElementById("userLat").innerHTML);
	var userLong = parseFloat(document.getElementById("userLong").innerHTML);
	if (isNaN(userLat) || isNaN(userLong)) {
		// The Boyd Orr: centre of the known universe
		var myLatlng = {lat: 55.87371280304047, lng: -4.2924705147743225};
	} else {
		var myLatlng = {lat: userLat, lng: userLong};
	}	
	
	
	var map = new google.maps.Map(document.getElementById('map'), {
		zoom: 8,
		center: myLatlng
	});
	
	var originalMarker = new google.maps.Marker({
		position: myLatlng,
		map: map,
		title: 'Home sweet home!'
	});
	
	var markers = [];

	google.maps.event.addListener(map, "click", function (e) {
		
		originalMarker.setMap(null);

		// lat and lng are available in the e object
		var latLng = e.latLng;
		var userChosenLat = e.latLng.lat();
		var userChosenLong = e.latLng.lng();
		console.log('userChosenLat = ', userChosenLat);
		console.log('userChosenLong = ', userChosenLong);
		
		if (confirm('Are you sure you want to set this position as your new location?')) {
		
			// Calls function to send GET request to Django view
			sendToDjango(userChosenLat, userChosenLong);
			
			// Deletes any existing markers
			if (markers.length > 0) {
				deleteMarkers(map,markers);
			} 
			
			// Adds a new marker
			addMarker(latLng,map,markers);				
			
		} else {
		
			// Do nothing!
		}			
	});	
}

// Sends a lat-long info to Django view as GET request
function sendToDjango(userChosenLat,userChosenLong) {
	// Using the core $.ajax() method
	$.ajax({ 
		// The URL for the request
		url: "/storelatlong",
		// The data to send (will be converted to a query string)
		data: {
			lng: userChosenLong,
			lat: userChosenLat
		},
		success: function(json) {
			console.log("Success!");
		},
		error: function(xhr,errmsg,err) {
			console.log(xhr.status + ": " + xhr.responseText);
		}
	});	
}

// Adds a marker to the maps
function addMarker(latLng,map,markers) {
	var marker = new google.maps.Marker({
	  position: latLng,
	  map: map,
	  title: 'My Location'
	});
	markers.push(marker);
}

// Sets map on all markers in array.
function setMapOnAll(map,markers) {
	for (var i = 0; i < markers.length; i++) {
		markers[i].setMap(null);
	}
	markers[0].setMap(null);
}

// Removes marker from map, but not from array
function clearMarkers(map,markers) {
	setMapOnAll(map,markers);
}

// Deletes all marker from array
function deleteMarkers(map,markers) {
	clearMarkers(map,markers);
	markers = [];
}