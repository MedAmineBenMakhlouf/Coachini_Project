from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE_NAME
from datetime import datetime
from flask import flash

class Bmi:
    def __init__(self, data_dict) :
        self.id = data_dict['id']
        self.min_range = data_dict['min_range']
        self.max_range = data_dict['max_range']
        self.category_name = data_dict['category_name']
    
    @classmethod
    def get_all_bmis(cls):
        query="""SELECT * from bmis;"""
        results = connectToMySQL(DATABASE_NAME).query_db(query)
        bmis = []
        for row in results:
            bmi = cls(row)
            bmis.append(bmi)
        return bmis
        
    @classmethod
    def get_bmis_not_in_program(cls,data_dict):
        query="""select * from bmis 
                where bmis.id not in 
                (select bmi_id from programs where bmis.id = programs.bmi_id and programs.id=%(id)s);"""
        results = connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
        bmis = []
        for row in results:
            bmi = cls(row)
            bmis.append(bmi)
        return bmis
    @classmethod
    def get_one_bmi(cls,data_dict):
        query="""SELECT * from bmis
                    where id=%(id)s"""
        results = connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
        bmis = cls(results[0])
        return bmis