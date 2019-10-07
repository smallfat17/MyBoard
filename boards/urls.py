from django.conf.urls import url
from . import views

app_name = 'boards'
urlpatterns = [
    url(r'^(?P<pk>\d+)/$', views.TopicListView.as_view(), name='board_topics'),
    url(r'^(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
    url(r'^(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$', views.PostListView.as_view(), name='topic_posts'),
    url(r'^(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/reply/$', views.topic_reply, name='topic_reply'),
    url(r'^(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/posts/(?P<post_pk>\d+)/edit/$',
        views.PostUpdateView.as_view(), name='edit_post'),
    # url(r'^(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/posts/(?P<post_pk>\d+)/edit/$',
    #     views.PostUpdateView.as_view(), name='edit_post'),
]