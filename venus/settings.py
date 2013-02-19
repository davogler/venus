# Django settings for venus project.
import os.path

DEBUG = True
TEMPLATE_DEBUG = DEBUG

#-------details below in settings_private.py --------#

ADMINS = (
     
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(os.path.dirname(__file__),'venus.sqlite'),                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}


SECRET_KEY = ''

TIME_ZONE = ''

GRAPPELLI_ADMIN_TITLE = ""

INTERNAL_IPS = ('127.0.0.1',)


DISQUS_API_KEY = ''
DISQUS_WEBSITE_SHORTNAME = ''

#-------private settings outside of repository-----#

from settings_private import *

#-------private settings outside of repository-----#



# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

ROOT_PATH = os.path.dirname(__file__)

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(ROOT_PATH, '../media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = (
	os.path.join(ROOT_PATH, '../assets')
)

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/assets/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(ROOT_PATH, './static'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

FIXTURE_DIRS = (
   os.path.join(ROOT_PATH, '../fixtures'),
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'venus.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'venus.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(ROOT_PATH, '../templates'),
)

FILEBROWSER_DIRECTORY = 'uploads/'
FILEBROWSER_URL_FILEBROWSER_MEDIA =  STATIC_URL + "filebrowser/"
FILEBROWSER_PATH_FILEBROWSER_MEDIA = os.path.join(STATIC_ROOT, 'filebrowser/')
FILEBROWSER_MAX_UPLOAD_SIZE = '10485760'
FILEBROWSER_EXTENSIONS = {
    'Folder': [''],
    'Image': ['.jpg','.jpeg','.gif','.png','.tif','.tiff'],
    'Document': ['.pdf','.doc','.rtf','.txt','.xls','.csv'],
    'Video': ['.mov','.wmv','.mpeg','.mpg','.avi','.rm'],
    'Audio': ['.mp3','.mp4','.wav','.aiff','.midi','.m4p']
}

FILEBROWSER_SELECT_FORMATS = {
    'file': ['Folder','Image','Document','Video','Audio'],
    'image': ['Image'],
    'document': ['Document'],
    'media': ['Video','Audio'],
}


FILEBROWSER_VERSIONS = {
    'admin_thumbnail': {'verbose_name': 'Admin Thumbnail(60x60)', 'width': 60, 'height': 60, 'opts': 'crop'},
    'thumbnail': {'verbose_name': 'Thumbnail(60x60)', 'width': 60, 'height': 60, 'opts': 'crop'},
    'small': {'verbose_name': 'Small(140x-)', 'width': 140, 'height': '', 'opts': ''},
    'medium': {'verbose_name': 'Medium(320x-)', 'width': 320, 'height': '', 'opts': ''},
    'big': {'verbose_name': 'Big(460x-)', 'width': 460, 'height': '', 'opts': ''},
    'large': {'verbose_name': 'Large(680x-)', 'width': 680, 'height': '', 'opts': ''},
}
FILEBROWSER_ADMIN_VERSIONS = ['thumbnail', 'small', 'medium', 'big', 'large']
FILEBROWSER_ADMIN_THUMBNAIL = 'admin_thumbnail'

TINYMCE_JS_URL = os.path.join(STATIC_URL, 'js/tiny_mce/tiny_mce.js')
TINYMCE_JS_ROOT = os.path.join(STATIC_ROOT, 'js/tiny_mce')

TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,paste,searchreplace,advimage,preview",
    'theme': "advanced",
    'theme_advanced_resizing': True,
    'theme_advanced_resizing_min_height' : 200,
    'theme_advanced_resizing_min_width' : 320,
    'relative_urls': False,
    'cleanup_on_startup': True,
    'auto_cleanup_word' : True,
    'custom_undo_redo_levels': 10,
    'paste_auto_cleanup_on_paste' : True,
    'extended_valid_elements' : "a[name|href|target=_blank|title|onclick],img[class|src|border=0|alt|title|hspace|vspace|width|height|align|onmouseover|onmouseout|name],hr[class|width|size|noshade],font[face|size|color|style],span[class|align|style]",
     'theme_advanced_buttons1' : "bold,italic,underline,|,justifyleft,justifycenter,justifyright,justifyfull,|,link,unlink,image,styleselect,formatselect,removeformat,cleanup,|,bullist,numlist,outdent,indent,hr,blockquote,replace,|,code", 
     }

TINYMCE_SPELLCHECKER = False
TINYMCE_COMPRESSOR = False
TINYMCE_FILEBROWSER = True




INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'grappelli',
    'filebrowser',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.flatpages',
    'disqus',
    'opstel',
    'tinymce',
    'flatpages_tinymce',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
