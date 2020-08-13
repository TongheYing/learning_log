"""definition of url pattern of learning_logs"""

from django.conf.urls import url

from . import views

urlpatterns = [
    # main page
    url(r'^$', views.index, name='index'),

    # show all subjects
    url(r'^topics/$', views.topics, name='topics'),

    # single subject's exact page
    url(r'^topic/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    # used to add new topic page
    url(r'^new_topic/$', views.new_topic, name='new_topic'),

    # used to add new item
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

    # used to edit items page
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry')
]
