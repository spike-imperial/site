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
<option class="dropdown-item" value="book">Book</option>
<option class="dropdown-item" value="inproceedings">Conference Proceedings</option>
<option class="dropdown-item" value="article">Journal</option>
<option class="dropdown-item" value="unpublished">Preprint</option>
<option class="dropdown-item" value="phdthesis">Thesis</option>
<option class="dropdown-item" value="workshop">Workshop</option>
</select>
</div>

<div class="dropdown-filter-parent">
<!-- https://stackoverflow.com/questions/51006763/uncaught-typeerror-cannot-read-property-setattribute-of-undefined-at-object-o -->
<label for="dropdown-year-filter">Year</label>
<select id="dropdown-year-filter" class="btn btn-primary dropdown-toggle dropdown-filter" role="button" v-model="selected" aria-haspopup="true" aria-expanded="false" aria-labelledby="dropdownMenuLink">
<option class="dropdown-item" value="all">All</option>
<option class="dropdown-item" value="2021">2021</option>
<option class="dropdown-item" value="2020">2020</option>
<option class="dropdown-item" value="2019">2019</option>
<option class="dropdown-item" value="2018">2018</option>
<option class="dropdown-item" value="2017">2017</option>
<option class="dropdown-item" value="2016">2016</option>
<option class="dropdown-item" value="2015">2015</option>
<option class="dropdown-item" value="2014">2014</option>
<option class="dropdown-item" value="2013">2013</option>
<option class="dropdown-item" value="2012">2012</option>
<option class="dropdown-item" value="2011">2011</option>
<option class="dropdown-item" value="2010">2010</option>
<option class="dropdown-item" value="2009">2009</option>
<option class="dropdown-item" value="2008">2008</option>
<option class="dropdown-item" value="2007">2007</option>
<option class="dropdown-item" value="2006">2006</option>
<option class="dropdown-item" value="2005">2005</option>
<option class="dropdown-item" value="2004">2004</option>
<option class="dropdown-item" value="2003">2003</option>
<option class="dropdown-item" value="2002">2002</option>
<option class="dropdown-item" value="2001">2001</option>
<option class="dropdown-item" value="2000">2000</option>
<option class="dropdown-item" value="1999">1999</option>
<option class="dropdown-item" value="1998">1998</option>
<option class="dropdown-item" value="1997">1997</option>
<option class="dropdown-item" value="1996">1996</option>
<option class="dropdown-item" value="1992">1992</option>
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

