from django.db import models
from utils import thread_local_data

class ProjectManager(models.Manager):
    def get_query_set(self):
        project = getattr(thread_local_data, 'project', None)
        if project:
            return super(ProjectManager, self).get_query_set().filter(project_id=project)
        else:
            return super(ProjectManager, self).get_query_set()


class BaseProjectModel(models.Model):
    project_id = models.CharField(max_length=100)

    objects = ProjectManager()

    class Meta:
        abstract = True


class FakeDeleteManager(models.Manager):
    def get_query_set(self):
        return super(FakeDeleteManager, self).get_query_set().filter(is_delete=False)


class FakeDeleteModel(models.Model):
    is_delete = models.BooleanField(default=False)

    objects = FakeDeleteManager()

    class Meta:
        abstract = True


    def delete(self):
        self.is_delete = True
        self.save()


class ComponentManager(ProjectManager, FakeDeleteManager):
    pass

class ComponentModel(BaseProjectModel, FakeDeleteModel):
    objects = ComponentManager()

    class Meta:
        abstract = True



         
