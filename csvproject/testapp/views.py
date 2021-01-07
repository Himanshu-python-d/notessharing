from django.shortcuts import render
import csv
from io import StringIO
from django.contrib import messages
from .models import Contact,Contact1
# Create your views here.

def contact_upload(request):
    template = "contact_upload.html"

    if request.method == "GET":
        return render(request , template)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string,delimiter=',' , quotechar="|"):
        _, created = Contact.objects.update_or_create(
        name=column[0],
        email=column[1],
        message=column[2]
        )
        _, created1 = Contact1.objects.update_or_create(
        name=column[0],
        email=column[1],
        message=column[2]
        )
    context = {}
    return render(request, template, context)
