[![Build Landscape from LFX](https://github.com/camaraproject/camara-landscape/actions/workflows/build.yml/badge.svg)](https://github.com/camaraproject/camara-landscape/actions/workflows/build.yml)

## Quick Info

- To view the Landscape, go to https://camara.landscape2.io
- The Landscape is used to maintain Member and Participating Organization information on the [CAMARA website](https://camaraproject.org)
- CAMARA Landscape Settings: https://github.com/cncf/landscape2-sites/blob/main/camara/settings.yml

## How It Works

The Landscape is generated nightly from the data in this repository using the [Landscape2](https://github.com/cncf/landscape2) tool. Member data is pulled automatically from LFX each night. LFX-managed fields (name, logo, description, homepage) will be overwritten; project-specific fields (second_path, extra) are preserved.

**Members:** To update your organization's name, logo, or description, please do so through your organization's LFX dashboard at `https://myorg.lfx.dev`. Changes will be reflected in the Landscape automatically on the next automatic build.

**Participating Organizations:** To add or update your entry, please open a pull request as described below, or send a request to adm@lists.camaraproject.org.

## Adding or Updating a Participating Organization Entry

Open a pull request adding or updating your entry in alphabetical order in the appropriate section of `landscape.yml`. Logos must be added to the `hosted_logos` folder in `.svg` format.

### Required Fields
```yaml
- item:
  name: <organization name>
  homepage_url: <website>
  logo: <filename of .svg in the hosted_logos folder>
  crunchbase: <URL to your organization's Crunchbase page>
```

If your organization does not have a Crunchbase entry, you may use the following instead of the `crunchbase` field:
```yaml
  organization:
    name: <organization name>
```

### Optional Fields
```yaml
  # Short description of the organization (2-3 sentences)
  description:

  # One or more landscape categories that reflect your organization's role.
  # An entry can appear in multiple categories simultaneously.
  # Valid values are:
  #   Planning / Associations
  #   Planning / Ecosystem Consultants & Training Partners
  #   Planning / Research Partners
  #   Integration / System Integrators
  #   Solution Provider / Independent Software Vendors
  #   Solution Provider / Portal Solution Providers
  #   Solution Provider / API Exposure Platform Solution Providers
  #   Solution Provider / Transformation Function Solution Providers
  #   Solution Provider / Network Capability Solution Providers
  #   Operation / API Customers
  #   Operation / Hyperscalers, CPaaS Providers, Aggregators
  #   Operation / Operators
  second_path:
    - <Category / Subcategory>

  extra:
    # A public-facing contact email for your organization
    # (e.g. a team or program inbox, not a personal address)
    contact: <email address>

    # Link to a publicly available demo, case study, or use case
    # related to CAMARA APIs or network APIs
    demo_url: <url>
```

### Logo Requirements

Logos must be in **SVG format** (PNG and JPG are not accepted) and placed in the `hosted_logos/` directory. Use a filename that clearly identifies your organization (e.g., `mycompany.svg`) and reference it by filename only (no path) in the `logo` field of `landscape.yml`.

SVG files must not contain embedded text elements -- this means any text in your logo (such as your company name or tagline) must be converted to paths/outlines before saving, rather than remaining as editable text. If this step is skipped, the build will fail. Most vector graphics tools handle this automatically or with a simple menu option:

- **Inkscape:** Path > Object to Path
- **Adobe Illustrator:** Type > Create Outlines
- **Sketch/Figma:** Use "Outline Stroke" or export as "Flatten" SVG
