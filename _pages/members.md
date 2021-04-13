{% assign my_array = "" | split: ',' %}
{% for member in site.data.people %}
{% if member.groups contains group %}
{% assign my_array = my_array | push: member %}
{% endif %}
{% endfor %}

{% assign filtered_group = my_array | sort: sorting_criteria %}
<div class="row">
{% for member in filtered_group %}
{% include_relative member.md %}
{% endfor %}
</div>

