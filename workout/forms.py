from django import forms
from workout.models import ExerciseModel, SplitModel, WorkoutModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AddExerciseForm(forms.ModelForm):
    class Meta:
        model = ExerciseModel
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(AddExerciseForm, self).__init__(*args, **kwargs)
        self.fields['description'].required = False
        self.fields['progression'].required = False


class AddSplitForm(forms.ModelForm):
    exercises = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                               queryset=ExerciseModel.objects.all(),
                                               required=False)

    class Meta:
        model = SplitModel
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(AddSplitForm, self).__init__(*args, **kwargs)
        self.fields['description'].required = False


class AddWorkoutForm(forms.ModelForm):
    splits = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                            queryset=SplitModel.objects.all(),
                                            required=False)

    class Meta:
        model = WorkoutModel
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(AddWorkoutForm, self).__init__(*args, **kwargs)
        self.fields['description'].required = False


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=150, required=True,
                             help_text='Required. 150 characters or fewer. Enter a valid email address.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')

    class Meta:
        fields = '__all__'