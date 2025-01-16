---
layout: default
title: Home
nav_order: 1
description: "GT New Horizons comprehensive guide"
permalink: /
---

# GT New Horizons Guide
{: .fs-9 }

A comprehensive guide covering various aspects of GT New Horizons modpack.
{: .fs-6 .fw-300 }

[Get Started]({{ site.baseurl }}/guides/getting-started){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
[View on GitHub]({{ site.github.repository_url }}){: .btn .fs-5 .mb-4 .mb-md-0 }

---

## Guide Sections

{% assign sorted_guides = site.guides | sort: "nav_order" %}
{% for guide in sorted_guides %}
- [{{ guide.title }}]({{ site.baseurl }}{{ guide.url }})
{% endfor %}

## About this Guide

This guide is a collection of tips, tricks, and detailed information about GT New Horizons, a complex modpack for Minecraft 1.7.10. The information is gathered from community experience and documentation.

## Contributing

This guide is open source. You can contribute by submitting pull requests to our [GitHub repository]({{ site.github.repository_url }}).
