# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

def displayForm(request):
    request.session['count'] = 0
    return render(request, 'survey_form/index.html')

def showResults(request):
    if request.method == 'POST':
        request.session['name'] = request.POST['name']
        request.session['dojos'] = request.POST['dojos']
        request.session['favLan'] = request.POST['favLan']
        request.session['comment'] = request.POST['comment']
        request.session['count'] += 1
    return render(request, 'survey_form/success.html')

def goBack(request):
    if request.method == 'POST':
        return redirect('/')
    return redirect('/survey_form')