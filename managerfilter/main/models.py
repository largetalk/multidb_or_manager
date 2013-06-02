from django.db import models
from utils.abstract_models import FakeDeleteManager, FakeDeleteModel, ComponentManager, ComponentModel

# Create your models here.
#
class Project(FakeDeleteModel):
    name = models.CharField(max_length=100)
    objects = FakeDeleteManager()


class Entry(ComponentModel):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return '<project: %s, name: %s>' % (self.project_id, self.name)

    objects = ComponentManager()


