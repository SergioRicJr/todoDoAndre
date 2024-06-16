from django.contrib import admin
from django.urls import path

from todo.views import TaskDeleteView, TaskInsert, TaskUpdate, TaskView
from user.views import UserDeleteView, UserInsert, UserLogin, UserUpdate

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TaskView.as_view(), name="Task View"),
    path("insert", TaskInsert.as_view(), name="Task Insert"),
    path("tasks/delete/", TaskDeleteView.as_view(), name="delete_task"),
    path("update/<pk>", TaskUpdate.as_view(), name="Task Update"),
    path("user_insert", UserInsert.as_view(), name="User Insert"),
    path("user/delete/", UserDeleteView.as_view(), name="User Delete View"),
    path("user_update/<pk>", UserUpdate.as_view(), name="User Update"),
    path("login", UserLogin.as_view(), name="Login"),
]
