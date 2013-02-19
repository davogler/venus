from django.conf.urls.defaults import *

from opstel.models import Category

urlpatterns = patterns('',
	(r'^$', 'django.views.generic.list_detail.object_list', {'queryset':Category.objects.all() }, 'opstel_category_list'),
	(r'^(?P<slug>[-\w]+)/$', 'opstel.views.category_detail', {}, 'opstel_category_detail'),
)