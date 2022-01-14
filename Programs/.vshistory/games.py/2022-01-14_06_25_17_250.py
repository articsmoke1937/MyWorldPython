import requests
import University.globals as globals
from tkinter import messagebox


#Chuck Norris Game
#############################################
class chuck_jokes(object):
    chuck_icon_url= "https://assets.chucknorris.host/img/avatar/chuck-norris.png"


    ##chuck_icon=request2(chuck_icon_url)
    def joke_menu_get():
        joke_menu_url = "https://api.chucknorris.io/jokes/categories"
        request = requests.get(joke_menu_url)
        joke_menu = request.json()
        return joke_menu

    #Display joke when button is pressed
    def display_joke(controller,btn_text):
        chuck_base_url= "https://api.chucknorris.io/jokes/random"
        for x in range(1):
            joke=''
            cat_url="%s?category=%s"%(chuck_base_url,btn_text)
            get=requests.get(cat_url)
            get_joke=get.json()
            joke=get_joke.get("value")
            messagebox.showinfo('Norrishment Time',f"Here is the Norris joke you requested:\n{joke}")

    def btn_layout(x):
        r=0
        c=0
        for k in range(x):
            t=int(((k+1)/(k+1))+1)
            if k % 2 ==0:
                c=t
                r=x
            else:
                c=t-1
                r=x+1
        return r,c

    def icon_get():
        chuck_base_url= "https://api.chucknorris.io/jokes/random"
        image_get=requests.get(chuck_base_url)
        image_set=image_get.json()
        image=image_set.get("icon_url")
        return image


#Rocks Paper Scissors Game
##########################################################################

class rocks_paper_scissors(object):
    def rps_play_rock():

        computer_choice = random.choice(['scissors', 'rock', 'paper'])
        user_choice = 'rock'
        if computer_choice == user_choice:
           messagebox.showinfo('RPS',f'\nI chose {computer_choice} so the game is a TIE')
        elif user_choice == 'rock' and computer_choice == 'scissors':
           messagebox.showinfo('RPS',f'\nI chose {computer_choice} so YOU WIN')
        elif user_choice == 'paper' and computer_choice == 'rock':
           messagebox.showinfo('RPS',F'\nI chose {computer_choice} so YOU WIN')
        elif user_choice == 'scissors' and computer_choice == 'paper':
           messagebox.showinfo('RPS','\nI chose {computer_choice} so YOU WIN')
        else:
           messagebox.showinfo('RPS',f'\nIchose {computer_choice} so YOU LOSE')
 