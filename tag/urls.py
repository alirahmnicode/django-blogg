from django.urls import path
from . import views


app_name='tag'

urlpatterns = [
    path('add/<int:obj_id>/', views.add_new_tag, name='add'),
    path('delete/<int:obj_id>/tag/<int:tag_id>/', views.delete_tag, name='delete'),
]