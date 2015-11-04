from django.conf.urls import include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, QuestionViewSet, SubjectViewSet
from django.contrib import admin

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'subjects', SubjectViewSet)


urlpatterns = router.urls
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
]