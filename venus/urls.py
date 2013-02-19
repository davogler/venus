from django.conf.urls import patterns, include, url
from filebrowser.sites import site
from django.conf import settings
from opstel.models import Entry
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

featured_entry_info_dict = {'queryset':Entry.objects.filter(featured=True), 'date_field': 'pub_date',}

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'venus.views.home', name='home'),
    # url(r'^venus/', include('venus.foo.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),
    url(r'^blog/categories/', include('opstel.urls.categories')),
    url(r'^blog/', include('opstel.urls.entries')),
)

urlpatterns += staticfiles_urlpatterns()
