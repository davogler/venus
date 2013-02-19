from django.template import Library, Node
from django import template
from django.db.models import get_model
from opstel.models import Category, Entry


from django.template import Context, loader
from django.http import HttpResponse
import datetime
     
register = Library()
register = template.Library()
     
class LatestContentNode(Node):
    def __init__(self, model, num, varname):
        self.num, self.varname = num, varname
        self.model = get_model(*model.split('.'))
    
    def render(self, context):
        context[self.varname] = self.model._default_manager.all()[:self.num]
        return ''
 
def get_latest(parser, token):
    bits = token.contents.split()
    if len(bits) != 5:
        raise TemplateSyntaxError, "get_latest tag takes exactly four arguments"
    if bits[3] != 'as':
        raise TemplateSyntaxError, "third argument to get_latest tag must be 'as'"
    return LatestContentNode(bits[1], bits[2], bits[4])
    
get_latest = register.tag(get_latest)


def nav_categorylist():
	categories = Category.objects.all()
	return {'categories': categories}
	
register.inclusion_tag('opstel/category_nav_list.html')(nav_categorylist)

def entry_list():
    '''a basic events listing view'''
    entries = Entry.objects.filter().order_by('-pub_date')
    now = datetime.datetime.now()
 
    #create a dict with the years and months:events 
    entry_dict = {}
    for i in range(entries[0].pub_date.year, entries[len(entries)-1].pub_date.year-1, -1):
        entry_dict[i] = {}
        for month in range(1,13):
            entry_dict[i][month] = []
    for entry in entries:
        entry_dict[entry.pub_date.year][entry.pub_date.month].append(entry)
 
    #this is necessary for the years to be sorted
    entry_sorted_keys = list(reversed(sorted(entry_dict.keys())))
    list_entry = []
    for key in entry_sorted_keys:
        adict = {key:entry_dict[key]}
        list_entry.append(adict)

    return {'list_entry': list_entry}

register.inclusion_tag('opstel/entry_mini_archive.html')(entry_list)
