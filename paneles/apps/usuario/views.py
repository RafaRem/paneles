import json

from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q,Count
from django.views.generic.edit import FormView
from django.views.generic import View
from django.contrib.auth import login, logout
from .form import FormularioLogin


import datetime
from datetime import date
# Create your views here.
class Login(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('inicio')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)

    def dispatch(self,request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        print(self.request,form.get_user())
        login(self.request,form.get_user())
        return super(Login,self).form_valid(form)


def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('accounts/login')