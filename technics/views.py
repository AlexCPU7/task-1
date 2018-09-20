from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Tipper, Model
from .forms import AddTipperForm, AddModelForm
from .filters import TipperFilter


class Catalog(ListView):
    model = Tipper
    context_object_name = "tippers"
    template_name = 'technics/catalog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = TipperFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self):
        try:
            if self.request.GET:
                return Tipper.objects.filter(model=self.request.GET['model'])
            else:
                return Tipper.objects.all()
        except ValueError:
            return Tipper.objects.all()


class AddModel(CreateView):
    model = Model
    form_class = AddModelForm
    template_name = "technics/add-element.html"

    def get_context_data(self, **kwargs):
        context = super(AddModel, self).get_context_data(**kwargs)
        context['title'] = 'Добавить модель'
        return context

    def form_valid(self, form):
        form.save()
        return redirect("/")

    def success_url(self):
        return redirect("/")


class AddTipper(CreateView):
    model = Tipper
    form_class = AddTipperForm
    template_name = "technics/add-element.html"

    def get_context_data(self, **kwargs):
        context = super(AddTipper, self).get_context_data(**kwargs)
        context['title'] = 'Добавить самосвал'
        return context

    def form_valid(self, form):
        form.save()
        return redirect("/")

    def success_url(self):
        return redirect("/")




