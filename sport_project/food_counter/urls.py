from django.urls import path
from . import views

urlpatterns = [
    path('add_or_update/', views.AddOrUpdate.as_view(), name='add_or_update'),
    path('add_date/', views.AddEatingDate.as_view(), name='add_eating_date'),
    path('add_date/add_eating/<int:pk>', views.AddEating.as_view(), name='add_eating'),
    path('add_date/add_eating/done', views.DoneAdd.as_view()),
    path('list_dates', views.ListEatingDates.as_view(), name='list_dates'),
    path('list_eatings/<int:pk>', views.ListEatings.as_view(), name='list_eatings'),
    path('detail_eating/<int:pk>', views.DetailEating.as_view(), name='detail_eating'),
    path('update_eating/<int:pk>', views.UpdateEating.as_view(), name='update_eating'),
    path('delete_eating/<int:pk>', views.delete_eating, name='delete_eating'),

]
