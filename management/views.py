from django.shortcuts import render
from .models import Item,Supplier, Project

# Create your views here.

def welcome(request):
    # total = Item.tbs()
    return render(request, 'test.html' )


def welcome2(request,id, project):

    total = Item.get_by_project_and_id(project, id)
   

    return render(request, 'test2.html', {'total':total} )

