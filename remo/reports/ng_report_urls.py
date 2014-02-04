from django.conf.urls.defaults import patterns, url

# New Generation reporting system
urlpatterns = patterns(
    'remo.reports.views',
    url(r'^new/$', 'edit_ng_report', name='reports_new_ng_report'),
    url(r'^mentor/(?P<mentor>[A-Za-z0-9_]+)/$', 'list_ng_reports',
        name='list_ng_reports_mentor'),
    url(r'^rep/(?P<rep>[A-Za-z0-9_]+)/$', 'list_ng_reports',
        name='list_ng_reports_rep'),
    url(r'^$', 'list_ng_reports', name='list_ng_reports'),
)
