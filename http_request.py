# Author: Emerson Araujo
import socket
import ssl
import webbrowser

HOST = 'www.unip.br'
PORT = 443

# https://unip.br/presencial/
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))
mysock = ssl.wrap_socket(mysock, keyfile=None, certfile=None, server_side=False, cert_reqs=ssl.CERT_NONE, ssl_version=ssl.PROTOCOL_SSLv23)
mysock.sendall(b"GET /presencial/ HTTP/1.1\r\nHOST: unip.br\r\naccept: */*\r\n\r\n")
page = b""

while True:
    data = mysock.recv(20000)
    if not data:
        break
    else:
        page = page+data

pos = page.find(b"\r\n\r\n")

page = page[pos+4:]
mysock.close()
print(page)
fhand = open("site_unip.html", "wb")
fhand.write(page)
webbrowser.open_new_tab('site_unip.html')
fhand.close()