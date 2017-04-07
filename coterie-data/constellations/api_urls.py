from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from constellations.api_views import ConstellationList, ConstellationDetail

urlpatterns = [
    url(r'^$', ConstellationList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', ConstellationDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
