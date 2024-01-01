from . import forms
from . import models
from django.views.generic import CreateView
from django.urls import reverse_lazy


class AddMusician(CreateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = "musicians.html"
    success_url = reverse_lazy("add_musician")

    def form_valid(self, form):
        return super().form_valid(form)