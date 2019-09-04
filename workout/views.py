from django.shortcuts import render
from django.views import View
from django.http.response import HttpResponseRedirect
from workout.forms import AddExerciseForm, AddSplitForm, AddWorkoutForm


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class ExercisesView(View):
    def get(self, request):
        return render(request, 'list_exercises.html')


class SplitsView(View):
    def get(self, request):
        return render(request, 'list_splits.html')


class WorkoutsView(View):
    def get(self, request):
        return render(request, 'list_workouts.html')


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
