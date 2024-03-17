import socket
import threading
import tkinter as tk

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            message_listbox.insert(tk.END, message)
        except:
            break

def send_message(event=None):
    message = my_message.get()
    my_message.set("")
    client_socket.send(bytes(message, 'utf-8'))
    if message == "{quit}":
        client_socket.close()
        root.quit()

def on_closing(event=None):
    my_message.set("{quit}")
    send_message()

def start_chat():
    global client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip.get(), 12345))

    receive_thread = threading.Thread(target=receive_messages)
    receive_thread.start()

root = tk.Tk()
root.title("局域网聊天室")

server_ip = tk.StringVar()
server_ip_entry = tk.Entry(root, textvariable=server_ip)
server_ip_entry.pack(fill=tk.X)

start_button = tk.Button(root, text="连接服务器", command=start_chat)
start_button.pack()

message_frame = tk.Frame(root)
message_frame.pack()

my_message = tk.StringVar()
my_message_entry = tk.Entry(message_frame, textvariable=my_message)
my_message_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
my_message_entry.bind("<Return>", send_message)

send_button = tk.Button(message_frame, text="发送", command=send_message)
send_button.pack(side=tk.RIGHT)

message_listbox = tk.Listbox(root, height=15, width=50)
message_listbox.pack(fill=tk.BOTH, expand=True)

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
