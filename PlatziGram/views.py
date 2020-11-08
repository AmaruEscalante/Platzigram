from django.http import HttpResponse
from datetime import datetime
import json


def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse("Current Server time is {}".format(now))


def sort_integers(request):
    #print(request)
    numbers = [int(i) for i in request.GET['numbers'].split(',')]

    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted succesfully.'
    }

    #import pdb; pdb.set_trace()
    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')


def say_hi(request, name, age):
    if age < 12:
        message = 'sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello, {}! Welcome to Platzigram'.format(name)

    return HttpResponse(message)
