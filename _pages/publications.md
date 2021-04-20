---
title: "Publications"
id: "publications"
layout: gridlay
sitemap: false
permalink: /publications/
---

<!-- https://stackoverflow.com/questions/51006763/uncaught-typeerror-cannot-read-property-setattribute-of-undefined-at-object-o -->
<select id="dropdown-year-filter" class="btn btn-primary dropdown-toggle" role="button" v-model="selected" aria-haspopup="true" aria-expanded="false" aria-labelledby="dropdownMenuLink">
    <option class="dropdown-item" value="all">All</option>
    <option class="dropdown-item" value="2019">2019</option>
    <option class="dropdown-item" value="2020">2020</option>
</select>

{% bibliography %}

<script>
$(document).ready(function() {
    $(".bibliography").addClass("list-group list-group-flush");
    $(".bibliography li").addClass("list-group-item");

    $("#dropdown-year-filter").on("change", function() {
        if ($(this).val() == 'all') {
            $(".bib-entry").parent().show();
        }
        else {
            $(".bib-entry").parent().hide();
            $(".bib-entry-year-" + $(this).val()).parent().show();
        }
    });
});
</script>

