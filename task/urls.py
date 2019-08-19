
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('detail/<int:pk>', views.DetailView.as_view(), name='detail' ),
]
