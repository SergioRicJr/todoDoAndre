from datetime import datetime
from random import randrange
from typing import Any
from django.http import HttpRequest
from django.urls import reverse
from django.views import View
from django.shortcuts import render, redirect
from user.authentication import getAuthenticatedUser, verifyToken
from .models import TaskEntity
from core.repository import Repository
from .serializers import TaskSerializer, TaskUpdateSerializer
from .forms import TaskForm, TaskUpdateForm


class TaskView(View):
    authenticate = False

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any):
        cookie_token = request.COOKIES.get("auth_token", "Cookie not found")
        error_code, _ = verifyToken(cookie_token)
        print(error_code)

        if error_code == 0:
            self.user = getAuthenticatedUser(cookie_token)
            self.authenticate = True

        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        if not self.authenticate:
            return redirect("Login")
        repository = Repository(collection_name="tasks")
        tasks = list(repository.getByAttribute("user_id", self.user))
        serializer = TaskSerializer(data=tasks, many=True)
        if serializer.is_valid():
            modelTask = serializer.save()
            tasks = [
                {**obj, "id": obj.pop("_id")} if "_id" in obj else obj for obj in tasks
            ]
        else:
            print(serializer.errors)
        return render(
            request, "home.html", {"tasks": tasks, "authenticate": self.authenticate}
        )


class TaskDeleteView(View):
    authenticate = False

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any):
        cookie_token = request.COOKIES.get("auth_token", "Cookie not found")
        error_code, _ = verifyToken(cookie_token)
        print(error_code)

        if error_code == 0:
            user = getAuthenticatedUser(cookie_token)
            self.authenticate = True

        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        if not self.authenticate:
            return redirect("Login")
        additional_value = request.POST.get("additional_field")
        taskRepository = Repository("tasks")
        task = taskRepository.findOneById(additional_value)
        taskRepository.delete(task)
        return redirect("Task View")


class TaskUpdate(View):
    authenticate = False

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any):
        cookie_token = request.COOKIES.get("auth_token", "Cookie not found")
        error_code, _ = verifyToken(cookie_token)
        print(error_code)

        if error_code == 0:
            user = getAuthenticatedUser(cookie_token)
            self.authenticate = True

        return super().dispatch(request, *args, **kwargs)

    def get(self, request, pk):
        if not self.authenticate:
            return redirect("Login")
        taskForm = TaskUpdateForm()

        return render(
            request, "update_form.html", {"form": taskForm, "primary_key": pk}
        )

    def post(self, request, pk):
        if not self.authenticate:
            return redirect("Login")
        taskForm = TaskUpdateForm(request.POST)
        serializer = TaskUpdateSerializer(data=taskForm.data)
        serializer.is_valid(raise_exception=True)
        dados_preenchidos = {}
        for campo, valor in serializer.data.items():
            if valor is not None and valor != "":
                dados_preenchidos[campo] = valor
        repository = Repository(collection_name="tasks")
        repository.update(pk, dados_preenchidos)
        return redirect("Task View")


class TaskInsert(View):
    authenticate = False

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any):
        cookie_token = request.COOKIES.get("auth_token", "Cookie not found")
        error_code, _ = verifyToken(cookie_token)

        if error_code == 0:
            self.user = getAuthenticatedUser(cookie_token)
            self.authenticate = True

        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        if not self.authenticate:
            return redirect("Login")
        taskForm = TaskForm()

        return render(request, "form.html", {"form": taskForm})

    def post(self, request):
        if not self.authenticate:
            return redirect("Login")
        taskForm = TaskForm(request.POST)
        if taskForm.is_valid():
            novo_dicionario = {
                chave: valor[0] for chave, valor in dict(taskForm.data).items()
            }
            novo_dicionario.update({"user_id": self.user})
            print(novo_dicionario)
            serializer = TaskSerializer(data=novo_dicionario)
            if serializer.is_valid():
                repository = Repository(collection_name="tasks")
                repository.insert(serializer.data)
            else:
                print(serializer.errors)
        else:
            print(taskForm.errors)

        return redirect("Task View")
