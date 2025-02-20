from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from admin2.forms import VocabForm
from apps.models import Vocab
import pandas as pd


class VocabTemplateView(TemplateView):
    template_name = "admin/vocab-list.html"

class VocabCreateView(CreateView):
    queryset = Vocab.objects.all()
    form_class = VocabForm
    template_name = 'admin/vocab-list.html'
    success_url = reverse_lazy("admin-vocab-list")

    def form_valid(self, form):
        excel_file = form.cleaned_data.get('excel_file')
        unit = form.cleaned_data.get('unit')
        try:
            data = pd.read_excel(excel_file)
            if 'eng' not in data.columns or 'uz' not in data.columns:
                return JsonResponse({'error': "The file must contain 'eng' and 'uz' columns."}, status=400)
            words = []
            for index, row in data.iterrows():
                english_word = row['eng']
                uzbek_word = row['uz']
                if pd.isna(english_word) or pd.isna(uzbek_word):
                    continue
                words.append({
                    'english': english_word.strip(),
                    'uzbek': uzbek_word.strip(),
                    'unit': unit
                })
            print(f"Extracted Words: {words}")
            return JsonResponse({'success': True, 'words': words})
        except Exception as e:
            return JsonResponse({'error': str(e)})