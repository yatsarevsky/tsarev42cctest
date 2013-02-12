from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
import os
from django.views.generic.simple import redirect_to

from .vcard import views


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.contacts, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^request_store/$', views.requests_store, name='requests'),
    url(r'^edit/$', views.edit_page, name='edit_page'),
    url(r'^sign-up/member/$', views.accounts_registration,
        name='accounts-registration'),
    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'accounts/signup_member.html'}, name='login'),
    url(r'^logout/$', views.logout_account,
        name='logout-account'),
    url(r'^accounts/profile/$', redirect_to, {'url': '/edit/'}),
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
