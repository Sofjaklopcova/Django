from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView


from .models import Trener, Tym, Soutez, Hrac


def index(request):

 num_Tym = Tym.objects.all()
 num_Souteze = Soutez.objects.all()

 context = {
 'num_tym': num_Tym,
 'num_soutez': num_Souteze
 }

 return render(request, 'index.html', context=context)


class TreneriListView(ListView):
 model = Trener
 context_object_name = 'treneri'
 template_name = 'trener/treneri_list.html'


class TrenerDetailView(DetailView):
 model = Trener
 context_object_name = 'trener'
 template_name = 'trener/trener_detail.html'



class HraciListView(ListView):
  model = Hrac
  context_object_name = 'hraci'
  template_name = 'hrac/hraci_list.html'

class HracDetailView(DetailView):
  model = Hrac
  context_object_name = 'hrac'
  template_name = 'hrac/hrac_detail.html'