import requests
import University.globals as globals
from tkinter import messagebox

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
            
   

    