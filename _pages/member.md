<style>
.networks {
    text-align: center;
}

.networks ul {
    display: inline-flex; 
    flex-direction: row; 
    flex-wrap: wrap; 
    justify-content: center; 
    list-style: none; 
    padding: 0; 
    margin: 0;
}

.networks li {
    margin-right: 10px;
}

.team-role {
    text-align: center;
    margin-top: 0.5em;
}

.avatar img {
    width: 125px;
    height: 125px;
    object-fit: cover;
}
</style>

<div class="col-lg-4 col-xl-4 mt-4 mb-3">
<div class="avatar">
<img src="{{ site.baseurl }}/assets/images/teampic/{% if member.photo %}{{ member.photo }}{% else %}default.jpg{% endif %}" class="rounded-circle d-block m-auto">
</div>
<h5 class="font-weight-bold" style="text-align: center">{{member.name}} {{member.surname}}</h5>
{% if group == "alumni" %}<h6 style="text-align: center">{{member.alumni.role}}, {{member.alumni.start}}{% if member.alumni.end %}-{{member.alumni.end}}{% endif %}</h6>{% endif %}
{% if group == "internal-collaborator" or group == "external-academic-collaborator" or group == "external-industrial-collaborator" %}<h6 style="text-align: center">{{member.institution}}</h6>{% endif %}

<div class="networks">
<ul>
{% if member.social.email %}<li><a href="mailto:{{ member.social.email }}" target="_blank"><i class="fa fa-envelope-square fa-2x"></i></a></li>{% endif %}
{% if member.social.scholar %}<li><a href="{{ member.social.scholar }}" target="_blank"><i class="ai ai-google-scholar-square ai-2x"></i></a></li>{% endif %}
{% if member.social.github %}<li><a href="{{ member.social.github }}" target="_blank"><i class="fa fa-github-square fa-2x"></i></a></li>{% endif %}
{% if member.social.researchgate %}<li><a href="{{ member.social.researchgate }}" target="_blank"><i class="ai ai-researchgate-square ai-2x"></i></a></li> {% endif %}
{% if member.social.website %}<li><a href="{{ member.social.website }}" target="_blank"><i class="fa fa-globe fa-2x"></i></a></li>{% endif %}
</ul>
</div>
</div>

