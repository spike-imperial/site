---
title: "Team"
layout: gridlay
sitemap: false
permalink: /team/
---

<!-- # Team -->

<!-- <b>We are looking for new graduate students to [join the team!]({{ site.url }}{{ site.baseurl }}/vacancies)</b>-->

<!--- Jump to [staff](#staff), [master and bachelor students](#master-and-bachelor-students), [alumni](#alumni), [administrative support](#administrative-support), [lab visitors](#lab-visitors). -->

<h2 class="team-role">Principal Investigators</h2>
<div class="row">
{% for member in site.data.people.pi %}
{% include_relative member.md %}
{% endfor %}
</div>

<h2 class="team-role">Post-Docs</h2>
<div class="row">
{% for member in site.data.people.postdocs %}
{% include_relative member.md %}
{% endfor %}
</div>

<h2 class="team-role">PhD Students</h2>
<div class="row">
{% for member in site.data.people.phd_students %}
{% include_relative member.md %}
{% endfor %}
</div>

