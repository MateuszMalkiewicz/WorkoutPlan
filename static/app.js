$(function(){
    let newExerciseButton = $("#new-exercise-button");
    newExerciseButton.click(function () {
        location.href = "/add_exercise/";
    });

    let newSplitButton = $("#new-split-button");
    newSplitButton.click(function () {
        location.href = "/add_split/";
    });

    let newWorkoutButton = $("#new-workout-button");
    newWorkoutButton.click(function () {
        location.href = "/add_workout/";
    });

});