import requests
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pyperclip


def clearlog():
    try:
        with open('_internal/log-138975237378278663534.txt', 'w') as file:
            file.write('')
        messagebox.showinfo('Cleared', 'Logs cleared successfully')
    except FileNotFoundError:
        messagebox.showerror('Oops An Error!', 'Log file doesn\'t found\n report this to support\n Error Code : Err-wer25445wer46rty')



def viewlog():
    try:
        with open('_internal/log-138975237378278663534.txt', 'r') as file:
            text = file.read()
        logs = tk.Toplevel()
        logs.geometry('450x200')
        logs.title("Logs view")
        txts = tk.Text(logs, font=('Lalezar', '12'))
        txts.pack()
        txts.delete('1.0', tk.END)
        txts.insert('1.0', text)
    except FileNotFoundError:
        messagebox.showerror('Oops An Error!', 'Log file doesn\'t found\n report this to support\n Error Code : Err-wer25445wer46rty')
    except:
        messagebox.showerror('Oops! An error?', 'we had an error loading the logs.\n Give the error code to the Support team\n Error Code : Err112fr')
def copytoclip(text):
    pyperclip.copy(text)
    messagebox.showinfo('Copied to clipboard', 'Link has been copied to clipboard')
def shortlink(event=None):
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
            with open('_internal/log-138975237378278663534.txt', 'a') as file:
                linked = link.get()
                shorted = r['shortenedUrl']
                file.write(f'{linked} to {shorted}\n')
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
    except FileNotFoundError:
        progrees.stop()
        window.destroy()
        messagebox.showerror('Oops An Error!', 'Log file doesn\'t found\n report this to support\n Error Code : Err-wer25445wer46rty')
    except:
        progrees.stop()
        window.destroy()
        messagebox.showerror('Oops! It\' an error', 'Failed.\n check your connection and try again')

def create_menu(root_window):
    menubar = tk.Menu(root_window)
    log_menu = tk.Menu(menubar, tearoff=0)
    log_menu.add_command(label='View Log', command=viewlog)
    log_menu.add_command(label='Clear Log', command=clearlog)
    menubar.add_cascade(label='Log', menu=log_menu)
    root_window.config(menu=menubar)

root = tk.Tk()
root.geometry('450x200')
root.title('UrlShortener')
root.config(bg='#3BA395')



lbl = tk.Label(text='Link:', font=('Arial', 14), bg='#3BA395')
link = tk.Entry(root)
link.bind('<Return>', shortlink)  # Bind the <Return> key event to the shortlink function
button = tk.Button(root, text='Shorten Link', fg='#FFFFFF', bg='#007bff', padx=10, pady=5, command=shortlink)
lbl.pack(pady=10)
link.pack(pady=5)
button.pack(pady=10)

create_menu(root)

root.mainloop()
