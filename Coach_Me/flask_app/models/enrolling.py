from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE_NAME
from datetime import datetime
from flask import flash

class Enrolling:
    def __init__(self, data_dict) :
        self.user_id = data_dict['user_id']
        self.program_id = data_dict['program_id']
        self.end_date = data_dict['end_date']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
        
    
    @classmethod
    def create_enrolling(cls,data_dict):
        query="""INSERT INTO enrollings (user_id,program_id)
                VALUES (%(user_id)s,%(program_id)s)"""
        return connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
    
    @classmethod
    def get_enrolling(cls,data_dict):
        query="""select * from enrollings where program_id=%(program_id)s;"""
        
        result = connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
        if result:
            for row in result:
                enrolling = cls(row)
                # print(enrolling)
            return enrolling
        return False
    
    @classmethod
    def update_enrolling(cls,data_dict):
        query="""update enrollings set end_date=%(end_date)s where user_id=%(user_id)s;"""
        return connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
    
    @classmethod
    def get_enrolling_with_id(cls,data_dict):
        query="""select * from enrollings where user_id=%(user_id)s;"""
        
        result = connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
        if result:
            for row in result:
                enrolling = cls(row)
                # print(enrolling)
            return enrolling
        return False
    
    @classmethod
    def delete_enrolling(cls,data_dict):
        query="""delete from enrollings where user_id=%(user_id)s and program_id=%(program_id)s"""
        return connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
        