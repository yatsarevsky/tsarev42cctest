from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import ListView, DetailView
from django.conf import settings
import os

from .vcard.models import VCard
from .vcard import views


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(model=VCard, template_name='index.html'),
        name='home'),
    url(r'^vcard/(?P<pk>\d+)/$', DetailView.as_view(model=VCard),
        name='vcard'),
    url(r'^vcard/(?P<pk>\d+)/edit/$', views.edit_page,
        name='edit_page'),
    url('request_store/$', views.requests_store, name='requests'),
    url('settings/$', views.settings, name='settings'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sign-up/member/$',
        views.accounts_registration,
        name='accounts-registration'
    ),
    url(r'^login/$',
        views.login_account,
        name='login-account'
    ),
    url(r'^logout/$',
        views.logout_account,
        name='logout-account'
    ),
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
