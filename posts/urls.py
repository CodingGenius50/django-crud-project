from django.urls import path
from . import views

app_name = 'posts'   # 👈 namespace যুক্ত করা হলো

urlpatterns = [
    path('home/', views.home, name='home'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('create/', views.create_post, name='create_post'),
    path('post/<int:post_id>/edit/', views.update_post, name='update_post'),
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),



]
