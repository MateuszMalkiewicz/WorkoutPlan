from django.forms import ModelForm
from workout.models import ExerciseModel, SplitModel, WorkoutModel


class AddExerciseForm(ModelForm):
    class Meta:
        model = ExerciseModel
        fields = '__all__'


class AddSplitForm(ModelForm):
    class Meta:
        model = SplitModel
        fields = '__all__'


class AddWorkoutForm(ModelForm):
    class Meta:
        model = WorkoutModel
        fields = '__all__'
