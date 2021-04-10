---
title: "News"
layout: textlay
sitemap: false
permalink: /news.html
---

## News


<div class="jumbotron">
{% for article in site.posts %}
{% assign content = article.content | strip_newlines %}
{% if content != '' %}
<a href="{{article.url}}" style="display:block">
<b>{{ article.title }}</b> {{ article.date | date: "%b %d, %Y" }}
</a>
{% else %}
<b>{{ article.title }} fish</b> {{ article.date | date: "%b %d, %Y" }}
{% endif %}
{{article.summary}}
{% endfor %}
</div>
