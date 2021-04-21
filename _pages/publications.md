---
title: "Publications"
id: "publications"
layout: gridlay
sitemap: false
permalink: /publications/
---

<style>
.dropdown-filter {
    margin-left: 5px;
}

.dropdown-filter-parent {
    padding-left: 20px;
}
</style>

<div class="row">
<div class="dropdown-filter-parent">
<label for="dropdown-type-filter">Type</label>
<select id="dropdown-type-filter" class="btn btn-primary dropdown-toggle dropdown-filter" role="button" v-model="selected" aria-haspopup="true" aria-expanded="false" aria-labelledby="dropdownMenuLink">
<option class="dropdown-item" value="all">All</option>
<option class="dropdown-item" value="inproceedings">Conference Proceedings</option>
<option class="dropdown-item" value="article">Journal</option>
<option class="dropdown-item" value="unpublished">Preprint</option>
<option class="dropdown-item" value="phdthesis">Thesis</option>
</select>
</div>

<div class="dropdown-filter-parent">
<!-- https://stackoverflow.com/questions/51006763/uncaught-typeerror-cannot-read-property-setattribute-of-undefined-at-object-o -->
<label for="dropdown-year-filter">Year</label>
<select id="dropdown-year-filter" class="btn btn-primary dropdown-toggle dropdown-filter" role="button" v-model="selected" aria-haspopup="true" aria-expanded="false" aria-labelledby="dropdownMenuLink">
<option class="dropdown-item" value="all">All</option>
<option class="dropdown-item" value="2020">2020</option>
<option class="dropdown-item" value="2019">2019</option>
</select>
</div>
</div>

{% bibliography %}

<script>
$(document).ready(function() {
    $(".bibliography").addClass("list-group list-group-flush");
    $(".bibliography li").addClass("list-group-item");

    $(".dropdown-filter").on("change", function() {
        var year = $("#dropdown-year-filter").val();
        var type = $("#dropdown-type-filter").val();
    
        if (year == 'all' && type == 'all') {
            $(".bib-entry").parent().show();    
        }
        else {
            var classes = ""
            if (year != 'all') {
                classes += ".bib-entry-year-" + year;
            }
            if (type != 'all') {
                classes += ".bib-entry-type-" + type;
            }
            
            $(".bib-entry").parent().hide();
            $(classes).parent().show();
        }
    });
});
</script>

