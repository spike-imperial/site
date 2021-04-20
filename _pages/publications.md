---
title: "Publications"
id: "publications"
layout: gridlay
sitemap: false
permalink: /publications/
---

<button id="holy" type="button" class="btn btn-primary">Primary</button>

<div class="dropdown">
  <a class="btn btn-secondary dropdown-toggle" href="#" role="button" id="dropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
    Dropdown link
  </a>

  <div class="dropdown-menu" aria-labelledby="dropdownMenuLink">
    <a class="dropdown-item" href="#">Action</a>
    <a class="dropdown-item" href="#">Another action</a>
    <a class="dropdown-item" href="#">Something else here</a>
  </div>
</div>

{% bibliography %}

<script>
$(document).ready(function() {
    $(".bibliography").addClass("list-group list-group-flush");
    $(".bibliography li").addClass("list-group-item");

    $("#holy").click(function() {
        $(".bib-entry-year-2020").parent().hide();
    });
});
</script>

