############################################
#Initial window design taken from
# https://codereview.stackexchange.com/questions/221325/tkinter-application-with-multiple-windows
############################################

# import tkinter as tk
from tkinter import *
from tkinter import ttk
from University import user_profile as user_profile
from University import globals as globals
from tkinter import messagebox
# from tkinter.ttk import *
import json

LargeFont=("Verdana",16)

MedFont=("Verdana",12)

SmallFont=("Verdana",8)

###########################################################
# Global Variables
# User Information shared across multiple classes
###########################################################

user_id=user_profile.user.last_user(globals.user_log_filename)
new_user_id=user_profile.user.get_new_user_id()
user_in=user_profile.user.username_check(globals.users_file,user_id)

########################
# Base Program.  This will loop
# entire program until exited
# Controls start and stop of program
########################
class start_program:

  def __init__(self,master):
    self.master=master
    # master.attributes('-alpha', 0)
    start=page_view_controller()
    start.mainloop()


############################################
# Page controller - this class will control
# the layout of the pages 
# The method that is used to call the frames is housed here
############################################
class page_view_controller(Tk):
 
  def __init__(self,*args,**kwargs):
    Toplevel.__init__(self,*args,**kwargs)
   
    # Window page template
    container=Frame(self)
    Toplevel.geometry(self,'500x500')
    container.pack(side='top',fill='both',expand=True)
    container.grid_rowconfigure(0, weight = 1)
    container.grid_columnconfigure(0, weight = 1)

    # Create blank dictionary to hold pages
    self.frame={}

    # All windows that need to show will be defined here

    for F in (user_validation,user_search,user_set_up,start_page,games,chuck_norris_jokes,rocks_paper_scissors,stocks,regression,classification,sentiment_analysis,nat_lang_proc,ai_network):
        frame = F(container, self)
        self.frame[F] = frame
        frame.grid(row = 0, column = 0, sticky = "nsew") 
   
   # Determine initial first page display and set last user log in
    if user_in=='y':
        user_profile.user.set_last_user_log(user_id)
        self.show_frame(user_validation) 

    elif user_in=='n':
        self.show_frame(user_set_up)
    
  # Function called to display a frame
  def show_frame(self, cont):
    frame = self.frame[cont]  
    frame.tkraise() 



##################################################################
# Application Frames
# This section will contain classes for each page
# Each class will encompass code for the activities that occur on the page
# The idea will be to call pages when needed, do activity and escape to a new page
###################################################################


###################################################################
# User Validation and setup frame classes
##################################################################
class user_validation(Frame):  
  
  # Pulled in stored User Information.  Bring in at global level to class
  global user_id_get,pname,lname,city,age
  user_id_get,pname,lname,city,age=user_profile.user.get_saved_user_info(globals.users_file,user_id)
  user_profile.user.set_last_user_log(user_id)

  def __init__(self, parent, controller):
    Frame.__init__(self, parent) 

    intro_label = Label(self, text="Welcome To My World",font=LargeFont)
    intro_label.pack(pady=10,padx=10)
    user_confirm_label = Label(self,text=f'Are you {pname}?',font=MedFont)
    user_confirm_label.pack(pady=10,padx=10)

    yes_btn = Button(self, text = "Yes", command =lambda:[self.user_been_here_before(),controller.show_frame(start_page)], width = 20, height = 1)   
    yes_btn.pack()

    no_btn = Button(self, text = "No", command =lambda:controller.show_frame(user_search), width = 20, height = 1)   
    no_btn.pack()

    cancel_btn = Button(self, text = "Cancel", command =controller.destroy, width = 20, height = 1)   
    cancel_btn.pack()
 
  def user_start_setup_message(self):
    messagebox.showinfo('infromation',f'\nOhhhh, you have never been here before!\nWell, we are going to get you set up!!')

  def user_been_here_before(self):
    messagebox.showinfo('infromation',f'\nOhhhh, you have been here before {pname}!\nWelcome back!! I hope {city} is treating you well!')

class user_search(Frame):  

  def __init__(self, parent, controller):
    Frame.__init__(self, parent) 
    intro_label = Label(self, text=f'Well I need to know who you are!', font = LargeFont)
    intro_label.pack(pady=5,padx=5)
    get_name_label=Label(self,text="Please enter your User ID:")
    get_name_label.pack(pady=10,padx=10)

    get_user_id= Entry(self)
    get_user_id.pack(pady=5,padx=5)
    print(get_user_id)
    # user_in=user_profile.user.username_check
    
    submit_btn = Button(self, text = "Submit",command = lambda: [self.verify_id(controller,get_user_id)], width = 20, height = 1)

    back_to_main_menu_btn = Button(self, text = "Back to Main Menu",
    command = lambda: controller.show_frame(user_validation), width = 20, height = 1)
    

    submit_btn.pack()
    back_to_main_menu_btn.pack()


  ###################################
  # Set current user_id to last user logged in
  # and will act appropriately if user has been 
  # recognized
  ######################################
  def verify_id(self,controller,get_user_id):
    user_in,user_id=self.submit_user_id_check(get_user_id)
    if user_in=='y':
        user_profile.user.set_last_user_log(user_id)
        self.user_been_here_before(user_id)
        controller.show_frame(start_page)
    elif user_in=='n':
        user_profile.user.set_last_user_log(user_id)
        user_validation.user_start_setup_message(self)
    controller.show_frame(user_set_up)
  
  ################################################
  # Needed to grab the user_id from the entry box
  # and compare it to the user_ids in tthe user log
  # The compare will look to see if the user log has a match,
  # if so, it will set the user_in flag to yes and break the loop.
  # if no match is found, user_in flag will be set to 0 and the user_id
  # will be set to the next available number
  ####################################################
  def submit_user_id_check(self,get_user_id):
    user_id=int(get_user_id.get())
    with open(globals.users_file) as open_user_file:
        user_id_check=json.load(open_user_file)
    for x in user_id_check['user_id'][0]:
        if x == user_id:
          user_in='y'
          break
    else:
      user_in='n'
    if user_in=='n':
        user_id=len(user_id_check['user_id'][0])
        print(user_id,user_in)
    return user_in,user_id

  def user_been_here_before(self,user_id):
    user_id,pname,lname,city,age=user_profile.user.get_saved_user_info(globals.users_file,user_id)
    messagebox.showinfo('infromation',f'\nOhhhh, you have been here before {pname}!\nWelcome back!! I hope {city} is treating you well!')

#Grab new User information and save to user file
class user_set_up(Frame):  
  
  def __init__(self, parent, controller):
    Frame.__init__(self, parent) 
    controller.title("Welcome Back Fuckers")  
    label = Label(self, text="User Set Up",font=LargeFont)
    label.pack(pady=10,padx=10)
    greeting_label=Label(self,text=f'Please provide the information requested below',font=MedFont)
    greeting_label.pack(pady=5,padx=5)

    firstname_get_label = Label(self, text=f'First Name', font = SmallFont)
    firstname_get_label.pack(pady=5,padx=5)
    firstname_get_entry= Entry(self)
    firstname_get_entry.pack(pady=5,padx=5)

    lastname_get_label = Label(self, text=f'Last Name', font=SmallFont)
    lastname_get_label.pack(pady=5,padx=5)
    lastname_get_entry= Entry(self)
    lastname_get_entry.pack(pady=5,padx=5)

    age_get_label = Label(self, text=f'Age', font = SmallFont)
    age_get_label.pack(pady=5,padx=5)
    age_get_entry= Entry(self)
    age_get_entry.pack(pady=5,padx=5)

    city_get_label = Label(self, text=f'City', font = SmallFont)
    city_get_label.pack(pady=5,padx=5)
    city_get_entry=Entry(self)
    city_get_entry.pack(pady=5,padx=5)

    save_btn = Button(self, text = "Save",command =  lambda:[user_profile.user.get_new_user_info(self,firstname_get_entry,lastname_get_entry,age_get_entry,city_get_entry)
                      ,self.user_info_save_confirm(),controller.show_frame(start_page)], width = 20, height = 1)
    save_btn.pack()

    cancel_btn = Button(self, text = "Cancel", command =lambda:controller.show_frame(user_validation), width = 20, height = 1)   
    cancel_btn.pack()
    
  def user_info_save_confirm(self):
    pname=user_profile.user.get_saved_user_info(globals.users_file,new_user_id)[1]
    user_profile.user.set_last_user_log(new_user_id)
    messagebox.showinfo('infromation',f'\n{pname}, your user information has been saved.\nNow its time to move on to the fun!!')

		# but
###################################################################
# Application Body Frame classes
##################################################################
class start_page(Frame):  

  def __init__(self, parent, controller):
    Frame.__init__(self, parent) 
    label = Label(self, text="Welcome To My World", font = LargeFont)
    label.pack(pady=10,padx=10)
    button1 = Button(self, text = "Games",
    command = lambda: controller.show_frame(games), width = 20, height = 1)   
    button2 = Button(self, text = "Stock Market",
    command = lambda: controller.show_frame(stocks), width = 20, height = 1)
    button3 = Button(self, text = "Regression Project",
    command = lambda: controller.show_frame(regression), width = 20, height = 1)
    button4 = Button(self, text = "Classification Project",
    command = lambda: controller.show_frame(classification), width = 20, height = 1)
    button5 = Button(self, text = "Sentiment Analysis",
    command = lambda: controller.show_frame(sentiment_analysis), width = 20, height = 1)
    button6 = Button(self, text = "Natural Language Processing",
    command = lambda: controller.show_frame(nat_lang_proc), width = 20, height = 1)
    button7 = Button(self, text = "Artificial Neural Networks",
    command = lambda: controller.show_frame(ai_network), width = 20, height = 1)
    button8 = Button(self, text = "Back to Main Menu",
    command = lambda: controller.show_frame(start_page), width = 20, height = 1)
    button1.pack()
    button2.pack()
    button3.pack()
    button4.pack()
    button5.pack()
    button6.pack()
    button7.pack()
    button8.pack()
#####################################################
# GAMES
#####################################################
class games(Frame):  

  def __init__(self, parent, controller):
    Frame.__init__(self, parent) 
    label = Label(self, text="Welcome To My World", font = LargeFont)
    label.pack(pady=10,padx=10)
    button1 = Button(self, text = "Games",
    command = lambda: controller.show_frame(games), width = 20, height = 1)   
    button2 = Button(self, text = "Stock Market",
    command = lambda: controller.show_frame(stocks), width = 20, height = 1)
    button3 = Button(self, text = "Regression Project",
    command = lambda: controller.show_frame(regression), width = 20, height = 1)
    button4 = Button(self, text = "Classification Project",
    command = lambda: controller.show_frame(classification), width = 20, height = 1)
    button5 = Button(self, text = "Sentiment Analysis",
    command = lambda: controller.show_frame(sentiment_analysis), width = 20, height = 1)
    button6 = Button(self, text = "Natural Language Processing",
    command = lambda: controller.show_frame(nat_lang_proc), width = 20, height = 1)
    button7 = Button(self, text = "Artificial Neural Networks",
    command = lambda: controller.show_frame(ai_network), width = 20, height = 1)
    button8 = Button(self, text = "Back to Main Menu",
    command = lambda: controller.show_frame(start_page), width = 20, height = 1)
    button1.pack()
    button2.pack()
    button3.pack()
    button4.pack()
    button5.pack()
    button6.pack()
    button7.pack()
    button8.pack()

######################################################
# Chuck Norris Jokes Frame
#####################################################
class chuck_norris_jokes(Frame):  
  print("Greetings8!")
  def __init__(self, parent, controller):
    Frame.__init__(self, parent) 
    label = Label(self, text="Welcome To My World", font = LargeFont)
    label.pack(pady=10,padx=10)
    button1 = Button(self, text = "Chuck Norris Jokes",
    command = lambda: controller.show_frame(chuck_norris_jokes), width = 20, height = 1)   
    button2 = Button(self, text = " Stock Program ",
    command = lambda: controller.show_frame(stocks), width = 20, height = 1)
    button3 = Button(self, text = "Rocks Papers Scissors",
    command = lambda: controller.show_frame(rocks_paper_scissors), width = 20, height = 1)
    button1.pack()
    button2.pack()
    button3.pack()

#####################################################
# STOCKS
#####################################################

######################################################
# STOCK PROGRAM FRAME
#####################################################
class stocks(Frame):  
  print("Greetings8!")
  def __init__(self, parent, controller):
    Frame.__init__(self, parent) 
    label = Label(self, text="Welcome To My World", font = LargeFont)
    label.pack(pady=10,padx=10)
    button1 = Button(self, text = "Chuck Norris Jokes",
    command = lambda: controller.show_frame(chuck_norris_jokes), width = 20, height = 1)   
    button2 = Button(self, text = " Stock Program ",
    command = lambda: controller.show_frame(stocks), width = 20, height = 1)
    button3 = Button(self, text = "Rocks Papers Scissors",
    command = lambda: controller.show_frame(rocks_paper_scissors), width = 20, height = 1)
    button1.pack()
    button2.pack()
    button3.pack()

######################################################
# ROCKS PAPER SCISSORS APPLICATION FRAME
#####################################################
class rocks_paper_scissors(Frame):  
  print("Greetings8!")
  def __init__(self, parent, controller):
    Frame.__init__(self, parent) 
    label = Label(self, text="Welcome To My World", font = LargeFont)
    label.pack(pady=10,padx=10)
    button1 = Button(self, text = "Chuck Norris Jokes",
    command = lambda: controller.show_frame(chuck_norris_jokes), width = 20, height = 1)   
    button2 = Button(self, text = " Stock Program ",
    command = lambda: controller.show_frame(stocks), width = 20, height = 1)
    button3 = Button(self, text = "Rocks Papers Scissors",
    command = lambda: controller.show_frame(rocks_paper_scissors), width = 20, height = 1)
    button1.pack()
    button2.pack()
    button3.pack()

#####################################################
# REGRESSION
#####################################################
class regression(Frame):  

  def __init__(self, parent, controller):
    Frame.__init__(self, parent) 
    label = Label(self, text="Welcome To My World", font = LargeFont)
    label.pack(pady=10,padx=10)
    button1 = Button(self, text = "Games",
    command = lambda: controller.show_frame(games), width = 20, height = 1)   
    button2 = Button(self, text = "Stock Market",
    command = lambda: controller.show_frame(stocks), width = 20, height = 1)
    button3 = Button(self, text = "Regression Project",
    command = lambda: controller.show_frame(regression), width = 20, height = 1)
    button4 = Button(self, text = "Classification Project",
    command = lambda: controller.show_frame(classification), width = 20, height = 1)
    button5 = Button(self, text = "Sentiment Analysis",
    command = lambda: controller.show_frame(sentiment_analysis), width = 20, height = 1)
    button6 = Button(self, text = "Natural Language Processing",
    command = lambda: controller.show_frame(nat_lang_proc), width = 20, height = 1)
    button7 = Button(self, text = "Artificial Neural Networks",
    command = lambda: controller.show_frame(ai_network), width = 20, height = 1)
    button8 = Button(self, text = "Back to Main Menu",
    command = lambda: controller.show_frame(start_page), width = 20, height = 1)
    button1.pack()
    button2.pack()
    button3.pack()
    button4.pack()
    button5.pack()
    button6.pack()
    button7.pack()
    button8.pack()
#####################################################
# CLASSIFICATIONS 
#####################################################
class classification(Frame):  

  def __init__(self, parent, controller):
    Frame.__init__(self, parent) 
    label = Label(self, text="Welcome To My World", font = LargeFont)
    label.pack(pady=10,padx=10)
    button1 = Button(self, text = "Games",
    command = lambda: controller.show_frame(games), width = 20, height = 1)   
    button2 = Button(self, text = "Stock Market",
    command = lambda: controller.show_frame(stocks), width = 20, height = 1)
    button3 = Button(self, text = "Regression Project",
    command = lambda: controller.show_frame(regression), width = 20, height = 1)
    button4 = Button(self, text = "Classification Project",
    command = lambda: controller.show_frame(classification), width = 20, height = 1)
    button5 = Button(self, text = "Sentiment Analysis",
    command = lambda: controller.show_frame(sentiment_analysis), width = 20, height = 1)
    button6 = Button(self, text = "Natural Language Processing",
    command = lambda: controller.show_frame(nat_lang_proc), width = 20, height = 1)
    button7 = Button(self, text = "Artificial Neural Networks",
    command = lambda: controller.show_frame(ai_network), width = 20, height = 1)
    button8 = Button(self, text = "Back to Main Menu",
    command = lambda: controller.show_frame(start_page), width = 20, height = 1)
    button1.pack()
    button2.pack()
    button3.pack()
    button4.pack()
    button5.pack()
    button6.pack()
    button7.pack()
    button8.pack()

#####################################################
# SENTIMENT ANALYSIS
#####################################################
class sentiment_analysis(Frame):  

  def __init__(self, parent, controller):
    Frame.__init__(self, parent) 
    label = Label(self, text="Welcome To My World", font = LargeFont)
    label.pack(pady=10,padx=10)
    button1 = Button(self, text = "Games",
    command = lambda: controller.show_frame(games), width = 20, height = 1)   
    button2 = Button(self, text = "Stock Market",
    command = lambda: controller.show_frame(stocks), width = 20, height = 1)
    button3 = Button(self, text = "Regression Project",
    command = lambda: controller.show_frame(regression), width = 20, height = 1)
    button4 = Button(self, text = "Classification Project",
    command = lambda: controller.show_frame(classification), width = 20, height = 1)
    button5 = Button(self, text = "Sentiment Analysis",
    command = lambda: controller.show_frame(sentiment_analysis), width = 20, height = 1)
    button6 = Button(self, text = "Natural Language Processing",
    command = lambda: controller.show_frame(nat_lang_proc), width = 20, height = 1)
    button7 = Button(self, text = "Artificial Neural Networks",
    command = lambda: controller.show_frame(ai_network), width = 20, height = 1)
    button8 = Button(self, text = "Back to Main Menu",
    command = lambda: controller.show_frame(start_page), width = 20, height = 1)
    button1.pack()
    button2.pack()
    button3.pack()
    button4.pack()
    button5.pack()
    button6.pack()
    button7.pack()
    button8.pack()
#####################################################
# NATURAL LANGUAGE PROCESSING
#####################################################
class nat_lang_proc(Frame):  

  def __init__(self, parent, controller):
    Frame.__init__(self, parent) 
    label = Label(self, text="Welcome To My World", font = LargeFont)
    label.pack(pady=10,padx=10)
    button1 = Button(self, text = "Games",
    command = lambda: controller.show_frame(games), width = 20, height = 1)   
    button2 = Button(self, text = "Stock Market",
    command = lambda: controller.show_frame(stocks), width = 20, height = 1)
    button3 = Button(self, text = "Regression Project",
    command = lambda: controller.show_frame(regression), width = 20, height = 1)
    button4 = Button(self, text = "Classification Project",
    command = lambda: controller.show_frame(classification), width = 20, height = 1)
    button5 = Button(self, text = "Sentiment Analysis",
    command = lambda: controller.show_frame(sentiment_analysis), width = 20, height = 1)
    button6 = Button(self, text = "Natural Language Processing",
    command = lambda: controller.show_frame(nat_lang_proc), width = 20, height = 1)
    button7 = Button(self, text = "Artificial Neural Networks",
    command = lambda: controller.show_frame(ai_network), width = 20, height = 1)
    button8 = Button(self, text = "Back to Main Menu",
    command = lambda: controller.show_frame(start_page), width = 20, height = 1)
    button1.pack()
    button2.pack()
    button3.pack()
    button4.pack()
    button5.pack()
    button6.pack()
    button7.pack()
    button8.pack()

#####################################################
# AI NEURAL NETWORK
#####################################################
class ai_network(Frame):  

  def __init__(self, parent, controller):
    Frame.__init__(self, parent) 
    label = Label(self, text="Welcome To My World", font = LargeFont)
    label.pack(pady=10,padx=10)
    button1 = Button(self, text = "Games",
    command = lambda: controller.show_frame(games), width = 20, height = 1)   
    button2 = Button(self, text = "Stock Market",
    command = lambda: controller.show_frame(stocks), width = 20, height = 1)
    button3 = Button(self, text = "Regression Project",
    command = lambda: controller.show_frame(regression), width = 20, height = 1)
    button4 = Button(self, text = "Classification Project",
    command = lambda: controller.show_frame(classification), width = 20, height = 1)
    button5 = Button(self, text = "Sentiment Analysis",
    command = lambda: controller.show_frame(sentiment_analysis), width = 20, height = 1)
    button6 = Button(self, text = "Natural Language Processing",
    command = lambda: controller.show_frame(nat_lang_proc), width = 20, height = 1)
    button7 = Button(self, text = "Artificial Neural Networks",
    command = lambda: controller.show_frame(ai_network), width = 20, height = 1)
    button8 = Button(self, text = "Back to Main Menu",
    command = lambda: controller.show_frame(start_page), width = 20, height = 1)
    button1.pack()
    button2.pack()
    button3.pack()
    button4.pack()
    button5.pack()
    button6.pack()
    button7.pack()
    button8.pack()
    # class user_not_recognized:
#   def __init__(self,master):
#   self.master=master
#   master.title('My World Python')
#   self.label=Label(master,text="Welcome To My World!!",font=LargeFont)
#   self.label.pack()

#   ### Add buttons to start and close program

#   self.start_button =Button(master, text="Start Program", command=page_view_controller_new_user,font=MedFont)
#   self.start_button.pack()

#   self.close_button = Button(master, text="Close", command=master.destroy,font=MedFont)
#   self.close_button.pack()

# class user_recognized:
#   def __init__(self,master,pname):
#   self.master=master
#   master.title('My World Python')
#   self.label=Label(master,text="Welcome To My World!!", font=LargeFont)
#   self.label.pack()
#   self.user_confirm=Label(master,text=f'Are you {pname}?', font=LargeFont)
#   self.user_confirm.pack()
    
#   start_button =Button(master, text="Yes", command=page_view_controller_valid_user, font=MedFont)
#   start_button.pack()

#   no_button =Button(master, text="No", command=page_view_controller_new_user, font=MedFont)
#   no_button.pack()
#   no_button.bind('<Button-1>',self.hide_me)

#   exit_btn =Button(master, text="Cancel", command=master.destroy, font=MedFont)
#   exit_btn.pack()
#   # close_button = Button(master, text="No", command=[lambda: self.hide_me(self.close_button),user_not_recognized(master),master.destroy])
#   # close_button.pack()
  
#   def hide_me(self, event):
#   print('hide me')
#   event.place_forget()
    # self.start_button =Button(master, text="Yes2", command=page_view_controller)
    # self.start_button.pack()

    # self.close_button = Button(master, text="No", command=user_validation)
    # self.close_button.pack()

##################################################################
# GUI page controller.  Program starts here and first page is created
# This class will define the window in which the app is run from.  
# Each page called will use this as base for their design.
# As a page is called by a function from another page, the show_frame function will show the page
##################################################################
# class page_view_controller_new_user(Tk):
 
#   def __init__(self,*args,**kwargs):
#   Toplevel.__init__(self,*args,**kwargs)
   
#   # Window page template
#   container=Frame(self)
#   Toplevel.geometry(self,'500x500')
#   container.pack(side='top',fill='both',expand=True)
#   container.grid_rowconfigure(0, weight = 1)
#   container.grid_columnconfigure(0, weight = 1)

#   # Create blank dictionary to hold pages
#   self.frame={}

#   # All windows that need to show will be defined here
#   for F in (user_set_up,user_validation,StartPage2):
#     frame = F(container, self)
#     self.frame[F] = frame
#     frame.grid(row = 0, column = 0, sticky = "nsew") 
    
#   self.show_frame(user_set_up) 

#   def show_frame(self, cont):
#   frame = self.frame[cont]  
#   frame.tkraise()  

