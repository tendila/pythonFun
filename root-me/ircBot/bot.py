from time import sleep
from math import sqrt
from Irc import *
import base64, zlib, codecs


###########################################################
# Challenge root-me.org => programming => IRC 1, 2, 3, 4  #
#     ~/python3 bot.py            JUST FOR FUN            #
#               MADE IN 12/21 - 410!5                     #
###########################################################

### TODO - what happen if Candy is not responding ?

server = "irc.root-me.org"
channel = "#root-me_challenge"
nickname = "BotdeDam"

irc = IRC()
irc.connect(server, nickname)
irc.joinchan(channel)
sleep(3)
print("Sending request to the bot Candy.. ")
servOutput = irc.sendmsg("!ep4", "Candy")
print(servOutput)

while True:
    if servOutput.find("Candy") != -1:  # If answser is coming from Candy
        index = servOutput.find(nickname +" :") 
        
        answerBot = servOutput[index+10:servOutput.find("\r\n")].strip() 
        
        ###### Challenge 1
        # nb = answerBot.split("/") # int(nb[0]) has the 1st number, int(nb[1]) the second
        # answer = str(round(math.sqrt(int(nb[0])) * int(nb[1]),2))
        
        ###### Challenge 2 - .decode() is use to send the decodedString with the str format but still encoded
        # answer = base64.b64decode(answerBot).decode() #Decode the String receive with base64 encoding 
        
        ###### Challenge 3 -
        # answer = codecs.decode(answerBot,"ROT_13)"); # Decode the String with a ROT-13 encryption
        
        ###### Challenge 4 - 
        answer = zlib.decompress(base64.b64decode(answerBot)).decode()
        
        print(irc.sendmsg("!ep4 -rep " +  answer, "Candy")) #send the result.
        break
    
    elif servOutput.find("PING :") != -1: #If answer = PING, PONG !
        irc.ping()
        