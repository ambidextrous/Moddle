// for when a user is viewing another users profile, we do not want
// them to be able to change the location from there.
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
		
				
	});	
}
