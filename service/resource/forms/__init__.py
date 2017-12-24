from django.forms import ModelForm
from suit.widgets import SuitSplitDateTimeWidget

from service.resource.models import Article, Album


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        widgets = {
            'status_changed': SuitSplitDateTimeWidget,
            'modified': SuitSplitDateTimeWidget,
        }
        # fields = '__all__'
        exclude = ('status_changed', 'favorite', 'favCount')


class AlbumForm(ModelForm):
    class Meta:
        model = Album
        widgets = {
            'status_changed': SuitSplitDateTimeWidget,
            'modified': SuitSplitDateTimeWidget,
        }
        # fields = '__all__'
        exclude = ('status_changed', 'favorite')
