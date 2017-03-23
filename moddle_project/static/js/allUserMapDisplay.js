function initMap() {
	
	var map = new google.maps.Map(document.getElementById('map'), {
		zoom: 3,
		center: {lat: 51.4927276519, lng: -0.0906372070312}
	});
    
	var markers = [];

    var homepage = location.protocol + '//' + location.host;
    var api = homepage + '/api/coords/';

    $.getJSON(api, function(jd) {
        
        var count = Object.keys(jd.results).length;
        for(var i = 0; i < count; i++) {
            var latitude = jd.results[i].latitude;
            var longitude = jd.results[i].longitude;
            
            var bikeLocation = {lat: latitude, lng: longitude};
            
            var contentString = '<h3>See all of <a href="' + homepage + '/' + jd.results[i].user.username + '">'+ jd.results[i].user.username + '\'s</a> bikes.</h3>';
            
            // Adds a new marker
            addMarker(contentString, bikeLocation,map,markers);	

        }
    });
}

// Adds a marker to the maps
function addMarker(contentString, latLng, map, markers) {
    
    var infowindow = new google.maps.InfoWindow({
          content: contentString
        });

	var marker = new google.maps.Marker({
	  position: latLng,
	  map: map,
	  title: 'My Location'
	});
    
    marker.addListener('click', function() {
          infowindow.open(map, marker);
    });

	markers.push(marker);
}
