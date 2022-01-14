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
        image_get=requests.get(chuck_base_url)
        image_set=image_get.json()
        image=image_set.get("icon_url")
        return image