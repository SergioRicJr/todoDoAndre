from datetime import datetime
from random import randrange
from typing import Any
from django.urls import reverse
from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from user.authentication import (
    authenticate,
    generateToken,
    getAuthenticatedUser,
    verifyToken,
)
from .models import UserEntity
from core.repository import Repository
from .serializers import UserSerializer
from .forms import UserForm, UserLoginForm, UserUpdateForm


class UserDeleteView(View):
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
        userRepository = Repository("user")
        user = userRepository.findOneById(self.user)
        userRepository.delete(user)
        return redirect("Login")


class UserUpdate(View):
    authenticate = False

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any):
        cookie_token = request.COOKIES.get("auth_token", "Cookie not found")
        error_code, _ = verifyToken(cookie_token)
        # print(error_code)

        if error_code == 0:
            self.user = getAuthenticatedUser(cookie_token)
            self.authenticate = True

        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        if not self.authenticate:
            return redirect("Login")
        userForm = UserUpdateForm()

        return render(request, "user_update_form.html", {"form": userForm})

    def post(self, request):
        if not self.authenticate:
            return redirect("Login")
        userForm = UserUpdateForm(request.POST)
        serializer = UserSerializer(data=userForm.data)
        serializer.is_valid(raise_exception=True)
        dados_preenchidos = {}
        for campo, valor in serializer.data.items():
            if valor is not None and valor != "":
                dados_preenchidos[campo] = valor
        repository = Repository(collection_name="user")
        repository.update(self.user, dados_preenchidos)
        return redirect("Task View")


class UserInsert(View):
    def get(self, request):
        userForm = UserForm()

        return render(request, "user_form.html", {"form": userForm})

    def post(self, request):
        userForm = UserForm(request.POST)
        if userForm.is_valid():
            serializer = UserSerializer(data=userForm.data)
            if serializer.is_valid():
                repository = Repository(collection_name="user")
                repository.insert(serializer.data)
            else:
                print(serializer.errors)
        else:
            print(userForm.errors)

        return redirect("Login")


class UserLogin(View):
    def get(self, request):
        user_login_form = UserLoginForm()
        return render(request, "login.html", {"form": user_login_form})

    def post(self, request):
        userForm = UserForm(request.POST)
        data = userForm.data
        if userForm.is_valid():
            auth = authenticate(data["username"], data["password"])
            if auth:
                token = generateToken(str(auth["_id"]), auth["username"])
                response = redirect("Task View")
                response.set_cookie("auth_token", token, max_age=3600)
            else:
                response = redirect("Login")
                print("not")
        else:
            print(userForm.errors)
        return response


class UserLogout(View):
    def get(self, request):
        response = redirect("Login")
        response.set_cookie("auth_token", "", max_age=3600)
        return response
