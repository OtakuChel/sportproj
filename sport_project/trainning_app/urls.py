from django.urls import path
from . import views

urlpatterns = [
    path('add_size/', views.AddBodySize.as_view()),
    path('add_size/done/', views.DoneView.as_view()),
    path('sizes-db/', views.ListBodySize.as_view()),
    path('sizes-db/<int:pk>', views.DetailBodySize.as_view(), name='size-detail'),
    path('update/<int:pk>', views.BodySizeUpdate.as_view(), name='size-update'),
    path('delete/<int:pk>', views.size_delete, name='size-delete'),
]
