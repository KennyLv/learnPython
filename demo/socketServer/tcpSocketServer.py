# Written by Vamei
# use TCPServer
import SocketServer

HOST = ''
PORT = 8000
text_content = '''HTTP/1.x 200 OK  
Content-Type: text/html

<head>
<title>WOW</title>
</head>
<html>
<p>Wow, Python Server</p>
<IMG src="test.jpg"/>
</html>
'''

# Read picture, put into HTTP format
f = open('test.jpg','rb')
pic_content = '''
HTTP/1.x 200 OK  
Content-Type: image/jpg

'''
pic_content = pic_content + f.read()
f.close()

# This class defines response to each request
class MyTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        # self.request is the TCP socket connected to the client
        request = self.request.recv(1024).decode('utf-8') 

        method     = request.split(' ')[0]
        src        = request.split(' ')[1]
        resopnse_content = ''

        if method == 'GET':
            if src == '/test.jpg':
                resopnse_content = pic_content
            else: resopnse_content = text_content

        if method == 'POST':
            form = request.split('\r\n')
            idx = form.index('')             # Find the empty line
            entry = form[idx:]               # Main content of the request
            value = entry[-1].split('=')[-1]
            resopnse_content = text_content + '\n <p>' + value + '</p>'
        self.request.sendall(resopnse_content)

# Create the server
server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
# Start the server, and work forever
server.serve_forever()