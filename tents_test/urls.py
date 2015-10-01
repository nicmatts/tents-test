from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'store.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^products/', include('store.urls'), name='store'),
    url(r'^admin/', include(admin.site.urls)),
]
