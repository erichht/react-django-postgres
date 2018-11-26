from django.urls import path
from . import views

app_name = 'LogoHome'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:supplier_id>/type/', views.type, name='type'),
]