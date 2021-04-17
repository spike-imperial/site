---
title: "Projects"
id: "projects"
layout: gridlay
sitemap: false
permalink: /projects/
---

<style>
/* img{
  border-radius: 10px;
}
iframe {
  width: 175px;
  display: inline;
  vertical-align:right;
  <!-- margin-bottom:5px; -->
  <!-- margin-left:5px; -->
  <!-- border: 1px solid red; -->
} */
/* .col-md-3 {
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
} */

.project-sources ul {
    display: inline-flex; 
    flex-direction: row; 
    flex-wrap: wrap; 
    justify-content: center; 
    list-style: none; 
    padding: 0; 
    margin: 0;
}
.project-sources li {
    margin-right: 10px;
}
</style>

{% for project in site.projects %}
<!-- <div class="jumbotron"> 
<div class="row align-items-end">
<div class="col-md-12 col-sm-12"> -->
<!-- <div class="container"> -->
<!-- {% if project.thumbnail != nil %}
<img class="container__image" src="{{project.thumbnail}}" /> 
{% endif %} -->
<div class="row mb-1">
<div class="col-md-12">
<div class="row g-0 border rounded overflow-hidden flex-md-row mb-4 shadow-sm h-md-250 position-relative">
<div class="col p-4 d-flex flex-column position-static">
<strong class="d-inline-block mb-2 text-primary">On-going</strong>
<h3 class="mb-0">{{project.title}}</h3>
<div class="mb-1 text-muted">
{{project.date | date: "%b %d, %Y"}}
</div>
<p class="card-text mb-auto">{{project.summary}}</p>
{% assign content = project.content | strip_newlines %}
{% if content != '' %}
<a href="{{project.url}}" class="stretched-link">Continue reading</a>
{% endif %}
</div>
{% if project.thumbnail %}
<div class="col-auto d-none d-lg-block">
<!-- <p>bla</p> -->
<img role="img"  style="margin-top: 15px" src="{{project.thumbnail}}" height="200" max-width="20" focusable="false">
</div>
{% endif %}
</div>
</div>
</div>

<!-- <svg class="bd-placeholder-img" width="200" height="250" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Placeholder: Thumbnail" preserveAspectRatio="xMidYMid slice" focusable="false"><title>Placeholder</title><rect width="100%" height="100%" fill="#55595c"/><text x="50%" y="50%" fill="#eceeef" dy=".3em">Thumbnail</text></svg> -->
<!-- <div class="container__text"> 
<h4><b>{{project.title}}</b></h4>
{{project.summary}}
{% assign content = project.content | strip_newlines %}
{% if content != '' %}
<a href="{{project.url}}">More information</a>
{% endif %}
<!-- </div> -->

<!--
<div class="project-sources">
<ul>
{% if project.website %}<a href="{{project.website}}" target="_blank"><i class="fa fa-globe fa-2x"></i></a>{% endif %}
</ul>
</div>
-->

<!-- </div>
</div>
</div> --> 
{% endfor %}

