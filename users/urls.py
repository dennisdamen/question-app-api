from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from users import views

# TUT2
# urlpatterns = [
# 	url(r'^users/$', views.users_list),
#     url(r'^users/(?P<pk>[0-9]+)/$', views.user_detail),
# ]

urlpatterns = [
	url(r'^users/$', views.UserList.as_view()),
	url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)