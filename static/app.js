$(function(){
    let addExerciseButton = $("#add-exercise-button");
    addExerciseButton.click(function () {
        location.href = "/add_exercise/";
    });

    let addSplitButton = $("#add-split-button");
    addSplitButton.click(function () {
        location.href = "/add_split/";
    });

    let addWorkoutButton = $("#add-workout-button");
    addWorkoutButton.click(function () {
        location.href = "/add_workout/";
    });

});