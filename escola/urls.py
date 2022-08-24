from django.urls import path

from escola.views import AlunoList, AlunoDetail

urlpatterns = [
    path("", AlunoList.as_view(), name="AlunoList"),
    path("create/", AlunoDetail.as_view(), name="AlunoDetail"),
]
