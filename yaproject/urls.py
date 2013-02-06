from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
import os

from .vcard import views


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.contacts, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url('request_store/$', views.requests_store, name='requests'),
    url(r'^edit/$', views.edit_page, name='edit_page'),
    url(r'^sign-up/member/$', views.accounts_registration,
        name='accounts-registration'),
    url(r'^login/$', views.login_account,
        name='login-account'),
    url(r'^logout/$', views.logout_account,
        name='logout-account'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': os.path.join(settings.PROJECT_ROOT, 'static/')}
        ),
        url(r'^uploads/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': os.path.join(settings.PROJECT_ROOT, 'uploads')}
        )
    )
