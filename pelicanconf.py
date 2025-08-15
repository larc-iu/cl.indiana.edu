import datetime

CURRENT_YEAR = datetime.datetime.now().year

AUTHOR = 'Indiana University'
SITENAME = 'Computational Linguistics'
SITEURL = ""

# Basic configuration
PATH = "content"
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'

# Disable all feed generation
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Remove unused blog features
LINKS = ()
SOCIAL = ()
DEFAULT_PAGINATION = False
RELATIVE_URLS = True

# Static content handling
STATIC_PATHS = ['static', 'images', '*.pdf', 'BS.pdf', 'BSMS.pdf']
STATIC_SAVE_AS = '{path}'
STATIC_URL = '{path}'

# Extension support
PLUGIN_PATHS = ['plugins']
PLUGINS = ['plugins.bibliography_markdown', 'plugins.yaml_loader']

# Turn off default templates (including index)
DIRECT_TEMPLATES = []

# Disable categories and tags
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
TAG_SAVE_AS = ''

# Treat all content as pages - include the root content directory
ARTICLE_PATHS = []
PAGE_PATHS = ['']

# URL and path configurations
PATH_METADATA = '(?P<path_no_ext>.*)\..*'
SLUG_REGEX_SUBSTITUTIONS = [(r'[^\w/]+', '-')]
PAGE_URL = '{path_no_ext}.html'
PAGE_SAVE_AS = '{path_no_ext}.html'
INDEX_URL = '{path_no_ext}/index.html'
INDEX_SAVE_AS = '{path_no_ext}/index.html'

# Use basename for slug generation
SLUGIFY_SOURCE = 'basename'

# Use path as translation identifier
TRANSLATION_ID_METADATA = 'path'

# Field formatting
FORMATTED_FIELDS = ['summary', 'path', 'url', 'save_as']

# Remove custom content processor as we're using Markdown now

# Theme
THEME = 'themes/cl-indiana'