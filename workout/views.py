from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from workout.forms import AddExerciseForm, AddSplitForm, AddWorkoutForm, RegisterForm, LoginForm
from workout.models import ExerciseModel, SplitModel, WorkoutModel
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class ExercisesView(View):
    def get(self, request):
        exercises = ExerciseModel.objects.all().order_by('id')
        return render(request, 'list_exercises.html', {'exercises': exercises})


class SplitsView(View):
    def get(self, request):
        splits = SplitModel.objects.all()
        return render(request, 'list_splits.html', {'splits': splits})


class WorkoutsView(View):
    def get(self, request):
        workouts = WorkoutModel.objects.all()
        return render(request, 'list_workouts.html', {'workouts': workouts})


class AddExerciseView(View):
    def get(self, request):
        form = AddExerciseForm()
        return render(request, 'add_exercise.html', {'form': form})

    def post(self, request):
        form = AddExerciseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/exercises')
        else:
            form = AddExerciseForm()
            return render(request, 'add_exercise.html', {'form': form})


class EditExerciseView(View):
    def get(self, request, exercise_id):
        exercise = get_object_or_404(ExerciseModel, id=exercise_id)
        form = AddExerciseForm(instance=exercise)
        return render(request, 'edit_exercise.html', {'form': form})

    def post(self, request, exercise_id):
        exercise = get_object_or_404(ExerciseModel, id=exercise_id)
        form = AddExerciseForm(request.POST or None, instance=exercise)
        if form.is_valid():
            form.save()
            return redirect('/exercises')
        else:
            form = AddExerciseForm(instance=exercise)
            return render(request, 'edit_exercise.html', {'form': form})


class DeleteExerciseView(View):
    def get(self, request, exercise_id):
        exercise = get_object_or_404(ExerciseModel, id=exercise_id)
        context = {'type': 'exercise', 'object': exercise}
        return render(request, 'delete.html', context)

    def post(self, request, exercise_id):
        exercise = get_object_or_404(ExerciseModel, id=exercise_id)
        exercise.delete()
        return redirect('/exercises')


class AddSplitView(View):
    def get(self, request):
        form = AddSplitForm()
        return render(request, 'add_split.html', {'form': form})

    def post(self, request):
        form = AddSplitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/splits')
        else:
            form = AddSplitForm()
            return render(request, 'add_split.html', {'form': form})


class EditSplitView(View):
    def get(self, request, split_id):
        split = get_object_or_404(SplitModel, id=split_id)
        form = AddSplitForm(instance=split)
        return render(request, 'edit_split.html', {'form': form})

    def post(self, request, split_id):
        split = get_object_or_404(SplitModel, id=split_id)
        form = AddSplitForm(request.POST or None, instance=split)
        if form.is_valid():
            form.save()
            return redirect('/splits')
        else:
            form = AddSplitForm(instance=split)
            return render(request, 'edit_split.html', {'form': form})


class DeleteSplitView(View):
    def get(self, request, split_id):
        split = get_object_or_404(SplitModel, id=split_id)
        context = {'type': 'split', 'object': split}
        return render(request, 'delete.html', context)

    def post(self, request, split_id):
        split = get_object_or_404(SplitModel, id=split_id)
        split.delete()
        return redirect('/splits')


class StartSplitView(View):
    def get(self, request, workout_id, split_id):
        workout = get_object_or_404(WorkoutModel, id=workout_id)
        split = get_object_or_404(SplitModel, id=split_id)
        user = request.user

        context = {'workout': workout, 'split': split, 'user': user}

        return render(request, 'start_split.html', context)

    def post(self, request, workout_id, split_id):
        pass


class AddWorkoutView(View):
    def get(self, request):
        form = AddWorkoutForm()
        return render(request, 'add_workout.html', {'form': form})

    def post(self, request):
        form = AddWorkoutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/workouts')
        else:
            form = AddWorkoutForm()
            return render(request, 'add_workout.html', {'form': form})


class EditWorkoutView(View):
    def get(self, request, workout_id):
        workout = get_object_or_404(WorkoutModel, id=workout_id)
        form = AddWorkoutForm(instance=workout)
        return render(request, 'edit_workout.html', {'form': form})

    def post(self, request, workout_id):
        workout = get_object_or_404(WorkoutModel, id=workout_id)
        form = AddWorkoutForm(request.POST or None, instance=workout)
        if form.is_valid():
            form.save()
            return redirect('/workouts')
        else:
            form = AddWorkoutForm(instance=workout)
            return render(request, 'edit_workout.html', {'form': form})


class DeleteWorkoutView(View):
    def get(self, request, workout_id):
        workout = get_object_or_404(WorkoutModel, id=workout_id)
        context = {'type': 'workout', 'object': workout}
        return render(request, 'delete.html', context)

    def post(self, request, workout_id):
        workout = get_object_or_404(WorkoutModel, id=workout_id)
        workout.delete()
        return redirect('/workouts')


class StartWorkoutView(View):
    def get(self, request, workout_id):
        workout = get_object_or_404(WorkoutModel, id=workout_id)
        return render(request, 'start_workout.html', {'workout': workout})


class RegisterView(View):
    form = RegisterForm

    def validate_passwords(self, password_one, password_two):
        if len(password_one) < 8:
            return False
        return True if password_one == password_two else False

    def get(self, request):
        return render(request, 'user_registration.html', {'form': self.form})

    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password_one = request.POST['password1']
        password_two = request.POST['password2']

        if self.validate_passwords(password_one, password_two):
            User.objects.create_user(username=username, email=email, password=password_one)
            return render(request, 'user_registration_success.html')

        return render(request, 'user_registration.html', {'invalid_password': True, 'form': self.form})


class LoginView(View):
    form = LoginForm

    def get(self, request):
        return render(request, 'user_login.html', {'form': self.form})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'user_login.html', {'form': self.form, 'invalid_login_or_password': True})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')
