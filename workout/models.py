from django.db import models
from django.contrib.auth.models import User


class ExerciseModel(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True)
    sets = models.IntegerField(null=True)
    reps = models.IntegerField(null=True)
    initial_load = models.FloatField(null=True)
    progression = models.FloatField(default=0, null=True)

    def __str__(self):
        if self.sets is not None:
            return self.name + ' ' + str(self.sets) + 'x' + str(self.reps)
        else:
            return self.name + ' 1x' + str(self.reps)


class SplitModel(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    exercises = models.ManyToManyField(ExerciseModel)

    def __str__(self):
        return self.name


class WorkoutModel(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    splits = models.ManyToManyField(SplitModel)

    def __str__(self):
        return self.name
