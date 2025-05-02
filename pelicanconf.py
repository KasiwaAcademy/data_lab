AUTHOR = "McBrown Mwale"
SITENAME = "Kasiwa Academy"
SITEURL = ""

PATH = "content"

TIMEZONE = "Africa/Cairo"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    (
        "My Resume",
        "https://drive.google.com/file/d/1M-Jvl3bvAcARvyDliUgSdh1Em5vZaUeP/view?usp=sharing",
    ),
    ("Github", "https://github.com/KasiwaAcademy"),
)
# ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
# ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ("LinkedIn", "https://www.linkedin.com/in/kasiwaacademy/"),
    ("Youtube", "https://www.youtube.com/@KasiwaAcademy"),
)

DEFAULT_PAGINATION = 10

MARKUP = ("md", "ipynb")

from pelican_jupyter import markup as nb_markup

PLUGINS = [nb_markup]

IGNORE_FILES = [".ipynb_checkpoints"]

THEME = "pelican-themes/aboutwilson"

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
DISQUS_SITENAME = "mcbrownmwale-github-io-data-lab"
