from tkinter import *


def Scankey(event):
    val = event.widget.get()
    print(val)

    if val == '':
        data = ''

    else:
        data = []
        for item in list:
            if val.lower() in item.lower():
                data.append(item)

    Update(data)


def Update(data):
    listbox.delete(0, 'end')
    # put new data
    for item in data:
        listbox.insert('end', item)


list = ('1', '11', '2', 'lol', 'a', 'lll', 'pp', 'ssl')

ws = Tk()
ws.geometry("750x250")

entry = Entry(ws)
entry.pack()
entry.bind('<KeyRelease>', Scankey)

listbox = Listbox(ws)
ws.mainloop()