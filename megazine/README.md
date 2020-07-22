AUTHOR
EMAIL
SITENAME
SITEURL
SITESUBTITLE

PROFILE_IMAGE
DONATE_IMAGE
BACKDROP_IMAGE

from datetime import date
YEAR = date.today().year
PATH = 'content'
SITE_DESCRIPTION
TIMEZONE
DONATE
DONATEURL
DEFAULT_LANG

THEME = 'megazine'

DISQUS_SITENAME

# Save Paths
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



# Blogroll
LINKS = (('Link Titel','#'),)

# Social widget
SOCIAL = (('Social', '#'),
          )
CC_LICENSE = 'CC-BY-NC-SA'
