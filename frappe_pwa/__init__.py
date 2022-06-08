# -*- coding: utf-8 -*-
from __future__ import unicode_literals

__version__ = '1.0.2'

def after_migrate():
    from frappe_pwa.frappe_pwa.doctype.web_app_manifest.web_app_manifest import configure_pwa
    configure_pwa()