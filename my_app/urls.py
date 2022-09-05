from django.urls import path
from . import views

app_name = 'my_app'
urlpatterns = [  
    path('trang-chu/', views.trang_chu, name="index"),  #.html    
    path('trang-store/', views.trang_store, name="store"),  #.html    
    path("<slug:slug>/",views.product_detail , name="product_detail"),  
    path("trang-store/<slug:slug>",views.trang_store , name="category"),  
    #path("trang-chu/search",views.trang_search, name="search"), 
]