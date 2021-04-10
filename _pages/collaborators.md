---
title: "Collaborators"
layout: gridlay
sitemap: false
permalink: /collaborators/
---

<h2 class="team-role">Internal Collaborators</h2>
<div class="row">
{% for member in site.data.people.collaborators.internal %}
{% include_relative member.md %}
{% endfor %}
</div>

<h2 class="team-role">External Academic Collaborators</h2>
<div class="row">
{% for member in site.data.people.collaborators.external_academic %}
{% include_relative member.md %}
{% endfor %}
</div>

<h2 class="team-role">External Industrial Collaborators</h2>
<div class="row">
{% for member in site.data.people.collaborators.external_industrial %}
{% include_relative member.md %}
{% endfor %}
</div>

