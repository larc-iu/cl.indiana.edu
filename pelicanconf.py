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
# Note: STATIC_PATHS takes literal paths, not globs -- the '*.pdf' entry below
# never matched anything, so slide decks must be listed by name.
STATIC_PATHS = ['static', 'images', '*.pdf', 'BS.pdf', 'BSMS.pdf',
                'git_tutorial.pdf', 'introLatex.pdf', 'Supercomputing_at_IU.pdf']
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

# Everything is a page except news/ and stories/, which are dated articles.
# Their folder name becomes the category, which is how templates tell them apart.
ARTICLE_PATHS = ['news', 'stories', 'colloquium']
PAGE_PATHS = ['']
PAGE_EXCLUDES = ['news', 'stories', 'colloquium']

# How much news the home page shows: at most HOME_NEWS_MAX posts, and none
# older than HOME_NEWS_MONTHS. The cutoff is precomputed as a year*12+month
# integer so templates can compare it without any timezone-aware date math.
HOME_NEWS_MAX = 3
HOME_NEWS_MONTHS = 6
HOME_STORIES_MAX = 3
_now = datetime.datetime.now()
HOME_NEWS_CUTOFF_MONTH = _now.year * 12 + _now.month - HOME_NEWS_MONTHS

# URL and path configurations
PATH_METADATA = '(?P<path_no_ext>.*)\..*'
SLUG_REGEX_SUBSTITUTIONS = [(r'[^\w/]+', '-')]
PAGE_URL = '{path_no_ext}.html'
PAGE_SAVE_AS = '{path_no_ext}.html'
ARTICLE_URL = '{path_no_ext}.html'
ARTICLE_SAVE_AS = '{path_no_ext}.html'
DEFAULT_DATE_FORMAT = '%B %d, %Y'
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