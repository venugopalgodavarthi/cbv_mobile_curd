from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView,FormView,CreateView,ListView,DetailView,UpdateView,DeleteView
from cbv.models import gomodel
from cbv.forms import goform
# Create your views here.
def sample(request,pk):
    res=gomodel.objects.get(id=pk)
    if request.method=='POST':
        res=gomodel.objects.get(id=pk).delete()
        return HttpResponse("data is deleted")
    return render(request,"deleteconfirm.html",{'res':res})

class csample(View):
    def get(self,request,pk):
        res=gomodel.objects.get(id=pk)
        return render(request,"deleteconfirm.html",{'res':res})

    def post(self,request,pk):
        res=gomodel.objects.get(id=pk).delete()
        return HttpResponse("data is deleted")

class psample(DeleteView):
    model=gomodel
    fields='__all__'
    template_name='deleteconfirm.html'
    context_object_name='res'
    success_url='/c/psample/1'

'''
def sample(request):
    return HttpResponse("helloworld")

class csample(View):'
    def get(self,request):
        return HttpResponse('helloworld')


def sample(request):
    form=goform()
    if request.method=='POST':
        form=goform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("data is created")
    return render(request,"sample.html",{'form':form})

class csample(View):
    def get(self,request):
        form=goform()
        return render(request,"sample.html",{'form':form})

    def post(self,request):
        form=goform(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse("data is created")



class psample(FormView):
    template_name='sample.html'
    form_class=goform
    def form_valid(self, form):
        data=form.cleaned_data
        return HttpResponse(str(data))

class psample(CreateView):
    model=gomodel
    fields='__all__'
    template_name='sample.html'
    success_url='/c/csample/'



def sample(request):
    res=gomodel.objects.all()
    return render(request,"select.html",{'res':res})

class csample(View):
    def get(self,request):
        res=gomodel.objects.all()
        return render(request,"select.html",{'res':res})

class psample(ListView):
    model=gomodel
    fields='__all__'
    template_name='select.html'
    context_object_name='res'


def sample(request,pk):
    res=gomodel.objects.get(id=pk)
    return render(request,"details.html",{'res':res})

class csample(View):
    def get(self,request,pk):
        res=gomodel.objects.get(id=pk)
        return render(request,"details.html",{'res':res})

class psample(DetailView):
    model=gomodel
    fields='__all__'
    template_name='details.html'
    context_object_name='res'


def sample(request,pk):
    res=gomodel.objects.get(id=pk)
    form=goform(instance=res)
    if request.method=='POST':
        form=goform(request.POST,instance=res)
        if form.is_valid():
            form.save()
            return HttpResponse("data is updated")
    return render(request,"sample.html",{'form':form})

class csample(View):
    def get(self,request,pk):
        res=gomodel.objects.get(id=pk)
        form=goform(instance=res)
        return render(request,"sample.html",{'form':form})

    def post(self,request,pk):
        res=gomodel.objects.get(id=pk)
        form=goform(request.POST,instance=res)
        if form.is_valid():
            form.save()
        return HttpResponse("data is updated")


class psample(UpdateView):
    model=gomodel
    fields='__all__'
    template_name='sample.html'
    success_url='/c/psample/1'

'''


