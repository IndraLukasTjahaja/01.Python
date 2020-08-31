import tkinter as tk
import tkinter.scrolledtext as scrolledtext
from tkinter import messagebox
from tkinter import filedialog
import os
import pandas as pd
import xlsxwriter


class Application:
    def __init__(self, master):
        self.master = master
        self.master.title('German_Credit')
        self.master.geometry('800x400')
        self.label = tk.Label(master, text='Read through German Credit')
        self.label.pack()
        self.output = tk.Label(master, text='Data Loaded: ')
        self.output.pack()
        self.button_loadexcel= tk.Button(master, text='Load Excel', command=self.load_excel)
        self.button_loadexcel.pack()
        self.button_summaryexcel= tk.Button(master, text='Export Summary', command=self.summary_excel)
        self.button_summaryexcel.pack()
        self.output1 = tk.Label(master, text='Data Saved: ')
        self.output1.pack()
        self.button_quit = tk.Button(master, text='Quit', command=on_closing)
        self.button_quit.pack()
    

    # create a menu bar with an Exit command
        menubar = tk.Menu(root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Exit", command=root.destroy)
        menubar.add_cascade(label="File", menu=filemenu)
        root.config(menu=menubar)

    # create a Text widget with a Scrollbar attached
        txt = scrolledtext.ScrolledText(root, undo=True)
        txt['font'] = ('consolas', '12')
        txt.pack(expand=True, fill='both')

    def load_excel(self, event=None):
        global path
        global df_credit
        global df_credit_shape
        path = filedialog.askopenfilename()
        df_credit = pd.read_excel(path)
        df_credit_shape = df_credit.shape
        self.output.config(text='Data loaded is:' + str(df_credit_shape))

    def summary_excel(self, event=None):
        global savename
        global export_excel
        savename = filedialog.asksaveasfilename()
        export_excel = savename.split('.')[0] + '.xlsx'
        self.output1.config(text='Data Saved:' + str(export_excel))
        writer = pd.ExcelWriter(export_excel, engine='xlsxwriter')
        writer.write_cells
        df_credit_tab1 = pd.crosstab(df_credit.purpose, df_credit.default)
        df_credit_tab1.to_excel(writer, sheet_name='Sheet1', startrow=5, header=True, index=True)
        workbook = writer.book
        worksheet = writer.sheets['Sheet1']
        worksheet.write('A1', 'Data Source:')
        worksheet.write('B1', path)
        worksheet.write('A2', 'Total Data')
        worksheet.write('B2', str(df_credit_shape))
        worksheet.write('A4', 'Basic Summary')
        writer.save()

    def some_action(self, event=None):
        """ It's very important to remember that if you use the 'command' argument
            to attach a handler function to a button, then the function cannot
            take any arguments. On the other hand, if you use bind() to attach
            a handler function, the function must take one argument.
            To avoid this conflict, use default argument 'event=None'. """
        self.output.config(text='Your text is: ' + self.entry.get())


    def on_closing(self, event=None):
        root.destroy()
        root.quit()

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root = tk.Tk()
app = Application(root)
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
