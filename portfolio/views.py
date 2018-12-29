from django.http import HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect

from django.views.generic import View
import os 


class ReactAppView(View):

    def get(self, request):
        try:

            with open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'frontend', 'build', 'index.html')) as file:
                return HttpResponse(file.read())

        except :
            return HttpResponse(
                """
                index.html not found ! build your React app !!
                """,
                status=501,
            )
