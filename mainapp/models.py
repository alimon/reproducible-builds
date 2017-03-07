from django.db import models

class Build(models.Model):
    build_id = models.CharField(max_length=64, primary_key=True)
    build_date = models.DateTimeField()
    target_machine = models.CharField(max_length=64)

class BuildDetails(models.Model):
    build = models.ForeignKey(Build, on_delete=models.CASCADE)
    repository = models.CharField(max_length=128)
    revision = models.CharField(max_length=64)

class ArtifactType(object):
    TARGET = 'target'
    NATIVE = 'native'

class Sstate(models.Model):
    ARTIFACT_TYPE_CHOICES = (
            (ArtifactType.TARGET, 'Target artifact'),
            (ArtifactType.NATIVE, 'Native artifact')
    )

    build = models.ForeignKey(Build, on_delete=models.CASCADE)
    artifact_type = models.CharField(max_length=16,
            choices=ARTIFACT_TYPE_CHOICES)
    rb_status = models.CharField(max_length=1)

class SstateTask(models.Model):
    sstate = models.ForeignKey(Sstate, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=128)
    diff = models.BinaryField()
