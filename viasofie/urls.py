from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[
    # Examples:
    # url(r'^$', 'viasofie.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	#url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)), # admin site
    url(r'^', include('webapp.urls')),
    url(r'^captcha/', include('captcha.urls')),
    #inlineedit
    (r'^inplaceeditform/', include('inplaceeditform.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
]

# admin_site.index_template = 'admin/index.html'