from tkinter import *
from tkinter import ttk
from currencyConverter import *

class Main:

    def __init__(self):
        self.CurrencyConverter = CurrencyConverter()

    def mainloop(self):
        # create root window
        root = Tk()
        # root window title
        root.title("Currency Converter")
        # set geometry (width x height)
        root.geometry('500x500')
        #set background
        root.config(bg = '#3A3B3C')


        # create title label
        self.title_label = Label(root, text='Currency Converter', bg='#3A3B3C', fg='white', font=('franklin gothic medium', 20), relief='sunken')
        self.title_label.place(x=250, y=35, anchor='center')

        # create amount label
        self.input_amount_label = Label(root, text='Input Amount: ', bg='#3A3B3C', fg='white', font=('franklin gothic book', 15))
        self.input_amount_label.place(x=250, y=80, anchor='center')

        # create amount entry box
        self.amount_entry = Entry(root)
        self.amount_entry.config(width=25)
        self.amount_entry.place(x=250, y=110, anchor='center')

        # create 'from' label
        self.base_currency_label = Label(root, text='From: ', bg='#3A3B3C', fg='white', font=('franklin gothic book', 15))
        self.base_currency_label.place(x=250, y=140, anchor='center')

        # create 'to' label
        self.destination_currency_label = Label(root, text='To: ', bg='#3A3B3C', fg='white', font=('franklin gothic book', 15))
        self.destination_currency_label.place(x=250, y=200, anchor='center')

        # create dropdown Menu
        self.base_currency = StringVar()
        self.des_currency = StringVar()
        self.base_currency.set('EUR')
        self.des_currency.set('USD')
        options_list = list(self.CurrencyConverter.rates.keys())

        self.currency_combobox1 = ttk.Combobox(root, width=20, textvariable = self.base_currency, values = options_list, state = 'readonly')
        self.currency_combobox1.place(x=250, y=170, anchor='center')
        self.currency_combobox2 = ttk.Combobox(root, width=20, textvariable = self.des_currency, values = options_list, state='readonly')
        self.currency_combobox2.place(x=250, y=230, anchor='center')

        # create 'convert' button
        self.convert_button = Button(root, text='Convert', bg='#52595D', fg='white', command = self.on_convert_click)
        self.convert_button.place(x=230, y=270, anchor='center')

        # create 'clear' button
        self.clear_button = Button(root, text='Clear', bg='red', fg='white', command = self.on_clear_click)
        self.clear_button.place(x=280, y=270, anchor='center')

        # Create converted result field
        self.final_result = Label(root, text='', font=('calibri', 12), relief='sunken', width=40)
        self.final_result.place(x=250, y=310, anchor='center')

        # Execute Tkinter
        root.mainloop()

    def on_clear_click(self):
        self.amount_entry.delete(0,END)
        self.final_result.config(text='')

    def on_convert_click(self):
        amount = float(self.amount_entry.get())
        base_currency = self.base_currency.get() 
        des_currency = self.des_currency.get()
        converted_amount = self.CurrencyConverter.convert(base_currency, des_currency, amount)
        self.final_result.config(text=f'{amount} {base_currency} = {converted_amount} {des_currency}')


if __name__ == '__main__':
    main = Main()
    main.mainloop()