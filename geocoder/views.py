from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import logging,json
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView
import os #, asyncio
#from asgiref.sync import sync_to_async
import pandas as pd
import numpy as np

from .forms import AddressBookForm
from .models import AddressBook

from common import read_data_file as rdf
from common import make_http_requests as mhr
from common import write_output as wo

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_INPUT_PATH = BASE_DIR + r'\media\uploaded_add_books\excel\{}'
MEDIA_OUTPUT_PATH= BASE_DIR + r'\media\output_add_books\excel\{}'

@csrf_exempt
def home(request):
    form = AddressBookForm()
    address_books = AddressBook.objects.all()
    return render(request, 'home.html', {
        'form': form, 'files': address_books
    })

def generateGeocodedAddressbook(file_name):
    input_file = MEDIA_INPUT_PATH.format(file_name)
    output_file = MEDIA_OUTPUT_PATH.format(file_name)
    print(output_file)

    df = rdf.read_excel_file(input_file)
    df['latitude'] = np.nan
    df['longitude'] = np.nan

    for index, row in df.iterrows():
        _api_response = mhr.make_post_request(row['Address'])
        
        df.loc[index, 'latitude'] = _api_response['results'][0]['geometry']['location']['lat']
        df.loc[index, 'longitude'] =  _api_response['results'][0]['geometry']['location']['lng']
    wo.write_to_excel(df, output_file)

@csrf_exempt 
def upload_excel_file(request):
    address_books = AddressBook.objects.all()
    if request.method == 'POST':
        #uploaded_file = request.FILES['excelFile']
        #fs = FileSystemStorage()
        #fs.save(uploaded_file.name, uploaded_file) 
        form = AddressBookForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                if ".xlsx" not in str(form.cleaned_data['excel_file'].name):
                     raise Exception("Not right file format")
                form.save()
                latest_id = AddressBook.objects.latest('ab_id')
                obj = AddressBook.objects.get(pk=latest_id)
                #print(form.cleaned_data['excel_file'])
                _input_file_name = str(obj.excel_file).split('/')[-1]
                generateGeocodedAddressbook(_input_file_name)
            except:
                error_msg = 'Bad request! Not right file format or semantics'
                print(error_msg)
                response = HttpResponse(json.dumps({'message': error_msg}), 
                content_type='application/json')
                response.status_code = 400
                return response
    else:
        form = AddressBookForm()
    #return redirect('home')
    return render(request, 'table.html', {
        'files': address_books
    })

    