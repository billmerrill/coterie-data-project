from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from constellations.api_views import ConstellationList, ConstellationDetail, ConstellationDetailByName

urlpatterns = [
    url(r'^$', ConstellationList.as_view(), name='constellation-list'),
    url(r'^(?P<pk>[0-9]+)/', ConstellationDetail.as_view(), name='constellation-detail'),
    url(r'^name/(?P<abbreviation>[\w]+)/', ConstellationDetailByName.as_view(), name='constellation-detail-by-name'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
