from workout.models import ExerciseModel, SplitModel, WorkoutModel


def context(request):
    ctx = {
        'exercises': ExerciseModel.objects.all(),
        'splits': SplitModel.objects.all(),
        'workouts': WorkoutModel.objects.all()
    }
    return ctx
