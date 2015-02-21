#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Eduardo Elias'
SITENAME = u'Tech Stuff'
SITEURL = 'http://tech.eduardoelias.com'

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'en'
DEFAULT_DATE_FORMAT = "%A, %d de %B de %Y às %H:%M"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'Feed'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Plugins
PLUGIN_PATHS = ['plugins']

STATIC_PATHS = ['images']

THEME = 'themes/simple-bootstrap'

# Blogroll
LINKS = (('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = ( ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

ARTICLE_URL = '{date:%Y}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
