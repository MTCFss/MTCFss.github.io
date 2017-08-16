from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^' + settings.ADMIN_PATH + '/', admin.site.urls),
    url(r'^nested_admin/', include('nested_admin.urls')),
    url(r'', include('website.urls'), name='website'),
    url(r'blog/', include('blog.urls'), name='blog'),
    url(r'inscription/', include('inscription.urls'), name='inscription'),
    url(r'^wordpress/', include('wordpress.urls')),
    url(r'^quiz/', include('quiz.urls')),
    url(r'^event/', include('event.urls')),
    url(r'', include('db.urls')),
]

if settings.DEBUG and settings.DEBUG_TOOLBAR_INSTALLED:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
