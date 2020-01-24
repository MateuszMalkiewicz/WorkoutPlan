from django.contrib import admin
from workout.models import ExerciseModel, SplitModel, WorkoutModel


admin.site.register(ExerciseModel)
admin.site.register(SplitModel)
admin.site.register(WorkoutModel)
