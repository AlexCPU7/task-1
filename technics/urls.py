from django.urls import path
from . import views

urlpatterns = [
    path('', views.Catalog.as_view(), name='catalog'),
    path('add-model/', views.AddModel.as_view()),
    path('add-tipper/', views.AddTipper.as_view())
]