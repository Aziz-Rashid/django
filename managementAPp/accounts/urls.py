from django.conf.urls import url
from . import views
urlpatterns = [
    url('register/', views.registerPage, name="register"),
	url('login/', views.loginPage, name="login"),  
	url('logout/', views.logoutUser, name="logout"),
    url('home/', views.home, name="home"),
    url('products/', views.products,name="products"),
    url('customer/', views.customer,name="customers"),
    url('createOrder/', views.createOrder,name="createOrder"),
    url('updateOrder/', views.updateOrder,name="updateOrder"),
    url('deleteOrder/', views.deleteOrder,name="deleteOrder"),
]