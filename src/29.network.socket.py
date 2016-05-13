# Written by Vamei
# Server side
import socket

# Address
HOST = ''
PORT = 8000

http_resopnse_content = '''
HTTP/1.x 200 OK  
Content-Type: text/html

<head>
<title>WOW</title>
</head>
<html>
<p>Wow, Python Server</p>
</html>
'''

# Configure socket
s      = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

# passively wait, 3: maximum number of connections in the queue
s.listen(3)
# accept and establish connection
conn, addr = s.accept()
# receive message
request    = conn.recv(1024)

print( 'request is: ',request)
print( 'Connected by', addr)
# send message
conn.sendall(http_resopnse_content.encode())
# close connection
conn.close()