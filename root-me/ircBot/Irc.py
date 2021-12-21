import socket
from time import sleep

class IRC:

    irc = socket.socket()
  
    def __init__(self):  
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    
    def connect(self, server, botnick):
        print("Connecting to the server : " + server)
        self.irc.connect((server, 6667)) # Here we connect to the server using the port 6667
        self.irc.send(bytes("USER "+ botnick +" "+ botnick +" "+ botnick + " " + botnick + "\n", "UTF-8")) #W Filling out a form with this line and saying to set all the fields to the bot nickname.
        self.irc.send(bytes("NICK "+ botnick +"\n", "UTF-8")) # assign the nick to the bot
        print("Auth sent, waiting an answer from the server..")
        sleep(3)
        print(self.irc.recv(10000).decode("UTF-8").strip('nr'))
        
    def joinchan(self, channel): # join channel  
        self.irc.send(bytes("JOIN "+ channel +"\n", "UTF-8"))
        print(self.irc.recv(10000).decode("UTF-8").strip('nr'))
    
    def sendmsg(self, msg, target): # sends messages to the target.  
        self.irc.send(bytes("PRIVMSG " + target + " " + msg +"\n", "UTF-8"))
        sleep(1)
        response=""
        try:
            response = self.irc.recv(10000).decode("UTF-8").strip('nr')
        except Exception as e:
            print(e)  
        return response
    
    def ping(self): # respond to server Pings.  
        self.irc.send(bytes("PONG :pingisn", "UTF-8"))
        print("PONG")