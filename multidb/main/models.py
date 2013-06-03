from django.db import models
from utils.custom_manager import MultiDBManager

class Project(models.Model):
    project_code = models.CharField(unique=True, max_length=20, null=False)
    db_name = models.CharField(max_length=50)
    db_user = models.CharField(max_length=50)
    db_passwd = models.CharField(max_length=50)
    db_host = models.CharField(max_length=50)
    db_port = models.IntegerField(default=3306)

    def __unicode__(self):
        return 'code: %s, name: %s, %s:%s' % (self.project_code, self.db_name, self.db_user, self.db_host)

    class Meta:
        db_table = 'project'


class Entry(models.Model):
    name = models.CharField(max_length=100)

    objects = MultiDBManager()
