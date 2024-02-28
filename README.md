## Quick Info:
+ To edit the Landscape, please follow the instructions below
+ CAMARA Landscape Settings https://github.com/cncf/landscape2-sites/blob/main/camara/settings.yml

# How it works
Landscape2 is a CLI tool that generates static websites from the information available in the data sources provided. These data sources are passed to the tool via arguments, usually in the form of urls or local paths, and are as follows:
+ **Landscape data:** The landscape data file is a YAML file that describes the items that will be displayed in the landscape website. For backwards compatibility reasons, this file must follow the format and conventions defined in the CNCF [landscape.yml file]([url](https://github.com/cncf/landscape/blob/master/landscape.yml)).
+ **Landscape settings:** The settings file is a YAML file that allows customizing some aspects of the generated landscape website, such as the logo, colors, how to group items or which ones should be featured. For more information about the settings file, please see the [reference documentation]([url](https://github.com/cncf/landscape2/blob/main/docs/config/settings.yml)).
+ **Landscape guide:** The guide file is a YAML file that defines the content of the guide that will be displayed on the landscape website. For more information, please see the [reference documentation]([url](https://github.com/cncf/landscape2/blob/main/docs/config/guide.yml)).
+ **Logos location:** Each landscape item must provide a valid relative reference to a logo image in **SVG format** in the landscape data file (item's logo field). The logos data source defines the location of those logos (base url or local path), so that the tool can get them as needed when processing the landscape items.

# Coming Soon
Additional instructions for community members to update the Landscape
