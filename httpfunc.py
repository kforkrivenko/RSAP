from tkinter import *
import threading
import socket


def Client(ip, port, Cname):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((str(ip), int(port)))
    msg = client.recv(4096)
    print(msg.decode("utf-8"))


# Server Dashboard
def __main__SD():
    tk = Tk()
    tk.attributes('-fullscreen', True)

    tk.title('SECL-Dashboard')

    x = 1080

    Top_Frame = Frame(width=x, height=50, bg='orange')
    Top_Frame.place(x=0, y=0)

    X_Button = Button(tk, width=5, height=1, text='X', bg='red', fg='white', command=tk.destroy)
    X_Button.place(x=1500, y=2)

    X_Button.config(font=("Bold", 16))

    tk.mainloop()

    print("Exiting")


# Config-CLIENT
def CONFIG2():
    root = Tk()
    root.resizable(width=False, height=False)

    root.title("SECL-Client")
    root.geometry('400x500')
    x = Frame(height=60, width=600, bg='green')
    x.pack()

    TITLE = Label(root, text="SECL", bg='green', fg='white')
    TITLE.place(x=140, y=4)
    TITLE.config(font=("Bold", 30))

    TP = Label(root, text='Client', bg='green', fg='white')
    TP.place(x=252, y=30)
    TP.config(font=("Bold", 15))

    # Create Button

    JoinB = Button(root, width=12, height=2, text='Join Server', bg='#00FF00',
                   command=lambda: [root.destroy(), __main__SD()])  # Server Join
    JoinB.place(x=90, y=440)

    # Cancle Button
    CancelB = Button(root, width=12, height=2, text='Cancel', bg='#D3D3D3', command=root.destroy)
    CancelB.place(x=200, y=440)

    CB = Button(root, width=5, height=2, text='<', bg='#FFFFFF', command=lambda: [root.destroy(), CONFIG1()])
    CB.place(x=350, y=455)
    CB.config(font=("Bold", 10))

    # Join
    port_I = Label(root, text='Port:')
    port_I.place(x=100, y=145)
    port_I.config(font=("Bold", 15))

    IP_I = Label(root, text='IP:')
    IP_I.place(x=100, y=200)
    IP_I.config(font=("Bold", 15))

    CN_I = Label(root, text='Client name:')
    CN_I.place(x=30, y=245)
    CN_I.config(font=("Bold", 15))

    ip = Entry(root, fg='black')
    ip.place(width=155, height=20)
    ip.place(x=150, y=200)

    port = Entry(root, fg='black')
    port.place(width=155, height=20)
    port.place(x=150, y=150)

    cn = Entry(root, fg='black')
    cn.place(width=155, height=20)
    cn.place(x=150, y=245)
    root.mainloop()


# Config-SERVER
def CONFIG1():
    root = Tk()
    root.resizable(width=False, height=False)

    root.title("SECL-Config")
    root.geometry('400x500')
    x = Frame(height=60, width=600, bg='blue')
    x.pack()

    TITLE = Label(root, text="SECL", bg='blue', fg='white')
    TITLE.place(x=140, y=4)
    TITLE.config(font=("Bold", 30))

    TP = Label(root, text='Server', bg='blue', fg='white')
    TP.place(x=252, y=30)
    TP.config(font=("Bold", 15))

    # Cancle Button
    CancleB = Button(root, width=12, height=2, text='Cancel', bg='#D3D3D3', command=root.destroy)
    CancleB.place(x=200, y=440)

    # Client Button

    CB = Button(root, width=5, height=2, text='>', bg='#FFFFFF', command=lambda: [root.destroy(), CONFIG2()])
    CB.place(x=350, y=455)
    CB.config(font=("Bold", 10))

    # INFO
    port_I = Label(root, text='Port:')
    port_I.place(x=80, y=145)
    port_I.config(font=("Bold", 15))

    Name_I = Label(root, text='Server Name:')
    Name_I.place(x=10, y=200)
    Name_I.config(font=("Bold", 15))

    MClient_I = Label(root, text="Max Client:")
    MClient_I.place(x=20, y=245)
    MClient_I.config(font=("Bold", 15))

    port = Entry(root, fg='black')
    port.place(width=155, height=20)
    port.place(x=150, y=150)

    name = Entry(root, fg='black')
    name.place(width=155, height=20)
    name.place(x=150, y=200)

    mclient = Entry(root, fg='black')
    mclient.place(width=155, height=20)
    mclient.place(x=150, y=245)

    server_running = False

    # sample client handler
    def handle_client(conn, addr):
        conn.send(bytes(f"Welcome to {name.get()}!", 'utf-8'))
        while True:
            data = conn.recv(512).decode().strip()
            print(data)
            if data == 'quit':
                break
        conn.close()

    def ALL_POINT():
        nonlocal server_running

        serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        print(ip, port.get())
        serv.bind((str(ip), int(port.get())))
        serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        serv.listen(int(mclient.get()))

        print("Server: Running")
        server_running = True
        while server_running:
            print('waiting connection ...')
            conn, addr = serv.accept()
            print('client connected', addr)
            # run client handler in thread so that server can serve new connection
            threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()

    # Create Button
    # CreateB = Button(root,width=12,height=2,text='Create Server',bg='#00FF00',command=lambda:[root.destroy(),ALL_POINT()])
    CreateB = Button(root, width=12, height=2, text='Create Server', bg='#00FF00', command=ALL_POINT)
    CreateB.place(x=90, y=440)

    root.mainloop()


#if __name__ == '__main__':
    #CONFIG1()