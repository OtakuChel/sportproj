from django.urls import path
from . import views
urlpatterns = [
    path('', views.MainPage.as_view()),
    path('add_size/', views.AddBodySize.as_view()),
    path('done/', views.DoneView.as_view()),
    path('sizes-db/', views.ListBodySize.as_view()),
#    path('sizes-db/<int:pk>', views.DetailFeedBack.as_view(), name='feedback-detail'),
]
