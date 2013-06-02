import random
import string

from django.http import HttpResponse
from main.models import Entry

def home(request):
    entries = Entry.objects.all()
    print '**********', entries
    project = request.session.get('project', 'None')

    return HttpResponse('blah blah ... project is %s' % project)

def random_set_project(request):
    random_project = ''.join([ random.choice(string.ascii_letters) for x in range(4) ])
    request.session['project'] = random_project
    return HttpResponse('random set project is %s ' % random_project)

