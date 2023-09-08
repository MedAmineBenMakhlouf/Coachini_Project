from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE_NAME
from datetime import datetime
from flask import flash

class Day:
    def __init__(self, data_dict) :
        self.id = data_dict['id']
        self.program_id = data_dict['program_id']
        self.body_name_day = data_dict['body_name_day']
        self.day_off = data_dict['day_off']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
        self.exercices =[]
    
    @classmethod
    def get_all_days(cls):
        query="""SELECT * from days;"""
        results = connectToMySQL(DATABASE_NAME).query_db(query)
        days = []
        for row in results:
            day = cls(row)
            days.append(day)
        return days
        
    
    @classmethod
    def get_one_day(cls,data_dict):
        query="""SELECT * from days
                    where id=%(id)s"""
        results = connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
        days = cls(results[0])
        return days
    
    @classmethod
    def get_all_prog_days(cls,data_dict):
        query="""SELECT * from days where program_id=%(id)s and day_off=0;"""
        results = connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
        days = []
        for row in results:
            day = cls(row)
            days.append(day)
        return days
    
    @classmethod
    def get_all_prog_days_for_update(cls,data_dict):
        query="""SELECT * from days where program_id=%(id)s;"""
        results = connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
        days = []
        for row in results:
            day = cls(row)
            days.append(day)
        return days
        
    
    @classmethod
    def create_program_days(cls,data_dict):
        query="""INSERT INTO days (program_id,body_name_day,day_off)
                VALUES (%(program_id)s,%(body_name_day)s,%(day_off)s)"""
        return connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
    
    @classmethod
    def update_program_days(cls,data_dict):
        query= """UPDATE days 
                    SET body_name_day=%(body_name_day)s,day_off=%(day_off)s 
                    WHERE program_id=%(program_id)s and id=%(id)s;"""
                    
        return connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
    
    @classmethod
    def get_all_days_exercices(cls,data_dict):
        query="""SELECT * from exercices
                    join exercices_has_days on exercices.id = exercices_has_days.exercice_id
                    join days on days.id = exercices_has_days.day_id
                    where days.id=%(day_id)s;"""
        results = connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
        if not results:
            return False
        day = cls(results[0])
        for row in results:
            day_exercices = {
                'id':row['exercices.id'],
                'coach_id':row['coach_id'],
                'exercice_name':row['exercice_name'],
                'num_of_series': row['num_of_series'],
                'num_of_reps':row['num_of_reps'],
                'description':row['description'],
                'exercice_picture':row['exercice_picture'],
                'created_at':row['exercices.created_at'],
                'updated_at':row['exercices.updated_at']
            }
            
            day.exercices.append(day_exercices)
        return day
    
    
    @classmethod
    def update_day_off(cls,data_dict):
        query="""update days set body_name_day='' where body_name_day=%(body_name_day)s
                    and day_off=%(day_off)s and program_id=%(program_id)s;"""
        return connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
    
    @classmethod
    def delete_program_days(cls,data_dict):
        query = """delete from days where program_id=%(program_id)s;"""
        return connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
        
        
    @classmethod
    def get_days_of_program(cls,data_dict):
        query="""SELECT * from days where program_id=%(program_id)s;"""
        results = connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
        days = []
        for row in results:
            day = cls(row)
            days.append(day)
        return days