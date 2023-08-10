import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, Entry, Button, END, filedialog
from tkinter import messagebox

def receive_messages(client_socket):
    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                print("Disconnected from server")
                break
            elif data.startswith("file:"):
                file_name = data[5:]
                receive_file(client_socket, file_name)
            else:
                display_message(data)
        except Exception as e:
            print("Error:", e)
            break

def send_unicast_message():
    recipient_address = unicast_input.get()
    message = input_box.get()
    if message:
        input_box.delete(0, tk.END)
        client_socket.send(f"unicast:{recipient_address}:{message}".encode('utf-8'))
        display_message(f"Sent to {recipient_address}: {message}")

def send_multicast_message():
    message = input_box.get()
    if message:
        input_box.delete(0, tk.END)
        client_socket.send(f"multicast:{message}".encode('utf-8'))
        display_message(f"Sent multicast: {message}")

def send_broadcast_message():
    message = input_box.get()
    if message:
        input_box.delete(0, tk.END)
        client_socket.send(message.encode('utf-8'))
        display_message(f"Sent broadcast: {message}")

def send_file(file_type):
    file_path = filedialog.askopenfilename()
    if file_path:
        file_name = file_path.split("/")[-1]
        client_socket.send(f"{file_type}:{file_name}".encode('utf-8'))
        with open(file_path, "rb") as f:
            file_data = f.read(1024)
            while file_data:
                client_socket.send(file_data)
                file_data = f.read(1024)
        display_message(f"Sent file: {file_name}")

def download_file(file_name):
    client_socket.send(f"download:{file_name}".encode('utf-8'))
    receive_file(client_socket, file_name)

def receive_file(client_socket, file_name):
    with open(f"received_files/{file_name}", "wb") as f:
        while True:
            file_data = client_socket.recv(1024)
            if not file_data:
                break
            f.write(file_data)
    print(f"Received file: {file_name}")
    show_file_received_notification(file_name)

def show_file_received_notification(file_name):
    messagebox.showinfo("File Received", f"Received file: {file_name}")

def display_message(message):
    text_area.config(state=tk.NORMAL)
    text_area.insert(tk.END, message + "\n")
    text_area.config(state=tk.DISABLED)

def on_closing():
    client_socket.close()
    window.destroy()

host = '10.217.18.147'
port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

window = tk.Tk()
window.title("Chat App")
window.geometry("400x500")

text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, state=tk.DISABLED)
text_area.pack(expand=True, fill=tk.BOTH)

input_box = Entry(window)
input_box.pack(side=tk.LEFT, expand=True, fill=tk.X)

unicast_input = Entry(window)
unicast_input.pack(side=tk.RIGHT)

send_unicast_button = Button(window, text="Send Unicast", command=send_unicast_message)
send_unicast_button.pack(side=tk.RIGHT)

send_multicast_button = Button(window, text="Send Multicast", command=send_multicast_message)
send_multicast_button.pack(side=tk.RIGHT)

send_broadcast_button = Button(window, text="Send Broadcast", command=send_broadcast_message)
send_broadcast_button.pack(side=tk.RIGHT)

send_file_unicast_button = Button(window, text="Send File Unicast", command=lambda: send_file("file_unicast"))
send_file_unicast_button.pack(side=tk.RIGHT)

send_file_multicast_button = Button(window, text="Send File Multicast", command=lambda: send_file("file_multicast"))
send_file_multicast_button.pack(side=tk.RIGHT)

send_file_broadcast_button = Button(window, text="Send File Broadcast", command=lambda: send_file("file_broadcast"))
send_file_broadcast_button.pack(side=tk.RIGHT)

download_button = Button(window, text="Download File", command=lambda: download_file("file_to_download.txt"))
download_button.pack(side=tk.RIGHT)

receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
receive_thread.start()

window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
