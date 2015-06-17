#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'RaPrism'
SITENAME = ':: RaPrism ::'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
#FEED_ALL_ATOM = None
#CATEGORY_FEED_ATOM = None
#TRANSLATION_FEED_ATOM = None
#AUTHOR_FEED_ATOM = None
#AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Planet Python', 'http://planetpython.org/'),
         )

# Social widget
SOCIAL = (('GitHub #source', 'https://github.com/prismv'),
          ('GitHub #publish', 'https://github.com/RaPrism'),
          ('Twitter', 'https://twitter.com/RaPrism'),
          )

DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

# Themes
THEME = 'blueidea'

# static
STATIC_PATHS = [
    'static/favicon.ico',
]
EXTRA_PATH_METADATA = {
    'static/favicon.ico': {'path': 'favicon.ico'},
}
