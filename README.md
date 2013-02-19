Venus
============================

**A Django starter project**

This repository is a bare-bones Django project intended for use as a website seed. The project currently features two applications, Flatpages and Opstel, a simple blog.  [TinyMCE](http://www.tinymce.com/) has been configured on both the Flatpages and the blog entries.

###Opstel

Opstel is a simple blog application.  It features [TinyMCE](http://www.tinymce.com/) on the Excerpt and Body fields of the Entry model.  [Disqus](http://disqus.com/) is employed for comments, and can be switched on and off per entry.  

Rough templates exist to populate a basic functioning site. The blog provides template tags for the following typical blog features:

1. Recent Entrys: {% get_latest %}
2. Date-Based Archive: {% entry_list %}
3. Blog Categories: {% nav_categorylist %}
        

Blog URLs are completely 'hackable'.

The **site admin** is pimped with [Grappelli](http://www.grappelliproject.com/) and [Filebrowser](https://github.com/sehmaschine/django-filebrowser), and uses [Pillow](http://pypi.python.org/pypi/Pillow) for image manipulation.

### Running the Project

1. Clone the repository. `git clone git://github.com/davogler/venus.git`

2. Set up a virtual enviroment: mkvirtualenv mynewenv -r requirements.txt
(if using [Virtualenv](http://pypi.python.org/pypi/virtualenv) and [Virtualenvwrapper](http://www.doughellmann.com/projects/virtualenvwrapper/))

3. Create a private settings file `settings_private.py` with the following details and place it in the root directory (note a [Disqus API Key](https://disqus.com/admin/signup/) will be required.):

        import sys
        import os
        
        ADMINS = ()
        MANAGERS = ADMINS
        SECRET_KEY = ''
        TIME_ZONE = ''
        GRAPPELLI_ADMIN_TITLE = ""
        INTERNAL_IPS = ()
        DISQUS_API_KEY = ''
        DISQUS_WEBSITE_SHORTNAME = ''
    
4. Make sure the directory `media/uploads` exists

5. `manage.py syncdb` Placeholder data will populate from two fixtures.
