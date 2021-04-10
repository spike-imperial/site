<div class="col-lg-4 col-xl-4 mt-4 mb-3">
<div class="avatar">
<img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{% if member.photo %}{{ member.photo }}{% else %}default.jpg{% endif %}" class="rounded-circle d-block m-auto" style="max-width:125px">
</div>
<h5 class="font-weight-bold" style="text-align: center">{{member.name}}</h5>
{% if member.role %}<h6 style="text-align: center">{{member.role}}</h6>{% endif %}
<div class="networks">
<ul>
{% if member.email %}<li><a href="mailto:{{ member.email }}" target="_blank"><i class="fa fa-envelope-square fa-2x"></i></a></li>{% endif %}
{% if member.cv %}<li><a href="{{ site.url }}{{ site.baseurl }}/{{ member.cv }}" target="_blank"><i class="ai ai-cv-square ai-2x"></i></a></li>{% endif %}
{% if member.scholar %}<li><a href="{{ member.scholar }}" target="_blank"><i class="ai ai-google-scholar-square ai-2x"></i></a></li>{% endif %}
{% if member.github %}<li><a href="{{ member.github }}" target="_blank"><i class="fa fa-github-square fa-2x"></i></a></li>{% endif %}
{% if member.researchgate %}<li><a href="{{ member.researchgate }}" target="_blank"><i class="ai ai-researchgate-square ai-2x"></i></a></li> {% endif %}
{% if member.website %}<li><a href="{{ member.website }}" target="_blank"><i class="fa fa-globe fa-2x"></i></a></li>{% endif %}
</ul>
</div>
</div>

