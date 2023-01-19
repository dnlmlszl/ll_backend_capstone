from django.urls import path
from . import views
from .views import BookingViewSet, MenuItemsView, SingleMenuItemView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.home, name="home"),
    path("about", views.about, name="about"),
    path("booking", views.BookingViewSet.as_view({'get': 'list', 'post': 'create', 'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path("menu-items/", views.MenuItemsView.as_view()),
    path("menu_items/<int:pk>", views.SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token),
    path('message/', views.msg),
     path('api-token-auth/', obtain_auth_token),
]
