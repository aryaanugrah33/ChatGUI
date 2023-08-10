**Step 1: Preparation**

1. Make sure you have a working Python installation on your computer. If not, you can download and install Python from the official python.org site.

2. Make sure all client and server instances are on the same WiFi network.

**Step 2: File and Directory Preparation**

1. Create a new directory named "received_files" in the same directory as server.py. This is the place where received files will be stored.

2. (Optional) If you want to have the ability to "download" files, create a new directory named "files_to_send" in the same directory as server.py. This is the place where the files that will be sent from the server to the client will be stored.

**Step 3: Running the Server**

1. Open a terminal or command prompt.

2. Navigate to the directory where server.py is located using the `cd /path/to/directory` command.

3. Run the server with the following command:
    ```
    python server. py
    ```

**Step 4: Running the Client**

1. Open a terminal or command prompt (open multiple instances according to the number of clients you want to run).

2. Navigate to the directory where client.py is located using the `cd /path/to/directory` command.

3. Run the client with the following command:
    ```
    python client. py
    ```

**Step 5: Interact with the Chat Application**

1. Each client window will appear. You can send text messages to all clients, or send/receive files.

2. To send a message, write a message in the text input box and press the "Send Unicast" button to send a private message to a specific client, or "Send Multicast" to send a message to all clients, or "Send Broadcast" to send a broadcast message to all client.

3. To send a file, press the "Send File Unicast", "Send File Multicast" or "Send File Broadcast" button. You will be asked to select a file to upload.

4. If you want to download the file, press the "Download File" button. You will be asked to enter the name of the file you want to download.

5. There will be a notification to inform you when the file is successfully received.

**Vital Records**:
- Make sure to run the server first before running the client.
- Make sure the IP address and port used on the client match the one used on the server.
- Ensure appropriate access permissions for previously mentioned file storage directories.

By following the steps above, you will be able to run a chat application with the feature of sending and receiving files and interacting with all the features that have been created. Be sure to run multiple client instances to observe communication between clients.