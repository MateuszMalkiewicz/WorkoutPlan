from django.db import models


REPS = {
    ('5x5', '5x5'),
    ('3x8', '3x8'),
    ('1x5', '1x5')
}


class ExerciseModel(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    reps = models.CharField(choices=REPS, max_length=4)

    def __str__(self):
        return self.name + ' ' + self.reps


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
