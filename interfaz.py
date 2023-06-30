import socket
import tkinter as tk
from tkinter import ttk
from functools import partial

host = socket.gethostname()
port = 8080


def sendOpc(opc):
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.connect((host,port))
        s.send(opc.encode('utf-8'))
    if opc == 'ff':
        ventana.destroy()
    print(opc)


ventana = tk.Tk()

ventana.title("S-Sampler")
ventana.config(width=385, height=420, background="#696969")

s = ttk.Style()
s.configure(
    "MyButton.TButton",
    background="#00FFFF"
)

key1 = ttk.Button(style="MyButton.TButton",command=partial(sendOpc,'11'))
key1.place(x = 5,y = 5,width = 90,heigh = 90)
key2 = ttk.Button(style="MyButton.TButton",command=partial(sendOpc,'12'))
key2.place(x = 100,y = 5,width = 90,heigh = 90)
key3 = ttk.Button(style="MyButton.TButton",command=partial(sendOpc,'13'))
key3.place(x = 195,y = 5,width = 90,heigh = 90)
key4 = ttk.Button(style="MyButton.TButton",command=partial(sendOpc,'14'))
key4.place(x = 290,y = 5,width = 90,heigh = 90)

key5 = ttk.Button(style="MyButton.TButton",command=partial(sendOpc,'21'))
key5.place(x = 5,y = 100,width = 90,heigh = 90)
key6 = ttk.Button(style="MyButton.TButton",command=partial(sendOpc,'22'))
key6.place(x = 100,y = 100,width = 90,heigh = 90)
key7 = ttk.Button(style="MyButton.TButton",command=partial(sendOpc,'23'))
key7.place(x = 195,y = 100,width = 90,heigh = 90)
key8 = ttk.Button(style="MyButton.TButton",command=partial(sendOpc,'24'))
key8.place(x = 290,y = 100,width = 90,heigh = 90)

key9 = ttk.Button(style="MyButton.TButton",command=partial(sendOpc,'31'))
key9.place(x = 5,y = 195,width = 90,heigh = 90)
key10 = ttk.Button(style="MyButton.TButton",command=partial(sendOpc,'32'))
key10.place(x = 100,y = 195,width = 90,heigh = 90)
key11 = ttk.Button(style="MyButton.TButton",command=partial(sendOpc,'33'))
key11.place(x = 195,y = 195,width = 90,heigh = 90)
key12 = ttk.Button(style="MyButton.TButton",command=partial(sendOpc,'34'))
key12.place(x = 290,y = 195,width = 90,heigh = 90)

key13 = ttk.Button(style="MyButton.TButton",command=partial(sendOpc,'41'))
key13.place(x = 5,y = 290,width = 90,heigh = 90)
key14 = ttk.Button(style="MyButton.TButton",command=partial(sendOpc,'42'))
key14.place(x = 100,y = 290,width = 90,heigh = 90)
key15 = ttk.Button(style="MyButton.TButton",command=partial(sendOpc,'43'))
key15.place(x = 195,y = 290,width = 90,heigh = 90)
key16 = ttk.Button(style="MyButton.TButton",command=partial(sendOpc,'44'))
key16.place(x = 290,y = 290,width = 90,heigh = 90)

closeBtn = ttk.Button(text='Cerrar',command=partial(sendOpc,'ff'))
closeBtn.place(x=140,y=390)
ventana.mainloop()
