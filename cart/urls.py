from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [  
    path('', views.gio_hang, name="cart"),        
    path('add_cart/<int:product_id>/', views.them_vao_gio_hang, name="add_cart"),
    path('remove_cart/<int:product_id>/', views.xoa_khoi_gio_hang, name="remove_cart"),
    path('check_out/', views.check_out, name="check_out"),
]