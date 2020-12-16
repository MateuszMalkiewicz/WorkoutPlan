from rest_framework import serializers
from workout.models import ExerciseModel, SplitModel, WorkoutModel, LoadModel


class ExerciseSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExerciseModel
        fields = '__all__'


class SplitSerializer(serializers.ModelSerializer):
    class Meta:
        model = SplitModel
        fields = '__all__'


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutModel
        fields = '__all__'


class LoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoadModel
        fields = ['weight']