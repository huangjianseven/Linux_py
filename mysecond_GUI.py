from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QTextEdit, QMessageBox
from socket import *
from threading import Thread

IP = '127.0.0.1'
PORT = 50000
BUFLEN = 1024

listenSocket = socket(AF_INET,SOCK_STREAM)
listenSocket.bind((IP,PORT))

#def readyToListen():

    #listenSocket.listen(8)
    #textEdit.setPlainText(f'''服务启动成功！！！\n监听在{PORT}端口\n等待客户连接......''')
    
#def stop_Listen():
    #listenSocket.close()
    #textEdit.setPlainText(f'''服务器成功关闭！！！''')

  
    
def deal_With_data(conn,addr) :
    while True:
        recved = conn.recv(BUFLEN)

        if not recved:
            break

        info=recved.decode()
        textEdit.setPlainText(f'''收到对方信息{info}''')

        conn.send(f'服务端收到了信息{info}'.encode())
    
    conn.close()
    textEdit.setPlainText(f'''Client {addr} has left.''')
     
#def deal_With_connect(conn,addr):
    #while True:
        #try:
            #conn,addr = listenSocket.accept()
        #except:
            #break
        #textEdit.setPlainText(f'''Connected by {addr}''')
        
        #t2 = Thread(target=deal_With_data,args=(conn,addr))
        #t2.start()  


app = QApplication([])

window = QMainWindow()
window.resize(500, 400)
window.move(300, 310)
window.setWindowTitle('Message Server')

textEdit = QTextEdit(window)

textEdit.move(10,25)
textEdit.resize(300,350)

button_START = QPushButton('Start Service', window)
button_START.move(380,80)

button_STOP = QPushButton('Stop Service', window)
button_STOP.move(380,140)

window.show()

# button_START.clicked.connect(readyToListen)

listenSocket.listen(8)
textEdit.setPlainText(f'''服务启动成功！！！\n监听在{PORT}端口\n等待客户连接......''')

app.exec_()
conn,addr = listenSocket.accept()
textEdit.setPlainText(f'''Connected by {addr}''')


t1 = Thread(target=deal_With_data,args=(conn,addr))
print('OKOKOK')
t1.start()  

# button_STOP.clicked.connect(stop_Listen)


    

