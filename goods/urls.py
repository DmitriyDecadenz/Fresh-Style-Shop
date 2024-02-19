from django.urls import path, include
from goods import views

app_name = "goods"
urlpatterns = [
    path("", views.category, name="category"),
]
