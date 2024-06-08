import requests
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pyperclip

def copytoclip(text):
    pyperclip.copy(text)
    messagebox.showinfo('Copied to clipboard', 'Link has been copied to clipboard')
def shortlink():
    window = tk.Toplevel()
    window.title('Loading...')
    window.geometry('300x130')
    lable = tk.Label(window, text='Wait, Loading...')
    lable.pack()
    progrees = ttk.Progressbar(window, mode='indeterminate')
    progrees.pack()
    progrees.start()
    try:
        urlapi = 'https://1da.ir/api'
        parameters = {'api': 'a36a01f0f9268f4ac5aa7232f661182d0cb6828c', 'url': link.get()}
        res = requests.get(url=urlapi, params=parameters, timeout=60)
        r = res.json()
        progrees.stop()
        window.destroy()
        if r['status'] == 'success':
            windows = tk.Toplevel()
            windows.title('Here\'s your link')
            windows.geometry('300x150')
            windows.config(bg='#3BA395')
            txt = tk.Label(windows, bg='#3BA395', font=('Lalezar', 12), text=f'your link has been shortened\n here is your link : {r['shortenedUrl']} \n UrlShortener v1.0 Beta By SACGroup')
            txt.pack()
            copy = tk.Button(windows, text='Copy to clipboard', command=lambda: copytoclip(r['shortenedUrl']))
            copy.pack()
        else:
            messagebox.showerror('Oops! It\'s an Error', 'shortening your link has been failed.\n check your connection and link then try again')
    except:
        progrees.stop()
        window.destroy()
        messagebox.showerror('Oops! It\' an error', 'Failed.\n check your connection and try again')

root = tk.Tk()
root.geometry('450x200')
root.title('UrlShortener')
root.config(bg='#3BA395')

lbl = tk.Label(text='Link :', font=('Arial', 14), bg='#3BA395')
link = tk.Entry(root)
button = tk.Button(root, text='Short Link', fg='#17D9F3', bg='#1B2171', command=shortlink)
lbl.pack(pady=0)
link.pack(pady=5.5)
button.pack(pady=10)

root.mainloop()