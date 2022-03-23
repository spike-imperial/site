---
title: "Team"
layout: gridlay
sitemap: true
permalink: /team/
---

<!-- # Team -->

<!-- <b>We are looking for new graduate students to [join the team!]({{ site.url }}{{ site.baseurl }}/vacancies)</b>-->

<!--- Jump to [staff](#staff), [master and bachelor students](#master-and-bachelor-students), [alumni](#alumni), [administrative support](#administrative-support), [lab visitors](#lab-visitors). -->

<h2 class="team-role">Principal Investigators</h2>
{% assign group = "pi" %}
{% assign sorting_criteria = "name" %}
{% include_relative members.md %}

<!--- 
<h2 class="team-role">Post-Docs</h2>
{% assign group = "post-doc" %}
{% assign sorting_criteria = "name" %}
{% include_relative members.md %}
-->

<h2 class="team-role">PhD Students</h2>
{% assign group = "phd-student" %}
{% assign sorting_criteria = "name" %}
{% include_relative members.md %}

