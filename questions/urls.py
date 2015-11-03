from django.conf.urls import include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views
from questions import views


urlpatterns = [
	url(r'^subjects/$', views.SubjectList.as_view()),
	url(r'^subjects/(?P<pk>[0-9]+)/$', views.SubjectDetail.as_view()),
	url(r'^users/$', views.UserList.as_view()),
	url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
	url(r'^questions/$', views.QuestionList.as_view()),
	url(r'^questions/(?P<pk>[0-9]+)/$', views.QuestionDetail.as_view()),
	url(r'^api-token-auth/', views.obtain_auth_token),
]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]