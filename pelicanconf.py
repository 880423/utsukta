#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Utsukta'
EMAIL = 'contact@utsukta.org'
SITENAME = 'Utsukta '
SITEURL = ''
SITESUBTITLE = 'Stay Curious.'

PROFILE_IMAGE =  '/uploads/logo.png'
DONATE_IMAGE = '/uploads/donate.png'
BACKDROP_IMAGE = '/uploads/backdrop.jpg'

PATH = 'content'
SITE_DESCRIPTION = '\'Utsukta\' is a blog where we publish works motivated by the pursuit of truth.'
TIMEZONE = 'Asia/Calcutta'
DONATE = 'If you appreciate the efforts of our team, you can <a href="upi://pay?pa=utsukta@sbi&pn=Utsukta&mc=0000&tn=Pay%to%Utsukta&cu=INR" >buy</a> us a coffee.'
DONATEURL = 'upi://pay?pa=utsukta@sbi&pn=Utsukta&mc=0000&tn=Pay%to%Utsukta&cu=INR'
DEFAULT_LANG = 'en'

THEME = 'megazine'
THEME_STATIC_DIR = ''
#BOOT = 'journal'
# Feed generation is usually not desired when developing

DISPLAY_CAT_ON_MENU = True
DISPLAY_RECENT_ON_MENU = True
DISQUS_SITENAME = 'utsukta'

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
RSS_FEED_SUMMARY_ONLY = True

# Save Paths
#ARTICLE_PATHS = ['articles']
USE_FOLDER_AS_CATEGORY = True
ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
TAG_URL = 'tags/{slug}/'
TAG_SAVE_AS = 'tags/{slug}/index.html'
TAGS_URL = 'tags.html'
DRAFT_URL = 'drafts/index.html'
DRAFT_SAVE_AS = 'drafts/{slug}.html'


ARCHIVES_SAVE_AS = 'archives/index.html'
ARCHIVES_URL = 'archives'
DAY_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/{date:%B}/{date:%d}/index.html'
YEAR_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/{date:%B}/index.html'

# Plugins
PLUGINS = ['sitemap', 'i18n_subsites','category_meta']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

I18N_SUBSITES = {
    'hi': {
        'SITENAME': ' उत्सुकता ' ,
        'THEME_STATIC_DIR': '',
        'THEME': 'megazine_hi',
        'STATIC_PATHS': ['uploads', 'images'],
        'SITESUBTITLE': 'जिज्ञासा बनाए रखें। ',
        'AUTHOR': 'उत्सुकता ',
        'SITE_DESCRIPTION':'उत्सुकता है जानने की, क्यों और कैसे, खुद से सवाल करने की।  ',
        'DONATE':'यदि आप हमारी टीम के प्रयासों की सराहना करते हैं, तो आप हमें एक कॉफी खरीद सकते हैं।',
       }
    }

DATE_FORMATS = {
    'en': ('en_US.utf8','%a, %d %b %Y'),
    'hi': ('hi_IN.utf8','%a, %d %b %Y'),
}


# Blogroll
LINKS = (('Utsukta Blog','https://blog.utsukta.org'),)

# Social widget
YOUTUBE = "https://www.youtube.com/channel/UClRzYw8JAQ6ZbPpXot2MqPA"


DIRECT_TEMPLATES = ['index', 'archives', 'categories']
#PAGINATED_PAGE_TEMPLATES = ('categories', 'archives')

STATIC_PATHS = ['uploads', 'images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

CC_LICENSE = 'CC-BY-NC-SA'

DEFAULT_PAGINATION = 8
PAGINATED_DIRECT_TEMPLATES = ('categories', 'archives','category', 'index')
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
