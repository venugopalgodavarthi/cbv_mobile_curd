from dataclasses import field
from django.shortcuts import render
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from oneplus.models import oneplusmodel
# Create your views here.


class mcreate(CreateView):
    template_name='mcreate.html'
    model=oneplusmodel
    fields='__all__'
    context_object_name='form'
    success_url='/o/mselect/'

class mselect(ListView):
    template_name='mselect.html'
    model=oneplusmodel
    fields='__all__'
    context_object_name='res'

class mdetail(DetailView):
    template_name='mdetails.html'
    model=oneplusmodel
    fields='__all__'
    context_object_name='i'

class mupdate(UpdateView):
    template_name='mcreate.html'
    model=oneplusmodel
    fields='__all__'
    context_object_name='form'
    success_url='/o/mselect/'

class mdelete(DeleteView):
    template_name='mdeleteconfirm.html'
    model=oneplusmodel
    fields='__all__'
    context_object_name='i'
    success_url='/o/mselect/'
