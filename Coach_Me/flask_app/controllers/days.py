from flask import  render_template, redirect, request, flash,session
from flask_app import app
from flask_app.models.day import Day
from flask_app.models.user import User
from flask_app.models.exercise import Exercise
from datetime import datetime


@app.route('/days/<int:program_id>/plan_your_week')
def plan_week(program_id):
    logged_user = User.get_by_id({'id': session['user_id']})
    exercices_by_coach = Exercise.get_exercises_by_coach({'id':logged_user.id})
    if exercices_by_coach:
        all_exercises = exercices_by_coach
    else:
        all_exercises = ""
    all_days = Day.get_all_prog_days({'id':program_id})
    for day in all_days:
        exercices = Exercise.get_all_days_exercices({'day_id':day.id})
        if exercices!=False:
            for exercice in exercices:
                day.exercices.append(exercice)
    return render_template('plan_your_week.html',coach_exercices=all_exercises, days=all_days, user_first_name=session['user_first_name'])