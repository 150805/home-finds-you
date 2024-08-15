from django.urls import path
#from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('', views.house_list, name='house_list'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('house/<int:house_id>/', views.house_detail, name='house_detail'),
    path('house/<int:house_id>/book/', views.book_house, name='book_house'),
    path('logout/', views.logout_view, name='logout'),
]