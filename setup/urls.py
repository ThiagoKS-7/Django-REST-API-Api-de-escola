from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.urls import re_path, path, include
from escola.views import index, api
from email_sender.views import SendEmail

schema_view = get_schema_view(
    openapi.Info(
        title="Django School REST API",
        default_version="v1",
        description="Curso introdutório de REST API da Alura",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="thiagokasper101@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
BASE_URL = "api/v1/"
urlpatterns = [
    path("", index, name="index"),
    path(BASE_URL, api, name="api"),
    path(BASE_URL + "escola/", include("escola.urls")),
    path(BASE_URL + "email/", SendEmail.as_view(), name="email"),
    path("admin/", admin.site.urls),
]
urlpatterns += [
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
]
