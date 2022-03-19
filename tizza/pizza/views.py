from django.shortcuts import render
from django.http import HttpResponse

import random 
from .models import Pizza 


def index(request, pid):

    pid = random.randrange(100)
    pizza=Pizza.objects.get(id=pid)
    print(id)
    if Pizza.objects.get(id=pid).DoesNotExist:
        return HttpResponse("No pizaa today baby")
    else:
        return HttpResponse(content={
            'id':pizza.id, 
            'title':pizza.title, 
            'description': pizza.description
            }
        )



