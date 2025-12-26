from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include


from blogapp.sitemaps import PostSitemap

sitemaps = {'post':PostSitemap}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blogapp.urls', namespace='blog')),
    path(
        'sitemap.xml',
        sitemap,
        {'sitemaps': {'posts': PostSitemap}},
        name='django.contrib.sitemaps.views.sitemap'
    )
]
