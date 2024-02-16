from django.urls import path, include
from goods import views
app_name = 'goods'
urlpatterns = [
    path("", views.goods, name= 'main_goods'),
]