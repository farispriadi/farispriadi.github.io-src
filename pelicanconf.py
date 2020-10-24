#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import os

AUTHOR = 'farispriadi'
SITENAME = 'iwakali.id'
SITEURL = ''
USER_LOGO_URL = 'iwakali_logo.png'
INDEX_TITLE = 'iwakali.id'
INDEX_DESC = 'Fish with free will'

PATH = 'content'

TIMEZONE = 'Asia/Jakarta'

DEFAULT_LANG = u'en'
DEFAULT_DATE_FORMAT = "%b %d, %Y"

THEME = "voce"

PLUGIN_PATHS = ["plugins", os.path.join(THEME, "plugins")]

LOAD_CONTENT_CACHE = False
SLUGIFY_SOURCE = 'basename'
STATIC_PATHS = [
    'images',
    'files'
]

EXTRA_PATH_METADATA = {
    'images/iwakali_logo.png': {'path': 'iwakali_logo.png'}, 
    'images/tag/iwakali_logo.png': {'path': 'tag/iwakali_logo.png'}, 
    'images/articles/iwakali_logo.png': {'path': 'articles/iwakali_logo.png'}, 
    'images/pages/iwakali_logo.png': {'path': 'pages/iwakali_logo.png'}, 
    'files/favicon-16x16.png': {'path': 'favicon-16x16.png'},
    'files/favicon-32x32.png': {'path': 'favicon-32x32.png'},
    'files/favicon-96x96.png': {'path': 'favicon-96x96.png'},
    # 'files/robots.txt': {'path': 'robots.txt'},
}

#Theme specific
# GOOGLE_ANALYTICS_ID = "UA-123456-7"
# GOOGLE_ANALYTICS_PROP = "siteurl.com"
# TAGLINE = "Site Tagline"
# MANGLE_EMAILS = False
# GLOBAL_KEYWORDS = ("keywords",)


SOCIAL = (
    ("Feed", "https://farispriadi.github.io/feeds/all.atom.xml"),
    ("GitHub", "https://github.com/farispriadi"),
)

LINKS = (
    ("Iwakali.id", "/index.html"),
	("Tentang", "/pages/about.html"),
)

DEFAULT_PAGINATION = 8

RELATIVE_URLS = True
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = [".git"]

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
SUMMARY_MAX_LENGTH = 50

ARCHIVES_URL = "archives.html"
ARCHIVES_SAVE_AS = 'archives.html'
ARTICLE_URL = 'articles/{slug}.html'
ARTICLE_SAVE_AS = 'articles/{slug}.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'
TAGS_URL = 'tag/{slug}.html'

AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
