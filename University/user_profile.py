import json
from University import globals as globals

class user(object):
    global user_id,pname,lname,city,age
   
    def __init__(self,user_id,pname,lname,city,age):
        self.user_id=user_id
        self.pname=pname
        self.lname=lname
        self.city=city
        self.age=age

#======================= =================
# Existing user functions
#========================================   
    #Get Last user logged in
    def last_user(user_log_filename):
        with open(globals.user_log_filename) as last_user_filename:
            user_id = json.load(last_user_filename)
        return user_id
    
    # Diplay current User's info
    def display_user_info(self):
        user_info=f'{self.user_id}\n{self.first}\n{self.last}\n{self.city}\n{self.age}'
        return user_info.title()
    
    #Check username in users file
    def username_check(user_file,user_id):
        with open(user_file) as open_user_file:
            username_check=json.load(open_user_file)
        if user_id in username_check['user_id'][0]:
            user_in='y'
        else:
            user_in='n'
        return user_in
        
#========================================
#User Attributes
#========================================
    #Get either user number or create number for new user
    def get_user_id(user_file,pname):
        with open(user_file) as open_user_file:
            username_check=json.load(open_user_file)
        user_id=-1
        for x in username_check['first'][0]:
            if x != pname:
                user_id=int(user_id)+1
            else:
                break
        user_id=int(user_id)
        return user_id
    
    #Get updated user information
    def get_saved_user_info(user_file,user_id):
        with open(user_file) as open_user_file:
            username_check=json.load(open_user_file)
            user_id_get=username_check['user_id'][0][int(user_id)] 
            pname=username_check['first'][0][int(user_id)]
            lname=username_check['last'][0][int(user_id)]
            city=username_check['city'][0][int(user_id)]
            age=username_check['age'][0][int(user_id)]
        return user_id_get,pname,lname,city,age
    
##################################################################
# New User setup
##################################################################
    
    def set_last_user_log(user_id):
         with open(globals.user_log_filename,'w') as f:
            json.dump(user_id,f)

    #Get new user ID
    def get_new_user_id():
        with open(globals.users_file) as open_user_file:
            username_check=json.load(open_user_file)
        user_id=int(len(username_check['first'][0]))
        new_user_id=user_id-1+1
        # for x in username_check['first'][0]:
        #     if x != pname:
        #         new_user_id=int(user_id)+1 
        return new_user_id
    
    #New User info will be retreived from Entry fiedl
    def get_new_user_info(self,firstname_get_entry,lastname_get_entry,age_get_entry,city_get_entry,):
        user.firstname_set(self,firstname_get_entry)
        user.lastname_set(self,lastname_get_entry)
        user.age_set(self,age_get_entry)
        user.city_set(self,city_get_entry)

    # Set variables will call teh update file to inser user info into history
    def firstname_set(self,firstname_get_entry):
        self.pname=firstname_get_entry.get()
        self.pname=self.pname.capitalize()
        self.user_id=user.get_new_user_id()
        user.update_users_file_pname(self,self.pname)
        user.update_users_file_user_id(self,self.user_id)
    
    def lastname_set(self,lastname_get_entry):
        self.lname=lastname_get_entry.get()
        self.lname=self.lname.capitalize()
        user.update_users_file_lname(self,self.lname)

    def age_set(self,age_get_entry):
        self.age=age_get_entry.get()
        self.age=self.age.capitalize()
        user.update_users_file_age(self,self.age)

    def city_set(self,city_get_entry):
        self.city=city_get_entry.get()
        self.city=self.city.capitalize()
        user.update_users_file_city(self,self.city)

    # Add User function updates user file
    def add_user(user_file, key,v1,value):
        with open(user_file) as f:
            users_file_decoded=json.load(f)
            users_file_decoded[key][v1].append(value)
        json.dump(users_file_decoded, open(user_file, 'w'))

    def update_users_file_user_id(self,user_id):
        user.add_user(globals.users_file,'user_id',0,int(user_id))       
    
    def update_users_file_pname(self,pname):
        user.add_user(globals.users_file,'first',0,pname)      
        
    def update_users_file_lname(self,lname):
        user.add_user(globals.users_file,'last',0,lname)
            
    def update_users_file_city(self,city):
        user.add_user(globals.users_file,'city',0,city) 
        
    def update_users_file_age(self,age):
        user.add_user(globals.users_file,'age',0,int(age))  
      
      
    
#************************************************
# Admin User Maintenance
#************************************************
# def user_clear(user_file):
#     print(user_file)
#     with open(user_file) as open_user_file:
#         user_clear=json.load(open_user_file)
#     for x in user_clear['user_id'][0]:
#         if x != '':
#             del user_clear['user_id'][0]
#             del user_clear['first'][0]
#             del user_clear['last'][0]
#             del user_clear['city'][0]
#             del user_clear['age'][0]
#         json.dump(open_user_file, open(user_file, 'w'))
#         for x in user_clear['user_id'][0]:
#             print('delete')
#             print(x)   
                
#         else:
#             break


    # def user_clear(user_file):
    #     print(user_file)
    #     with open(user_file) as open_user_file:
    #         user_clear = json.load(open_user_file)
    #     for key, value in user_clear['user_id'][0]:
    #         del user_clear[key][value]
    #         json.dump(open_user_file, open(user_file, 'w'))


        
   
