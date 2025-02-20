from django.db.models import FileField, IntegerField
from django.forms import ModelForm

from apps.models import Book, Unit, Vocab


class BookModelForm(ModelForm):

    class Meta:
        model = Book
        fields = 'name', 'level', 'image'


class UnitModelForm(ModelForm):
    class Meta:
        model = Unit
        fields = 'unit_num', 'book'

class VocabForm(ModelForm):
    excel_file = FileField()
    unit = IntegerField()

class VocabCreateModelForm(ModelForm):
    excel_file = FileField()
    class Meta:
        model = Vocab
        fields = "__all__"

