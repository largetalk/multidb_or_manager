# Create your views here.
#
from django.http import HttpResponse
from main.models import Project, Entry


def home(request):
    projects = Project.objects.all()
    print '#####', projects
    return HttpResponse('abcd')

def home2(request):
    entries = Entry.objects.all()
    print '####', entries
    return HttpResponse('asdfg')


def pset(request):
    code = request.GET.get('project', None)
    if code:
        request.session['project'] = code
        return HttpResponse('set project code ' + code)
    return HttpResponse('error')
