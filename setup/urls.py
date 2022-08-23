from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.urls import re_path, path
from escola.views import alunos, index
from demo.views import SendEmail

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
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("alunos/", alunos, name="alunos"),
    path("email-demo/", SendEmail.as_view(), name="email"),
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
