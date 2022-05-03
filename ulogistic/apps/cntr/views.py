from django.http.response import JsonResponse
from django.shortcuts import render

from . import forms
from .models import Cntr

def containerYardStatus(request):
    if request.method == "GET":
        waiting4pickup = 99
        waiting4putdown = 99

        return render(request, 'cntr/container_yard_status.html', {
            'waiting4pickup': waiting4pickup,
            'waiting4putdown': waiting4putdown,
            'update_at': '2021-07-25 12:00',
        })

def imp(request):
    return render(request, 'cntr/import.html')

def exp(request):
    return render(request, 'cntr/export.html')

def unpack(request):
    return render(request, 'cntr/unpack.html')

def import_search_m(request):
    if request.method == 'POST':
        form = forms.CntrnoSearchForm(request.POST)
        if form.is_valid():

            qs = Cntr.objects.filter(
                cntrno__exact = form.cleaned_data['cntrno']
            )

            data = list(qs.values('vsl_seq', 'so_no', 'op_date', 'vsl_cd', 'voyage', 'stus_cd'))

            return JsonResponse({
                'status': 'ok',
                'result': data
            })

        else:
            return JsonResponse({
                'status': 'ng',
                'msg': dict(form.errors.items())
            })

    return JsonResponse({
        'status': 'ng'
    })


def export_search(request):
    pass