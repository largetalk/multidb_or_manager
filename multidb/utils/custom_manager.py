from django.db import models
from django.db.models import sql
from django.conf import settings
#from django.db.transaction import savepoint_state
from utils import thread_local_data

try:
    import thread
except ImportError:
    import dummy_thread as thread

class MultiDBManager(models.Manager):

    def get_query_set(self):
        _db = self.get_db()
        if _db:
            self._db = _db
        qs = super(MultiDBManager, self).get_query_set()
        #qs.query.connection = self.get_db_wrapper()
        return qs

    def get_db(self):
        from main.models import Project
        pcode = getattr(thread_local_data, 'project', None)
        if not pcode:
            return None
        else:
            project = Project.objects.get(project_code=pcode)
            database = {
                    'ENGINE': 'django.db.backends.mysql', 
                    'NAME': project.db_name,
                    'USER': project.db_user,
                    'PASSWORD': project.db_passwd,
                    'HOST': project.db_host,
                    'PORT': str(project.db_port),
                    }
            settings.DATABASES[pcode] = database
            print settings.DATABASES
            return pcode

    def get_db_wrapper(self):
        from main.models import Project
        pcode = getattr(thread_local_data, 'project', None)
        if not pcode:
            database = settings.DATABASES['default']
        else:
            project = Project.objects.get(project_code=pcode)
            database = {
                    'ENGINE': 'django.db.backends.mysql', 
                    'NAME': project.db_name,
                    'USER': project.db_user,
                    'PASSWORD': project.db_passwd,
                    'HOST': project.db_host,
                    'PORT': str(project.db_port),
                    }

        print '-----', database

        #backend = __import__('django.db.backends.' + database['DATABASE_ENGINE']
        #    + ".base", {}, {}, ['base'])
        backend = __import__('django.db.backends.mysql.base', {}, {}, ['base'])

        wrapper = backend.DatabaseWrapper(database)
        return wrapper

    #def _insert(self, values, return_id=False, raw_values=False):
    #    query = sql.InsertQuery(self.model, self.get_db_wrapper())
    #    query.insert_values(values, raw_values)
    #    ret = query.execute_sql(return_id)
    #    query.connection._commit()
    #    thread_ident = thread.get_ident()
    #    if thread_ident in savepoint_state:
    #        del savepoint_state[thread_ident]
    #    return ret
