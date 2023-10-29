from django.urls import path
from . import views

urlpatterns = [
    path('add_date', views.AddEatingDate.as_view(), name='add_eating_date'),
    path('add_eating', views.AddEating.as_view(), name='add_eating'),
    #path('add_date/<int:pk>', views.AddEating.as_view(), name='add_eating'),
    #path('add_date/add_eating/done', views.AddEating.as_view()),
]
