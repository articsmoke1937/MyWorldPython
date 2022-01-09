import requests
import University.globals as globals

class chuck_jokes(object):
          
    def __init__(self, joke_menu_url,joke_single_url):
         joke_menu_url = "https://api.chucknorris.io/jokes/categories"
         joke_single_url = "https://api.chucknorris.io/jokes/random"

   
    def joke_menu_get(self):
        request = requests.get(joke_menu_url)
        joke_menu = request.json()
        return joke_menu

    def joke_single_get(self):
        request = requests.get(joke_single_url)
        joke_single = request.json()
        return joke_single

        while more_jokes==1:
            num=int(input("How many Norris Jokes would you like to hear? "))
            for x in range(num):
                request = requests.get(url)
                json = request.json()
                joke = json.get("value")
                print('\n',joke)
            jokecount=jokecount+1
            if jokecount>1:
                print('\n',"You have just been Norrished yet again!!\n")
            else:
                print('\n',"You have just been Norrished!\n")
                print(globals.border)
            print(f'Would {pname} like to play again?\n1. Yes\n2. No')
            more_jokes=int(input(globals.prompt))
