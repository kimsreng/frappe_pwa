# -*- coding: utf-8 -*-
# Copyright (c) 2021, Monogramm and Contributors
# See license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils.jinja import is_rtl

no_sitemap = 1
base_template_path = "templates/www/sw.js"


def get_context(context):
	hooks = frappe.get_hooks()

	context.include_js = hooks["app_include_js"]
	style_urls = hooks["app_include_css"]
	context.include_css = get_rtl_styles(style_urls) if is_rtl() else style_urls

	if not context.get("favicon"):
		context["favicon"] = "/assets/frappe/images/favicon.png"

	settings = frappe.get_single("Website Settings")
	if settings.favicon and settings.favicon != "attach_files:":
		context["favicon"] = settings.favicon

	# TODO Sync cache version with Frappe cache?
	service_worker = frappe.db.get_singles_dict("Service Worker")
	context.sw_version = service_worker.version or 1

def get_rtl_styles(style_urls):
	rtl_style_urls = []
	for style_url in style_urls:
		rtl_style_urls.append(style_url.replace('/css/', '/css-rtl/'))
	return rtl_style_urls