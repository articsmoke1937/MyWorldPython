import yfinance as yf
import matplotlib.pyplot as plt
import University.globals as globals
import Programs.activity_choice as activity_choice
import tkinter.messagebox as messagebox


class stock_information():
    global stock_chose,ticker
    def __init__(self, stock_chose, ticker):
        self.stock=stock_chose
        self.ticker=ticker
    
    def stock_choice_get(self,stock_name_get):
        global stock_chose, ticker
        stock_chose=stock_name_get.get()
        stock_chose=stock_chose.upper()
        ticker=yf.Ticker(stock_chose)
        messagebox.showinfo("Stock Chosen",f'You have chosen {stock_chose}')

    def comp_info_get(self):
        stock_company_information=['symbol','website','industry','fullTimeEmployees','recommendationKey','longBusinessSummary']
        ticker.info['longBusinessSummary']

        for x in range(len(stock_company_information)):
            messagebox.showinfo('Company Information',f'{stock_company_information[x].capitalize()}: {stock.info[stock_company_information[x]]}')

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
       