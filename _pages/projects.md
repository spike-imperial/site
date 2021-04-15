---
title: "Projects"
layout: gridlay
sitemap: false
permalink: /projects/
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

## Projects

{% for project in site.projects %}
<div class="jumbotron">
<div class="row align-items-end">
<div class="col-md-12 col-sm-12">
<h4><b>{{project.title}}</b></h4>
<!--
<div class="project-sources">
<ul>
{% if project.website %}<a href="{{project.website}}" target="_blank"><i class="fa fa-globe fa-2x"></i></a>{% endif %}
</ul>
</div>
-->
{{project.summary}}
<a href="{{project.url}}">More information</a>
</div>
</div>
</div>
{% endfor %}

