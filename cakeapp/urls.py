"""cakeapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views
from django.contrib.auth import views as auth_views
from django.conf.urls import url
urlpatterns = [
    path('api/allcakes/', views.allcakes.as_view()),
    path('api/addcake/',views.addcakes.as_view()),
    path('api/cake/<int:id>',views.cakedetails.as_view()),
    path('api/register/',views.user_register),
    path('api/uploadimg/',views.Upload_image.as_view()),
    #path('api/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/',views.CustomAuthToken.as_view()),
    path('api/addcaketocart/',views.addtocart.as_view()),
    path('api/cart/',views.showcart.as_view()),
    path('api/removefromcart/',views.removefromcart.as_view()),
    url(r'^api/searchcakes/(?P<cakes>[a-zA-Z]+)$',views.searchitems.as_view()),
    path('api/placeorder/',views.placeorder.as_view()),
    path('api/myorders/',views.myorders.as_view()),
    path('api/logout/', views.Logout.as_view()),
    path('api/recoverpassword/', views.recoverpass.as_view()),
    path('api/resetpass/',views.resetPassword.as_view()),
    
    # path('login/',LoginView.as_view(template_name='login.html'),name='login'),
    # path('logout/',LogoutView.as_view(template_name='logout.html'),name='logout'),
]
