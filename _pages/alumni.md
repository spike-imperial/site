---
title: "Alumni"
layout: gridlay
sitemap: false
permalink: /alumni/
---

<h2 class="team-role">Alumni</h2>
<div class="row">
{% for member in site.data.people.alumni %}
{% include_relative member.md %}
{% endfor %}
</div>

