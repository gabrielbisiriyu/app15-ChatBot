from PyQt6.QtWidgets import QApplication, QMainWindow,QTextEdit,QLineEdit,QPushButton
import sys
from backend import ChatBot
import threading

class ChatBotWindow(QMainWindow):
    def __init__(self):
        super().__init__() 
        self.setMinimumSize(620,400) 

        # instantiating the ChatBox class we created in backend.py
        self.chatbot = ChatBot()

        # Add Chat Area widget 
        self.chat_area=QTextEdit(self)
        self.chat_area.setGeometry(10,10,480,320)# !0px from the left, !0px from the top,480 width, 320 length
        self.chat_area.setReadOnly(True)
        # Add input widget 
        self.input_field=QLineEdit(self)
        self.input_field.setGeometry(10,340,480,50) 
        self.input_field.returnPressed.connect(self.send) # This activates the Enter key on the nkeyboard as send  button
        # Add  button
        self.button=QPushButton("Send",self)
        self.button.clicked.connect(self.send)
        self.button.setGeometry(500,340,100,50)
        
        self.show()


    def send(self):
        user_input=self.input_field.text().strip()  
        self.chat_area.append(f"<p style='color:#333333'>Me: {user_input}</p>")   
        self.input_field.clear()
        thread=threading.Thread(target=self.get_txt_response,args=(user_input,))
        thread.start()   
    
    def get_txt_response(self,user_input):
        response=self.chatbot.get_response(user_input)
        self.chat_area.append(f"<p style='color:#333333; background-color: #E9E9E9'>Bot: {response}</p>")
        

app=QApplication(sys.argv) 
main_window=ChatBotWindow() 
app.exit(app.exec())