from django.contrib import admin
from django.urls import path, include
from config.settings import DEBUG
import main.urls
import carts.urls
import users.urls
import orders.urls
import goods.urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(main.urls, namespace="main")),
    # path("cart/", include(carts.urls), name = 'cart'),
    path("user/", include(users.urls, namespace="users")),
    # path("order/", include(orders.urls)),
    path("catalog/", include(goods.urls, namespace="goods")),
]

if DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
