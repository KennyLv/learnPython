# Written by Vamei
# Server side
import socket
import sqliteDB as db

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
# Read picture, put into HTTP format
pic_content = '''
HTTP/1.x 200 OK  
Content-Type: image/jpg

'''
f = open('D:\\HBuild_WorkSpace\\learnPython\\demo\\socketServer\\test.jpg','rb')
pic_content = f.read()
f.close()

# Configure socket
s      = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))


# Serve forever
while True:
    # passively wait, 3: maximum number of connections in the queue
    s.listen(1)
    # accept and establish connection
    conn, addr = s.accept()
    # receive message
    request    = conn.recv(1024).decode('utf-8')         # 1024 is the receiving buffer size
    method     = request.split(' ')[0]
    src        = request.split(' ')[1]
    #print( 'request is: ',request)
    #print( 'Connected by', addr)
    # if GET method request
    if method == 'GET':
        if src == '/test.jpg':
            conn.sendall(pic_content)
        else :
            content_text = ''
            for row in db.queryAll():
                content_text = content_text + '<p>' + str(row[1]) + '</p>' + '<p>' + str(row[2]) + '</p>' + '<p>' + str(row[3]) + '</p>' + '<p>' + str(row[5]) + '</p>'
            http_resopnse_content = http_resopnse_content + content_text
            # send message
            conn.sendall(http_resopnse_content.encode())
    '''
    # if POST method request
    if method == 'POST':
        form = request.split('\r\n')
        idx = form.index('')             # Find the empty line
        entry = form[idx:]               # Main content of the request
        value = entry[-1].split('=')[-1]
        http_resopnse_content = text_content + '\n <p>' + value + '</p>'
    ''' 
    # close connection
    conn.close()

