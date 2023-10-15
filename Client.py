import socket
import encryptor

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 8080

client_socket.connect((host, port))

message = client_socket.recv(1024)
try:
    msg = encryptor.decrypt_file(message)
    print(msg)
    fin = open("Decrypt_msg.txt", "w")
    fin.write(msg)
    fin.close()
    print("Message successfully decrypted.")
except Exception as e:
    print(f"Error during decryption: {str(e)}")

client_socket.close()
