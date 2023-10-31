from django.urls import path
from . import views

urlpatterns = [
    path('add_date/', views.AddEatingDate.as_view(), name='add_eating_date'),
    path('add_date/add_eating/<int:pk>', views.AddEating.as_view(), name='add_eating'),
    path('add_date/add_eating/done', views.DoneAdd.as_view()),
]
