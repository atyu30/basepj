from django.views import generic
from .models import Item, Photo, Tag
        
class IndexView(generic.ListView):
    template_name = 'items/index.html'
    def get_queryset(self):
        return Item.objects.all()
        #return Item.objects.all()[:5]
        
class ListView(generic.ListView):
    model = Item
    template_name = 'items/items_list.html'
        
class ItemDetailView(generic.DetailView):
    model = Item    
    template_name = 'items/items_detail.html'
        
class PhotoDetailView(generic.DetailView):
    model = Photo
    template_name = 'items/photos_detail.html'


class ExtraContext(object):
    extra_context = {}

    def get_context_data(self, **kwargs):
        context = super(ExtraContext, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context

