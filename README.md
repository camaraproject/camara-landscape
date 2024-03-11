## Quick Info:
+ To edit the Landscape, please follow the instructions below
+ CAMARA Landscape Settings https://github.com/cncf/landscape2-sites/blob/main/camara/settings.yml

# How it works
Landscape2 is a CLI tool that generates static websites from the information available in the data sources provided. These data sources are passed to the tool via arguments, usually in the form of urls or local paths, and are as follows:
+ **Landscape data:** The landscape data file is a YAML file that describes the items that will be displayed in the landscape website. For backwards compatibility reasons, this file must follow the format and conventions defined in the CNCF [landscape.yml file](https://github.com/cncf/landscape/blob/master/landscape.yml).
+ **Landscape settings:** The settings file is a YAML file that allows customizing some aspects of the generated landscape website, such as the logo, colors, how to group items or which ones should be featured. For more information about the settings file, please see the [reference documentation](https://github.com/cncf/landscape2/blob/main/docs/config/settings.yml).
+ **Landscape guide:** The guide file is a YAML file that defines the content of the guide that will be displayed on the landscape website. For more information, please see the [reference documentation](https://github.com/cncf/landscape2/blob/main/docs/config/guide.yml).
+ **Logos location:** Each landscape item must provide a valid relative reference to a logo image in **SVG format** in the landscape data file (item's logo field). The logos data source defines the location of those logos (base url or local path), so that the tool can get them as needed when processing the landscape items.

# New Entries
To add a new entry to the landscape, please open a pull request to add it in alphabetical order to the landscape.yml file. The logo must be added to the hosted_logos directory (in SVG format) and referenced from the logo field.

## Adding and managing landscape entries

When creating new entries, the only 4 required fields are `name`, `homepage_url`, `logo`, and `crunchbase`. 

```yaml
- item:
  name: <entry name>
  homepage_url: <website for entry>
  # filename in hosted_logos folder. Put the svg file into the hosted_logos
  folder and reference its name.
  logo: <logo for entry> 
  crunchbase: <twitter for entry>
```  

Additional keys that can be set are defined below:

```yaml
  # Add statement or intro about the entry or organzation
  content:
  # url for the Twitter account; Only add if the value in Crunchbase is incorrect
  twitter: 
  # url to the repo for the project; will fetch stats if it starts with https://github.com/. If you add a `repo_url` the card will be white instead of grey. 
  repo_url: 
  # url to the GitHub organization for the project; when using `repo_url`, `project_org` can be set pointing to an organization on GitHub, this will have the effect of pulling the information for all the repos belonging to that organization but using `repo_url` for information regarding license and best practices.
  project_org: 
  # additional repos for the project; will fetch stats if they start with https://github.com/
  additional_repos: 
  # Stock Ticker for the organization of the project/entry; normally pulls from Crunchbase but can be overridden here. For delisted and many foreign countries, you'll need to add `stock_ticker` with the value to look up on Yahoo Finance to find the market cap.
  stock_ticker: 
  # description of the entry; if not set pulls from the GitHub repo description
  description: 
  # default branch to reference if not the main one for the repo
  branch: 
  # if the entry is a project hosted by the project, let's you set the maturity level. Should be a value in relations.values.children.id in settings.yml
  project: 
  # url for the CII Best Practices entry if it's not directly mapped to the repo_url
  url_for_bestpractices: 
  # set to false if a repo_url is given but the entry is a project that isn't open source
  open_source: 
  # allows multiple entries with the same repo_url; set for each instance
  allow_duplicate_repo: 
  # set to true if you are using an anonymous organization. You will also need anonymous_organization set in settings.yml
  unnamed_organization:
  # Add special keywords for searching
  # Add 1'- "keyword"' below
  keywords:
  # Extras Extra is an additional category that adds additional information in subkeys that can be defined.
  extra:
  # Subkeys for 'extra'
  accepted:
  annual_review_date:
  annual_review_url: 
  dev_stats_url:
  blog_url:
  artwork_url:
  slack_url: 
  chat_channel:
  clomonitor_name:
  maling_list_url:
  summary_tags:
  summary_use_case:
  summary_business_use_case:
  summary_release_date:
  summary_integrations:
  summary_intro_url:
  clomonitor_name:
```

For some of the key, there is some guidance as listed below.

### Logos

The most challenging part of creating a new landscape is finding SVG images for all projects and companies. These landscapes represent a valuable resource to a community in assembling all related projects, creating a taxonomy, and providing up-to-date logos, and unfortunately, there are no shortcuts.

Do *not* try to convert PNGs to SVGs. You can't automatically go from a low-res to a high-res format, and you'll just waste time and come up with a substandard result. Instead, invest your time finding SVGs and then (when necessary) having a graphic designer recreate images when high res ones are not available.

Tips for finding high quality images:

- Google images is often the best way to find a good version of the logo (but ensure it's the up-to-date version). Search for [grpc logo filetype:svg](https://www.google.com/search?q=grpc+logo&tbs=ift:svg,imgo:1&tbm=isch) but substitute your project or product name for grpc. 
- Wikipedia also is a good source for high quality logos ( search in either the main [Wikipedia](https://en.wikipedia.org/w/index.php?sort=relevance&search=svg&title=Special%3ASearch&profile=advanced&fulltext=1&advancedSearch-current=%7B%7D&ns6=1) or [Wikipedia Commons](https://commons.wikimedia.org/w/index.php?sort=relevance&search=svg&title=Special%3ASearch&profile=advanced&fulltext=1&advancedSearch-current=%7B%7D&ns0=1&ns6=1&ns12=1&ns14=1&ns100=1&ns106=1) ).
- VectorLogoZone ( https://www.vectorlogo.zone/ )
- Also search for 'svg' in the GitHub for the project, as sometimes projects will embed them there.

For new landscapes of any size, you will probably need a graphic artist to rebuild some of the logos for you. 

If the project is hosted/sponsored by an organization but doesn't have a logo, best practice is to use that organization's logo with the title of the project underneath ( [example](https://landscape.cncf.io/selected=netflix-eureka) ). You can use a tool such as [Inkscape](https://inkscape.org/) to add the text.

If you get an error with the image that it has a PNG embedded, you will need to find a different SVG that doesn't include a PNG or work with a graphic artist to rebuild the logo.

#### SVGs Can't Include Text

SVGs need to not rely on external fonts so that they will render correctly in any web browser, whether or not the correct fonts are installed. That means that all embedded text and tspan elements need to be converted to objects. Use of SVGs with embedded text will fail with an error. You can convert the SVGs as using one of the tools below.

##### CloudConvert

1. Go to https://cloudconvert.com/, and click 'Select File' and select the SVG file.
2. Next to 'Convert to', click the dropdown and select 'SVG'
3. There will be wrench icon that appears. Click that.
4. For the option 'Text To Path', select 'Yes' and then click 'Okay'
5. Click 'Convert' to do the conversion and the download the converted file.

##### Adobe Illustrator

1. Select all text
1. With the text selected, go to Object > Expand in the top menu
1. Export file by going to File > Export > Export As in top menu
1. Select SVG from the format drop down and make sure that "Use Artboards" is checked
1. This will open a SVG options box, make sure to set Decimal to 5 (that is the highest possible, so to ensure that sufficient detail is preserved)
1. Click Okay to export

##### Inkscape

1. Select the text
1. Ctrl+K (path combine)
1. Ctrl+J (dynamic offset)
1. Save

### Crunchbase Requirement

We require all landscape entries to include a [Crunchbase](https://www.crunchbase.com/) url. We use the Crunchbase API to fetch the backing organization and headquarters location and (if they exist), Twitter, LinkedIn, funding, parent organization, and stock ticker. For open source, non-affiliated projects, we will just create a nonprofit organization representing the project (if one doesn't already exist), and set the location to the lead developer.

Using an external source for this info saves effort in most cases, because most organizations are already listed. Going forward, the data is being independently maintained and updated over time.

If for certain reason Crunchbase should not be used - we rely on `organization: { name: 'My Organization Name' }` instead of a `crunchbase` field

#### Overriding industries from Crunchbase

To override industries returned from Crunchbase for a specific Crunchbase entry, add it to an `crunchbase_overrides` top-level entry on `landscape.yml`. For instance, the following will set `industries` for Linux Foundation to Linux and Cloud Computing:

```yaml
crunchbase_overrides:
  https://www.crunchbase.com/organization/linux-foundation:
    industries:
      - Linux
      - Cloud Computing
```

`crunchbase_overrides` must be a top-level key on `landscape.yml`, so it should be a sibling of `landscape`. That's to prevent having to override multiple items that share the same Crunchbase URL.
