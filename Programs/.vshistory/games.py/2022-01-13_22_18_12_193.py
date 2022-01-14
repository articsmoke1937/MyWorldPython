import requests
import University.globals as globals
from tkinter import messagebox

class chuck_jokes(object):
    joke_menu_url = "https://api.chucknorris.io/jokes/categories"
    chuck_icon_url= "https://assets.chucknorris.host/img/avatar/chuck-norris.png"


    ##chuck_icon=request2(chuck_icon_url)
    def joke_menu_get():
        joke_menu_url = "https://api.chucknorris.io/jokes/categories"
        request = requests.get(joke_menu_url)
        joke_menu = request.json()
        return joke_menu

    def display_joke(controller,btn_text):
        chuck_base_url= "https://api.chucknorris.io/jokes/random"
        for x in range(1):
            joke=''
            cat_url="%s?category=%s"%(chuck_base_url,btn_text)
            get=requests.get(cat_url)
            get_joke=get.json()
            joke=get_joke.get("value")
            messagebox.showinfo('Norrishment Time',f"Here is the Norris joke you requested:\n{joke}")
            print(joke)
            print(get_joke)
            print(cat_url)

    def joke_single_get():
        request = requests.get(joke_single_url)
        joke_single = request.json()
        return joke_single

    def get_chuck_joke_single(self,controller):
            chuck_joke_single=games_play.chuck_jokes.joke_single_get()
            print(chuck_joke_single)

    def get_chuck_menu():
            chuck_joke_menu=games_play.chuck_jokes.jokes_menu_get()
            print(chuck_joke_menu)

    