"""GymWorkoutSet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
    ExercisesView, AddExerciseView, EditExerciseView, \
    SplitsView, AddSplitView, EditSplitView, \
    WorkoutsView, AddWorkoutView, EditWorkoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view()),
    path('exercises/', ExercisesView.as_view()),
    path('add_exercise/', AddExerciseView.as_view()),
    path('exercise/<int:exercise_id>/', EditExerciseView.as_view()),
    path('splits/', SplitsView.as_view()),
    path('add_split/', AddSplitView.as_view()),
    path('split/<int:split_id>/', EditSplitView.as_view()),
    path('workouts/', WorkoutsView.as_view()),
    path('add_workout/', AddWorkoutView.as_view()),
    path('workout/<int:workout_id>/', EditWorkoutView.as_view()),
]
