from django.db import models
from django.contrib.auth.models import User


class ExerciseModel(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True)
    sets = models.IntegerField(null=True)
    reps = models.IntegerField(null=True)
    user = models.ForeignKey(User, null=True, default=None, on_delete=models.DO_NOTHING)

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


class LoadModel(models.Model):
    weight = models.FloatField()
    exercise = models.ForeignKey(ExerciseModel, on_delete=models.DO_NOTHING)
    split = models.ForeignKey(SplitModel, on_delete=models.DO_NOTHING)
    workout = models.ForeignKey(WorkoutModel, on_delete=models.DO_NOTHING)

