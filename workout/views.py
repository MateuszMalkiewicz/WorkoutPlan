from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http.response import HttpResponseRedirect
from workout.forms import AddExerciseForm, AddSplitForm, AddWorkoutForm
from workout.models import ExerciseModel, SplitModel, WorkoutModel


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class ExercisesView(View):
    def get(self, request):
        return render(request, 'list_exercises.html', {'exercises': ExerciseModel.objects.all()})


class SplitsView(View):
    def get(self, request):
        return render(request, 'list_splits.html', {'splits': SplitModel.objects.all()})


class WorkoutsView(View):
    def get(self, request):
        return render(request, 'list_workouts.html', {'workouts': WorkoutModel.objects.all()})


class AddExerciseView(View):
    def get(self, request):
        form = AddExerciseForm()
        return render(request, 'add_exercise.html', {'form': form})

    def post(self, request):
        form = AddExerciseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/exercises')
        else:
            form = AddExerciseForm()
            return render(request, 'add_exercise.html', {'form': form})


class EditExerciseView(View):
    def get(self, request, exercise_id):
        exercise = ExerciseModel.objects.get(id=exercise_id)
        form = AddExerciseForm(instance=exercise)
        return render(request, 'edit_exercise.html', {'form': form})

    def post(self, request, exercise_id):
        exercise = get_object_or_404(ExerciseModel, id=exercise_id)
        form = AddExerciseForm(request.POST or None, instance=exercise)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/exercises')
        else:
            form = AddExerciseForm(instance=exercise)
            return render(request, 'edit_exercise.html', {'form': form})


class AddSplitView(View):
    def get(self, request):
        form = AddSplitForm()
        return render(request, 'add_split.html', {'form': form})

    def post(self, request):
        form = AddSplitForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/splits')
        else:
            form = AddSplitForm()
            return render(request, 'add_split.html', {'form': form})


class EditSplitView(View):
    def get(self, request, split_id):
        split = SplitModel.objects.get(id=split_id)
        form = AddSplitForm(instance=split)
        return render(request, 'edit_split.html', {'form': form})

    def post(self, request, split_id):
        split = get_object_or_404(SplitModel, id=split_id)
        form = AddSplitForm(request.POST or None, instance=split)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/splits')
        else:
            form = AddSplitForm(instance=split)
            return render(request, 'edit_split.html', {'form': form})


class AddWorkoutView(View):
    def get(self, request):
        form = AddWorkoutForm()
        return render(request, 'add_workout.html', {'form': form})

    def post(self, request):
        form = AddWorkoutForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/workouts')
        else:
            form = AddWorkoutForm()
            return render(request, 'add_workout.html', {'form': form})


class EditWorkoutView(View):
    def get(self, request, workout_id):
        workout = WorkoutModel.objects.get(id=workout_id)
        form = AddWorkoutForm(instance=workout)
        return render(request, 'edit_workout.html', {'form': form})

    def post(self, request, workout_id):
        workout = get_object_or_404(SplitModel, id=workout_id)
        form = AddWorkoutForm(request.POST or None, instance=workout)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/workouts')
        else:
            form = AddWorkoutForm(instance=workout)
            return render(request, 'edit_workout.html', {'form': form})
