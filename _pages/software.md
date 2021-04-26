---
title: "Software"
id: "software"
layout: gridlay
sitemap: false
permalink: /software/
---

<style>
img{
	border-radius: 10px;
}
iframe {
	width: 175px;
	display: inline;
	vertical-align:middle;
	<!-- margin-bottom:5px; -->
	<!-- margin-left:5px; -->
	<!-- border: 1px solid red; -->
}
.col-md-3 {
	margin:0;
	padding:0;
	margin-top:10px;
	margin-bottom:10px;
	display:block;
	overflow:hidden;
	text-align:center;
	display: table-cell;
	height: auto;
	float: none;
	background:white;
	border-radius:20px;
	<!-- border: 1px solid black; -->
}
.sw-sources ul {
		display: inline-flex; 
		flex-direction: row; 
		flex-wrap: wrap; 
		justify-content: center; 
		list-style: none; 
		padding: 0; 
		margin: 0;
}
.sw-sources li {
		margin-right: 10px;
}
</style>

<html>
<div class="row mb-1">
<div class="col-md-12">
{% for software in site.posts %}
{% if software.type == "software" %}

<div class="row g-0 border rounded overflow-hidden flex-md-row mb-4 shadow-sm h-md-250 position-relative">
<div class="col p-4 d-flex flex-column position-static">

{% if software.logo != nil %}
<img src="{{ software.logo }}" width="200rem" style="border-radius:0px; padding-bottom:10px">
{% endif %}
<div class="d-flex w-100 justify-content-between">
	<div>
		<h4 class="mb-0" style="color:black">{{ software.title }}</h4>
		<b>Author:</b>
		<i>{{ software.author }}</i>
	</div>
	<div class="sw-sources">
		<ul>
		{% if software.paper != nil %}
		<li><a href="{{ software.paper }}" target="_blank"><i class="fa fa-file-alt fa-2x"></i></a></li>
		{% endif %}
		{% if software.github != nil %}
		<li><a href="{{ software.github }}" target="_blank"><i class="fa fa-github-square fa-2x"></i></a></li>
		{% endif %}
		{% if software.webpage != nil %}
		<li><a href="{{ software.webpage }}" target="_blank"><i class="fa fa-globe fa-2x"></i></a></li>
		{% endif %}
		</ul>
	</div>
</div>
<br>
{{ software.content }}
</div>
</div>
{% endif %}
{% endfor %}
</div>
</div>
</html>
