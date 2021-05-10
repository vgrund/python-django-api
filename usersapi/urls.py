from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from usersapi.usersapp import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.response import Response

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, login URLs included for the browsable API.
urlpatterns = [
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<id>\b[0-9a-f]{8}\b-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-\b[0-9a-f]{12}\b)/$',
        views.UserDetail.as_view(), name='user-detail'),

    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),

    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(url_name="schema"
                                       ),
        name="swagger-ui",
    ),
]
