---
title: "Publications"
layout: gridlay
sitemap: false
permalink: /publications/
years: [2016, 2017, 2018, 2019, 2020, 2021]
---

<style>
.jumbotron{
    padding:3%;
    padding-bottom:10px;
    padding-top:10px;
    margin-top:10px;
    margin-bottom:30px;
}
</style>

## Publications

<div class="jumbotron">
### Preprints
{% bibliography --query @unpublished %}
</div>

<div class="jumbotron">
### Journal Articles
{% bibliography --query @article %}
</div>

<div class="jumbotron">
### Conference Proceedings
{% bibliography --query @inproceedings %}
</div>

<div class="jumbotron">
### Other Publications
{% bibliography --query @thesis,@report %}
</div>

