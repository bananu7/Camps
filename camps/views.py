from django.http import HttpResponseRedirect
from django.views import generic
from django import forms

from camps.models import Camp

class IndexView(generic.ListView):
    template_name = 'camps/index.html'
    context_object_name = 'camps'
    model = Camp

class DetailView(generic.DetailView):
    model = Camp

class CampForm(forms.ModelForm):
    class Meta:
        model = Camp
        exclude = ['date_added']

class CreateView(generic.CreateView):
    form_class = CampForm
    template_name = 'camps/camp_form.html'
    success_url = '/camps/'

