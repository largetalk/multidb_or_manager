from utils import thread_local_data

class SetProjectMiddleware(object):

    def process_request(self, request):
        if 'project' in request.session:
            thread_local_data.project = request.session['project']
        pass
