from django.contrib import admin
from django.urls import path

from user.views import UserDeleteView, UserInsert, UserLogin, UserUpdate

urlpatterns = [
    path("admin/", admin.site.urls),
    path("user_insert", UserInsert.as_view(), name="User Insert"),
    path("user/delete/", UserDeleteView.as_view(), name="User Delete View"),
    path("user_update/<pk>", UserUpdate.as_view(), name="User Update"),
    path("login", UserLogin.as_view(), name="Login"),
]
