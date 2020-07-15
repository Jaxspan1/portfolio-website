from django.shortcuts import render
from django.views.generic import View


class HomeView(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'index.html')


home_view = HomeView.as_view()


def terms(request):
    return render(request, 'pages/terms-conditions.html')


def privacy(request):
    return render(request, 'pages/privacy-policy.html')
