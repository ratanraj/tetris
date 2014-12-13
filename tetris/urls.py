from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'leaderboard.views.redirectview',name='redirect'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^leaderboard', 'leaderboard.views.leaderboard', name='leaderboard'),
    url(r'^scores', 'leaderboard.views.scores', name='scores'),
    url(r'^userscore', 'leaderboard.views.userscore', name='userscore'),
    url(r'^submissions', 'leaderboard.views.submissions', name='submissions'),
    url('^accounts/login/$', auth_views.login),
    url('^accounts/profile/$',  'leaderboard.views.redirectview',name='redirect'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/accounts/login/'})
)

