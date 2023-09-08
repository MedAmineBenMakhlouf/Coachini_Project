from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE_NAME
from flask_app.models.program import Program
from flask import flash
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
# MEASURES_REGEX = re.compile(r'^\d+$')
class User:
    def __init__(self, data_dict) :
        self.id = data_dict['id']
        self.first_name = data_dict['first_name']
        self.last_name = data_dict['last_name']
        self.email = data_dict['email']
        self.password = data_dict['password']
        self.role = data_dict['role']
        self.is_valid = data_dict['is_valid']
        self.is_banned = data_dict['is_banned']        
        self.is_blocked = data_dict['is_blocked']
        self.picture = data_dict['picture']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']

    @classmethod
    def create_user(cls, data_dict):
        query = """INSERT INTO users (first_name, last_name, email, password,role,is_valid,picture,is_blocked,is_banned)
                    VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s,%(role)s,%(is_valid)s,%(picture)s,0,0);"""
        return connectToMySQL(DATABASE_NAME).query_db(query, data_dict)
    
    @classmethod
    def get_by_id(cls, data_dict):
        query = """SELECT * FROM users WHERE id =%(id)s;"""
        result = connectToMySQL(DATABASE_NAME).query_db(query, data_dict)
        return cls(result[0])
    
    @classmethod
    def get_by_email(cls, data_dict):
        query = """SELECT * FROM users WHERE email = %(email)s;"""
        result = connectToMySQL(DATABASE_NAME).query_db(query, data_dict)
        if result:
            return cls(result[0])
        return False
    
    @classmethod
    def get_invalid_coachs(cls):
        query="""SELECT * from users where role='c' and is_valid=0;"""
        results = connectToMySQL(DATABASE_NAME).query_db(query)
        coachs = []
        if results:
            for row in results:
                
                coach = cls(row)
                coachs.append(coach)
            return coachs
        return False
    
    @classmethod
    def get_valid_coachs(cls):
        query="""SELECT * from users where role='c' and is_valid=1;"""
        results = connectToMySQL(DATABASE_NAME).query_db(query)
        coachs = []
        if results:
            for row in results:
                
                coach = cls(row)
                coachs.append(coach)
            return coachs
        return False
    
    @classmethod
    def get_valid_coachs_home(cls):
        query="""SELECT * from users where role='c' and is_valid=1 limit 3;"""
        results = connectToMySQL(DATABASE_NAME).query_db(query)
        coachs = []
        if results:
            for row in results:
                
                coach = cls(row)
                coachs.append(coach)
            return coachs
        return False
    
    @classmethod
    def get_all_users(cls):
        query="""SELECT * from users where role='u';"""
        results = connectToMySQL(DATABASE_NAME).query_db(query)
        users = []
        if results:
            for row in results:
                
                user = cls(row)
                users.append(user)
            return users
        return False
    
    @classmethod
    def validate_coach(cls,data_dict):
        query= """UPDATE users SET is_valid=1 WHERE id=%(id)s"""
        return connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
    
    @classmethod
    def delete_coach(cls,data_dict):
        query= """DELETE FROM users WHERE id=%(id)s"""
        return connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
    
    @staticmethod
    def validate_register(data_dict):
        is_valid = True
        if data_dict['role']=="u" and len(data_dict['weight'])==0:
            flash("Your weight is required", "weight")
            is_valid = False
        if data_dict['role']=="u" and len(data_dict['height'])==0:
            flash("Your height is required", "height")
            is_valid = False
        if data_dict['role']=="":
            flash("Role is required", "role")
            is_valid = False
        if len(data_dict['first_name'])< 2:
            
            flash("First Name too short", "first_name")
            is_valid = False
        if len(data_dict['last_name'])< 2:
            flash("Last Name too short .....", "last_name")
            is_valid = False
        if len(data_dict['password'])< 7:
            flash("Password too short .....", "password")
            is_valid = False
        elif data_dict['password'] != data_dict['confirm_password']:
            flash("Password and Confirm password Don't match !!!!!", "password")
            is_valid = False
        if not EMAIL_REGEX.match(data_dict['email']): 
            flash("Invalid email address!", "email")
            is_valid = False
        # if not MEASURES_REGEX.match(data_dict['height']) and data_dict['role']=="u":
        #     flash("height must be a number (cm)", "height")
        #     is_valid = False
        # if not MEASURES_REGEX.match(data_dict['weight']) and data_dict['role']=="u":
        #     flash("weight must be a number (kg)", "weight")
        #     is_valid = False
        elif User.get_by_email({'email':data_dict['email']}):
            flash("Email Already taken . Hope by you !!!! ", "email")
            is_valid = False
        
        return is_valid
    

    #==========Validate caoch===========
    @staticmethod
    def coach_validate_update(data_dict):
        is_valid = True
        if len(data_dict['first_name'])< 2:
            
            flash("First Name too short", "first_name")
            is_valid = False
        
        if len(data_dict['last_name'])< 2:
            flash("Last Name too short .....", "last_name")
            is_valid = False

        if not EMAIL_REGEX.match(data_dict['email']): 
            flash("Invalid email address!", "email")
            is_valid = False
        return is_valid
#====================Update Coach==========================
    @classmethod
    def update_coach(cls,data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s , picture = %(picture)s  WHERE id = %(id)s;"
        
        return connectToMySQL(DATABASE_NAME).query_db(query,data)
    @classmethod
    def update_user(cls,data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s , picture = %(picture)s  WHERE id = %(id)s;"
        
        return connectToMySQL(DATABASE_NAME).query_db(query,data)

#====================ban a coach ===================

    @classmethod
    def ban_coach(cls,data_dict):
        query= """UPDATE users SET is_banned=1 WHERE id=%(id)s"""
        return connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
   #    ===== ==== ====    Unban coach =================
    @classmethod
    def unban_coach(cls,data_dict):
        query= """UPDATE users SET is_banned=0 WHERE id=%(id)s"""
        return connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
