from django.conf.urls import patterns, include, url
from django.contrib import admin

from django_blog.sitemaps import BlogSitemap
from django_blog.sitemaps import StaticViewSitemap

admin.autodiscover()

sitemaps = {
    'blog': BlogSitemap,
    'static': StaticViewSitemap
}

from django_blog import settings
urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'apps.blog.views.index', name='home'),
    url(r'^about$','apps.blog.views.about', name='about'),
    url(r'^blog/', include('apps.blog.urls', namespace='blog')),
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #url(r'^grappelli/',include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'404', 'apps.blog.views.not_found'),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',{'sitemaps':sitemaps}),
    #gallery
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    url(r'^items/', include('apps.items.urls')),
    #djangoueditor
    #url(r'^ueditor/',include('DjangoUeditor.urls' )),
    #url(r'^cms/', include('apps.cms.urls', namespace='cms')),
    url(r'^ckeditor/', include('ckeditor.urls')),
)
