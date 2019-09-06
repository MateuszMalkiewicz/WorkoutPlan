from django import forms
from workout.models import ExerciseModel, SplitModel, WorkoutModel


class AddExerciseForm(forms.ModelForm):
    class Meta:
        model = ExerciseModel
        fields = '__all__'


class AddSplitForm(forms.ModelForm):
    exercises = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                               queryset=ExerciseModel.objects.all(),
                                               required=False)

    class Meta:
        model = SplitModel
        fields = '__all__'


class AddWorkoutForm(forms.ModelForm):
    splits = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                            queryset=SplitModel.objects.all(),
                                            required=False)

    class Meta:
        model = WorkoutModel
        fields = '__all__'


