
from django.shortcuts import render
from rest_framework import viewsets

from browsersPc.models import PC, Browsers
from browsersPc.serializers import PCSerializer, BrowsersSerializer


class PCViewSet(viewsets.ModelViewSet):
    queryset = PC.objects.all()
    serializer_class = PCSerializer


class BrowsersViewSet(viewsets.ModelViewSet):
    queryset = Browsers.objects.all()
    serializer_class = BrowsersSerializer


def report(request):
    print(PC.objects.select_related('browser_id')[0].memory)
    return render(request, 'report.html', {'data': {
        'pc': PC.objects.select_related('browser_id')
    }})
