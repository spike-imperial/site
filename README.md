# SPIKE Research Group Website
[![Netlify Status](https://api.netlify.com/api/v1/badges/0e446421-a3b6-4aec-a324-ba4f47b1317f/deploy-status)](https://app.netlify.com/sites/spike-icl/deploys)

## Testing the website in your computer

## Adding a publication
The `publications` folder contains a BibTeX file called `ref.bib` in which all the publications are stored. Therefore, any publication you may add must be formatted in BibTeX. If you don't have a BibTeX prepared for your publications, you can:
* Use the ones in the file as a reference; or 
* Try to find your publication in [DBLP](https://dblp.org/) and get the BibTeX from there. These BibTeX usually contain a lot of data that you may wish to remove (e.g., editors, url, doi, timestamp, biburl, bibsource).

Once you have your BibTeX available, you can also add the following custom entries:
* `_pdf` - a link to a website in which the website can be found.
* `_code` - a link to the repository containing the implementation of your paper (or a binary).
* `_type` - this is added in case you want to specify a custom type which cannot be specified through BibTeX's usual tags (`unpublished`, `inproceedings`, `article`, ...). The currently supported custom types are (if you need any other type of custom type, let us know!):
    * `workshop` - if your paper has been published in a workshop.
We can add more custom entries if you want (e.g., if you want to add a link to a set of slides, a poster, ...).

If for some reason your publication does not appear once added, let us know (there might be a problem with the filtering).

