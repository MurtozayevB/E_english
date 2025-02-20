from django.views.generic import TemplateView


class AdminPanelTemplateView(TemplateView):
    template_name = 'admin/panel.html'