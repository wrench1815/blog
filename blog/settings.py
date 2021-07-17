"""
Django settings for blog project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
from dotenv import load_dotenv
import os
import dj_database_url

# ? load environ file
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.getenv('DEBUG_TOGGLE'))

ALLOWED_HOSTS = ['wrenchlog.herokuapp.com', '127.0.0.1', 'localhost']

# Application definition

INSTALLED_APPS = [
    'mainpages.apps.MainpagesConfig',
    'jazzmin',
    'blogs.apps.BlogsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'blog.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600)

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'statics'

# For Media Files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Settings for whitenoise compression
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Settings for using Dropbox as a backend for Media
DEFAULT_FILE_STORAGE = os.getenv('DEFAULT_FILE_STORAGE')
DROPBOX_OAUTH2_TOKEN = os.getenv('DROPBOX_OAUTH2_TOKEN')
DROPBOX_ROOT_PATH = '/media'

# settings for auto-generated primary keys as per Django 3.2
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# yapf: disable
# Jazzmin settings
JAZZMIN_SETTINGS = {
    # 'show_ui_builder': True,

    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Wrench-log Admin",
    "navbar_small_text": False,

    # Title on the brand, and login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Wrench-log Admin",

    # square logo to use for your site, must be present in static files, used for favicon and brand on top left
    "site_logo": "favicon.ico",

    # Welcome text on the login screen
    "welcome_sign": "Need some Powers?",

    # Copyright on the footer
    "copyright": "wrench1815",

    ############
    # Top Menu #
    ############

    # Links to put along the top menu
    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {
            "name": "Home",
            "url": "admin:index",
            "permissions": ["auth.view_user"]
        },

        # model admin to link to (Permissions checked against model)
        {
            "model": "auth.User"
        },

        # Link to Site
        {
            "name": "To main Site",
            "url": "home",
            "new_window": True
        },

        # App with dropdown menu to all its models pages (Permissions checked against models)
        # {
        #     "app": "books"
        # },
    ],

    #############
    # Side Menu #
    #############

    # Whether to display the side menu
    "show_sidebar": True,

    # Whether to auto expand the menu
    "navigation_expanded": True,

    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],

    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [],

    # Just make sure auth is first
    "order_with_respect_to": ["auth"],

    # Custom icons for side menu apps/models
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "Blogs": "far fa-file-alt",
        "Blogs.Post": "fas fa-pen-nib",
        "mainpages":"far fa-file",
        "mainpages.ChangelogsModel":"fas fa-sync-alt rotate-circular"
    },

    #############
    # UI Tweaks #
    #############

    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": "css/stylesheet.css",
    "custom_js": None,

    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": False,


    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",

    # Render django related popups inside a modal using
    "related_modal_active": True
}

JAZZMIN_UI_TWEAKS={
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-light-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "default",
    # "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-outline-info",
        "warning": "btn-outline-warning",
        "danger": "btn-outline-danger",
        "success": "btn-outline-success"
    },
    "actions_sticky_top": True
}
# yapf: enable

# CKEitor Configurations

#yapf: disable
CKEDITOR_CONFIGS = {
    'default': {
        'width':'100%',
        'height':'500px',
        'skin':'bootstrapck',
        'toolbar':'custom',
        'toolbar_custom': [
            [ 'Styles', 'Format', 'Font', 'FontSize' ],
            [ 'Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'CopyFormatting', 'RemoveFormat' ],
            '/',
            ['TextColor', 'BGColor'],
            [ 'NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'Language' ],
            [ 'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo' ],
            [ 'Find', 'Replace', '-', 'SelectAll' ],
            [ 'Link', 'Unlink', 'Anchor' ],
            [ 'Image', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'Iframe' ],
            [ 'Maximize', 'ShowBlocks' ],
            [ 'Source'],
            [ 'About' ]
        ],
        'stylesSet': [
            {
                'name': 'Paragraph',
                'element': 'p',
                'attributes': {'class': 'p'},
            },
            {
                'name': 'Heading 1',
                'element': 'h1',
                'attributes': {'class': 'h1'},
            },
            {
                'name': 'Heading 2',
                'element': 'h2',
                'attributes': {'class': 'h2'},
            },
            {
                'name': 'Heading 3',
                'element': 'h3',
                'attributes': {'class': 'h3'},
            },
            {
                'name': 'Heading 4',
                'element': 'h4',
                'attributes': {'class': 'h4'},
            },
            {
                'name': 'Heading 5',
                'element': 'h5',
                'attributes': {'class': 'h5'},
            },
            {
                'name': 'Heading 6',
                'element': 'h6',
                'attributes': {'class': 'h6'},
            },
            {
                'name': 'Alert Warning',
                'element': 'div',
                'attributes': {'class': 'alert alert-warning text-white font-weight-bold d-inline-block p-2'},
            },
        ],
        'removePlugins': ','.join(['exportpdf', ]),
        "contentsCss": (STATIC_URL+'css/soft-design-system.min.css', STATIC_URL+'css/stylesheet.css'),

    },
}
# yapf: enable
