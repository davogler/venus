"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'venus.dashboard.CustomIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for Venus Project
    """
    
    def init_with_context(self, context):
        site_name = get_admin_site_name(context)
        
        # append a link list module for "quick links"
        self.children.append(modules.LinkList(
            _('Quick links'),
            column=1,
            collapsible=False,
            children=[
                [_('Return to site'), '/'],
                [_('Change password'),
                 reverse('%s:password_change' % site_name)],
                [_('Log out'), reverse('%s:logout' % site_name)],
            ]
        ))
                
        # append an app list module for "Applications"
        self.children.append(modules.AppList(
            title=_('Applications'),
            column=1,
            collapsible=True,
            exclude=('django.contrib.*',),
        ))
        
                # append an app list module for "Administration"
        self.children.append(modules.ModelList(
             _('Administration'),
             column=1,
             collapsible=True,
             models=('django.contrib.*',),
         ))

       
        # append a recent actions module
        self.children.append(modules.RecentActions(
            title=_('Recent Actions'),
            column=2,
            collapsible=False,
            limit=5,
        ))
        
                
               
        # append another link list module for "support".
        self.children.append(modules.LinkList(
            _('Media Management'),
            column=2,
            children=[
                {
                    'title': _('FileBrowser'),
                    'url': '/admin/filebrowser/browse/',
                    'external': False,
                },
            ]
        ))
        
        # append another link list module for "support".
        self.children.append(modules.LinkList(
            _('Support'),
            column=2,
            children=[
                {
                    'title': _('Django Documentation'),
                    'url': 'http://docs.djangoproject.com/',
                    'external': True,
                },
                {
                    'title': _('Grappelli Documentation'),
                    'url': 'http://packages.python.org/django-grappelli/',
                    'external': True,
                },
                {
                    'title': _('Local Grappelli Documentation'),
                    'url': '/grappelli/grp-doc/',
                    'external': False,
                },
                {
                    'title': _('Grappelli Google-Code'),
                    'url': 'http://code.google.com/p/django-grappelli/',
                    'external': True,
                },
            ]
        ))
        
     
        
      

