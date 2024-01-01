from . import forms
from . import models
from django.views.generic import CreateView
from django.urls import reverse_lazy


class AddAlbum(CreateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = "album.html"
    success_url = reverse_lazy("add_album")

    def form_valid(self, form):
        form.instance.release = self.request.user
        return super().form_valid(form)