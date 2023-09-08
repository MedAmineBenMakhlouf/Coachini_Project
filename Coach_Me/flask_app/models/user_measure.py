from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE_NAME
from datetime import datetime
from flask import flash

class User_measure:
    def __init__(self, data_dict) :
        self.user_id = data_dict['user_id']
        self.bmi_id = data_dict['bmi_id']
        self.height = data_dict['height']
        self.weight = data_dict['weight']
        self.bmi = data_dict['bmi']
        
    @classmethod
    def create_user_measure(cls,data_dict):
        query = """INSERT INTO user_measures (user_id, bmi_id, height, weight,bmi)
                    VALUES (%(user_id)s,%(bmi_id)s,%(height)s,%(weight)s,%(bmi)s);"""
        return connectToMySQL(DATABASE_NAME).query_db(query, data_dict)
    
    @classmethod
    def get_bmi(cls,data_dict):
        query="""select * from user_measures where user_id=%(user_id)s"""
        result= connectToMySQL(DATABASE_NAME).query_db(query, data_dict)
        user_measure = cls(result[0])
        return user_measure