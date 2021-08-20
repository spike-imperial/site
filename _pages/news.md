---
title: "News"
id: "news"
layout: textlay
sitemap: true
permalink: /news.html
---
<div class="row mb-1">
<div class="col-md-12">
<div class="row g-0 border rounded overflow-hidden flex-md-row mb-4 shadow-sm h-md-250 position-relative">

<ol class="list-group list-group-flush">
{% for article in site.posts %}
{% if article.type == 'news' %}
{% assign content = article.content | strip_newlines %}
{% if content != '' %}
<a href="{{article.url}}" class="list-group-item list-group-item-action flex-column align-items-start ">
{% else %}
<div class="list-group-item ">
{% endif %}
<div class="d-flex w-100 justify-content-between">
<h5 class="mb-1" style="color:var(--primary)">{{ article.title }}</h5>
<small style="color:gray-dark">{{ article.date | date: "%b %d, %Y" }}</small>
</div>
<p class="mb-1">{{article.summary}}</p>
{% if content != '' %}
</a>
{% else %}
</div>
{% endif %}
{% endif %}
{% endfor %}
</ol>

</div>
</div>
</div>
