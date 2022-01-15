import yfinance as yf
import matplotlib.pyplot as plt
import University.globals as globals
import Programs.activity_choice as activity_choice
import tkinter.messagebox as messagebox


class stock_information():

    def __init__(self, stock_chose):
        self.stock=stock_chose

    def stock_choice_get(self,stock_name_get):
        stock_chose=stock_name_get.get()
        stock_chose=stock_chose.capitalize()
        messagebox.showinfo("Stock Chosen",f'You have chose {stock_chose}')

def stocks_choice(pname):
    cycle=1
    print(f'{globals.border}\nWelcome To The Stock Proram!\n{globals.border}')
    while (cycle==1):
        stockchoice = activity_choice.get_stock_symbol(pname)
        activity_choice.get_basic_stock_info(stockchoice)
        optionchoice = activity_choice.stock_activity_start(globals.stockoptions)
        if optionchoice == 1:
            stockchoice = activity_choice.get_stock_symbol(pname)
        elif optionchoice == 2:
            optioninput = 1
            while (optioninput < 17):
                print(f'\n{globals.border}')
                optioninput = activity_choice.stock_option_input(globals.stockoptions,pname)
                # activity_choice.stock_info_get(optioninput,stockchoice,pname)
            break
        elif optionchoice == 3:
            activity_choice.compare_get(stockchoice,pname)
            cycle=cycle+1
        
        elif optionchoice == 4:
            print(globals.border)
            break
       