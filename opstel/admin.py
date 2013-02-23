from django.contrib import admin
from django import forms
from opstel.models import Category, Entry
from tinymce.widgets import TinyMCE
from tinymce.views import preview
from django.core.urlresolvers import reverse

class CategoryAdmin(admin.ModelAdmin): 
	prepopulated_fields = { 'slug': ['title'] }
	
admin.site.register(Category, CategoryAdmin)

class EntryAdminForm(forms.ModelForm):
    excerpt = forms.CharField(widget=TinyMCE(mce_attrs={'cols': 80, 'rows': 200}), label=u'Excerpt', required=False)
    body = forms.CharField(widget=TinyMCE(mce_attrs={'cols': 80, 'rows': 200, 'theme_advanced_buttons2' : "preview",}), label=u'Body', required=False)
	#  'plugin_preview_pageurl': reverse('preview', "preview")
    
    class Meta:
        model = Entry
	 
    def formfield_for_foreignkey(self, db_field, request, **kwargs): #defaults author field to current user
	    if db_field.name == 'author':
	        kwargs['initial'] = request.user.id
	        return db_field.formfield(**kwargs)
	    return super(EntryAdmin, self).formfield_for_foreignkey(
	        db_field, request, **kwargs
	    )
	

class EntryAdmin(admin.ModelAdmin): 
	prepopulated_fields = { 'slug': ['title'] }
	list_display = ('title','author','pub_date','status','featured',)
	
	form = EntryAdminForm
	
	
admin.site.register(Entry, EntryAdmin)




