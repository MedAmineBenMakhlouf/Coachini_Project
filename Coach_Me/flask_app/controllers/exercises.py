from flask import  render_template, redirect, request, flash,session
from flask_app import app
from flask_app.models.exercise import Exercise
from flask_app.models.user import User
from datetime import datetime


@app.route('/exercises/<int:day_id>/new',methods=['POST'])
def create_exercise(day_id):
    id= session['program_id']
    if Exercise.validate(request.form):
        if 'file' not in request.files:
            flash('please put a picture','file')
            return redirect(f'days/{id}/plan_your_week')
        else:
            uploaded_file = request.files['file']
            pic = 'flask_app/static/img/' + uploaded_file.filename
            uploaded_file.save(pic)
        logged_user = User.get_by_id({'id': session['user_id']})
        data_dict = {
            **request.form,
            'coach_id':logged_user.id,
            'exercice_picture':pic
        }
        exrcice_id = Exercise.create_exercise(data_dict)
        data_day_exercise={
            'exercice_id':exrcice_id,
            'day_id':day_id
        }
        Exercise.create_day_exercise(data_day_exercise)
        
        return redirect(f'/days/{id}/plan_your_week')
    
    return render_template("plan_your_week.html")

@app.route('/exercises/<int:exercise_id>/update', methods=['POST'])
def update_exercise(exercise_id):
    id= session['program_id']
    if Exercise.validate(request.form):
        if 'file' not in request.files:
            flash('please put a picture','file')
            return redirect(f'days/{id}/plan_your_week#edit_delete_exercice')
        else:
            uploaded_file = request.files['file']
            pic = 'flask_app/static/img/' + uploaded_file.filename
            uploaded_file.save(pic)
            
            data_exercise={
                'exercice_id':exercise_id,
                'exercice_name':request.form["exercice_name"],
                'num_of_reps':int(request.form["num_of_reps"]),
                'num_of_series':int(request.form["num_of_series"]),
                'description':request.form["description"],
                'exercice_picture':pic
            }
            Exercise.update_exercise(data_exercise)
            return redirect(f'/days/{id}/plan_your_week')
    return redirect(f'/days/{id}/plan_your_week')

@app.route('/exercises/<int:day_id>/new_from_existing',methods=['POST'])
def add_from_existing_exercises(day_id):
    id= session['program_id']
    data_day_exercise ={
        'day_id':day_id,
        'exercice_id':request.form['exercices_list']
    }
    Exercise.create_day_exercise(data_day_exercise)
    return redirect(f'/days/{id}/plan_your_week')

@app.route('/exercises/delete',methods=['POST'])
def delete_day_exercise():
    
    id=session['program_id']
    data= {
        **request.form
    }
    # Exercise.get_exercice_to_delete(data)
    Exercise.delete_only_exercise_day(data)
    return redirect(f'/days/{id}/plan_your_week')
    