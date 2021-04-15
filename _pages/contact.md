---
title: "Contact"
layout: gridlay
sitemap: false
permalink: /contact/
---

<link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css"
integrity="sha512-xodZBNTC5n17Xt2atTPuE1HxjVMSvLVW9ocqUKLsCC5CXdbqCmblAshOMAS6/keqq/sMZMZ19scR4PsZChSR7A=="
crossorigin=""/>

<script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js"
integrity="sha512-XQoYMqMTK8LvdxXYG3nZ448hOEQiglfqkJs1NOQV44cWnUrBc8PkAOcXy20w0vlaXaVUearIOBhiXZ5V3ynxwA=="
crossorigin=""></script>

<style>
#mapid { height: 360px; }
</style>

## Contact 

<div id="mapid"></div>
<script>
var mymap = L.map('mapid').setView([51.4990, -0.1795], 15);
L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoiZXJ0c2lnZXIiLCJhIjoiY2tuajd5YXl6M3Z4bzJ1bng2Y2h2aTN3aiJ9.9P1HOw0uH2scinJXCxPcgw', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoiZXJ0c2lnZXIiLCJhIjoiY2tuajd5YXl6M3Z4bzJ1bng2Y2h2aTN3aiJ9.9P1HOw0uH2scinJXCxPcgw'
}).addTo(mymap);
L.marker([51.4990, -0.1795]).addTo(mymap);
</script>

