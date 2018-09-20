import django_filters
from .models import Tipper


class TipperFilter(django_filters.FilterSet):

    def __init__(self, *args, **kwargs):
        super(TipperFilter, self).__init__(*args, **kwargs)
        self.form.fields['model'].empty_label = 'Все'

    class Meta:
        model = Tipper
        fields = ['model']




