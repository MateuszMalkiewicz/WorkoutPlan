"""WorkoutPlanner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from workout.views import IndexView, \
    ExercisesView, AddExerciseView, EditExerciseView, DeleteExerciseView,\
    SplitsView, AddSplitView, EditSplitView, DeleteSplitView, StartSplitView, \
    WorkoutsView, AddWorkoutView, EditWorkoutView, DeleteWorkoutView, StartWorkoutView, \
    RegisterView, LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('exercises/', ExercisesView.as_view(), name='exercises'),
    path('add_exercise/', AddExerciseView.as_view(), name='add_exercise'),
    path('exercise/<int:exercise_id>/', EditExerciseView.as_view(), name='edit_exercise'),
    path('exercise/<int:exercise_id>/delete', DeleteExerciseView.as_view(), name='delete_exercise'),
    path('splits/', SplitsView.as_view(), name='splits'),
    path('add_split/', AddSplitView.as_view(), name='add_split'),
    path('split/<int:split_id>/', EditSplitView.as_view(), name='edit_split'),
    path('split/<int:split_id>/delete', DeleteSplitView.as_view(), name='delete_split'),
    path('workouts/', WorkoutsView.as_view(), name='workouts'),
    path('add_workout/', AddWorkoutView.as_view(), name='add_workout'),
    path('workout/<int:workout_id>/', EditWorkoutView.as_view(), name='edit_workout'),
    path('workout/<int:workout_id>/delete', DeleteWorkoutView.as_view(), name='delete_workout'),
    path('workout/<int:workout_id>/start', StartWorkoutView.as_view(), name='start_workout'),
    path('workout/<int:workout_id>/start/<int:split_id>', StartSplitView.as_view(), name='start_split'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
