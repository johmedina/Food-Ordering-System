#    15-112: Principles of Programming and Computer Science
#    HW07 Programming: Implementing a Chat Client
#    Code desgined and written by:  Johanne Medina
#    AndrewID  : jgmedina

#    File Created: 19/10 11:42 am
#    Modification History:
#    Start              End
#    21/10 10:48 am     4:55 pm   
#    21/10 10:30 pm     11:30 pm
#    22/10 11:00 am     1:20 pm
#    22/10 5:30 pm      7:00 pm
#    22/10 9:20 pm      11:06 pm
#    23/10 1:00 pm      1:20 pm
#    23/10 5:15 pm      5:26 pm


from socket import*

########## USE THIS SPACE TO WRITE YOUR HELPER FUNCTIONS ##########

'''return a message which is the concatenation of password and challenge string;
message should be 512 characters long and the format should be password + challenge + 1 + all 0s
and the last two characters should be the length of the password and challenge string combined
take as input the password and the challenge string
this will be called in the messagedigest function which will be used in logging in'''
def conc(PD,CH):
    #get the length of the password
    lp = len(PD)
    #get the length of the challenge string
    lc = len(CH)
    #add the lengths of both
    tl = lp + lc
    #get the total umber of zeros in between
    not0 = lp + lc + len(str(tl)) + 1
    total0 = 512 - not0
    zeros = total0*[0]
    zerostring = ''.join(str(x) for x in zeros)
    
    #join the password, challenge string, zeros, and length in one message
    message = PD + CH + '1' + zerostring + str(tl)
    
    return  message



'''break the message into sixteen 32 character chunks and find the sum of the
ASCII values of each character in the chunk then save it in M  which is a list of
16 integers
this will be called in the messagedigest function which will be used in logging in'''
#split the message into chunks
def chunks(mess):
    while mess:
        yield mess[:32]
        mess = mess[32:]


#find the sum of the ascii values of each character of each chunk and save it in M 
def sumofascii(lst):
    M = []
    for x in lst:
        sumx = 0
        for i in range(len(x)):
            #add all the ascii values of the characters
            sumx = sumx + ord(x[i])

        M.append(sumx)
    
    return M
            
            

#given helper function from the pseudocode
def leftrotate(x,c):
    
    return (x << c)&0xFFFFFFFF | (x >> (32-c)&0x7FFFFFFF>>(32-c))

'''message digest function used to login (following the given pseudocode)
this will porcess each chunk
The result variable calculted is a string that is the final message digets to be used in the login'''
def messagedigest(PD,CH): 
    #input parameters are password and challenge string
    #get the message with the concatation of the password and challenge
    message = conc(PD,CH)
    
    #split it into 16 32-character chunks
    chunky = list(chunks(message))
    #define M to be the sum of the ascii values of the characters 
    M = sumofascii(chunky)
    
    
    #initalize the lists and string
    S = []
    K = []
    abcd= ''
                                    
    for i in range(4):
        S.append(7)
        S.append(12)
        S.append(17)
        S.append(22)

    for j in range(4):
        S.append(5)
        S.append(9)
        S.append(14)
        S.append(20)

    for j in range(4):
        S.append(4)
        S.append(11)
        S.append(16)
        S.append(23)

    for j in range(4):
        S.append(6)
        S.append(10)
        S.append(15)
        S.append(21)

    

    #make the list K from the pseudocode
    #K[0...3]
    K.append(0xd76aa478)
    K.append(0xe8c7b756)
    K.append(0x242070db)
    K.append(0xc1bdceee)
    #K[4...7]
    K.append(0xf57c0faf)
    K.append(0x4787c62a)
    K.append(0xa8304613)
    K.append(0xfd469501)
    #K[8...11]
    K.append(0x698098d8)
    K.append(0x8b44f7af)
    K.append(0xffff5bb1)
    K.append(0x895cd7be)
    #K[12...15]
    K.append(0x6b901122)
    K.append(0xfd987193)
    K.append(0xa679438e)
    K.append(0x49b40821)
    #K[16...19]
    K.append(0xf61e2562)
    K.append(0xc040b340)
    K.append(0x265e5a51)
    K.append(0xe9b6c7aa)
    #K[20...23]
    K.append(0xd62f105d)
    K.append(0x02441453)
    K.append(0xd8a1e681)
    K.append(0xe7d3fbc8)
    #K[24...27]
    K.append(0x21e1cde6)
    K.append(0xc33707d6)
    K.append(0xf4d50d87)
    K.append(0x455a14ed)
    #K[28...31]
    K.append(0xa9e3e905)
    K.append(0xfcefa3f8)
    K.append(0x676f02d9)
    K.append(0x8d2a4c8a)
    #K[32...35]
    K.append(0xfffa3942)
    K.append(0x8771f681)
    K.append(0x6d9d6122)
    K.append(0xfde5380c)
    #K[36...39]
    K.append(0xa4beea44)
    K.append(0x4bdecfa9)
    K.append(0xf6bb4b60)
    K.append(0xbebfbc70)
    #K[40...43]
    K.append(0x289b7ec6)
    K.append(0xeaa127fa)
    K.append(0xd4ef3085)
    K.append(0x04881d05)
    #K[44...47]
    K.append(0xd9d4d039)
    K.append(0xe6db99e5)
    K.append(0x1fa27cf8)
    K.append(0xc4ac5665)
    #K[48...51]
    K.append(0xf4292244)
    K.append(0x432aff97)
    K.append(0xab9423a7)
    K.append(0xfc93a039)
    #K[52...55]
    K.append(0x655b59c3)
    K.append(0x8f0ccc92)
    K.append(0xffeff47d)
    K.append(0x85845dd1)
    #K[56...59]
    K.append(0x6fa87e4f)
    K.append(0xfe2ce6e0)
    K.append(0xa3014314)
    K.append(0x4e0811a1)
    #K[60...63]
    K.append(0xf7537e82)
    K.append(0xbd3af235)
    K.append(0x2ad7d2bb)
    K.append(0xeb86d391)

    
    
    #Initialize variables
    a0 = 0x67452301 #A
    b0 = 0xefcdab89 #B
    c0 = 0x98badcfe #C
    d0 = 0x10325476 #D
    
    A = a0
    B = b0
    C = c0
    D = d0

    #Main loop
    
    for i in range(0,64):
        if 0 <= i and i <= 15:
            F = (B & C) | ((~B) & D)
            F = F & 0xFFFFFFFF
            g = i
        elif 16 <= i and i <= 31:
            F = (D & B) | ((~D) & C)
            F = F & 0xFFFFFFFF
            g = (5*i + 1) % 16
        elif 32 <= i and i <= 47:
            F = B ^ C ^ D
            F = F & 0xFFFFFFFF
            g = (3*i + 5) % 16
        elif 48 <= i  and i <= 63:
            F = C ^ (B | (~D))
            F = F & 0xFFFFFFFF
            g = (7*i) % 16

        dTemp = D
        D = C
        C = B
        B = B + leftrotate((A + F + K[i] + M[g]) , S[i])
        B = B & 0xFFFFFFFF
        A = dTemp

        
        

    #add this chunk's hash to result so far:
    a0 = (a0 + A) & 0xFFFFFFFF
    b0 = (b0 + B) & 0xFFFFFFFF
    c0 = (c0 + C) & 0xFFFFFFFF
    d0 = (d0 + D) & 0xFFFFFFFF

    abcd += str(a0)
    abcd += str(b0)
    abcd += str(c0)
    abcd += str(d0)

    
    return abcd
                                


########## FILL IN THE FUNCTIONS TO IMPLEMENT THE CLIENT ##########
def StartConnection (IPAddress, PortNumber):
    s = socket(AF_INET,SOCK_STREAM)
    s.connect((IPAddress, PortNumber))
    return s

def login (s, username, password):
    s.send('LOGIN %s \n' %(username)) 
    rep = s.recv(512) #in the format : LOGIN username CHALLENGE
    print rep
    #put the reply in a list to be able to access the challenge string
    replist = rep.split()
    #challenge string is the second index of the list
    CH = replist[2]
    #use this challenge string in the messagedigest
    
    s.send('LOGIN %s %s \n' %(username, messagedigest(password,CH)))
    rep2 = s.recv(512)
    print rep2
    if "Login Successful" in rep2:
        return True
    else:
        return False
        


    
    
'''takes a socket connection as input parameter and returns a list of
active users'''
def getUsers(s):
    s.send('@users \n')
    u = s.recv(1087) #1087 since the size returned by the server which allows me to read everything
    #remove the \r\n
    length = len(u)
    users = u[:length-2]

    
    #split the reply on the @ signs
    sp = users.split('@')


    #return the list of users which comes on the third index of the list and until the end
    return sp[4:]
    

#print getUsers(socket)


'''return a list of users who you have as friends, same algorithm as in getUsers'''
def getFriends(s):
    s.send('@friends \n')
    friends = s.recv(512)
    #remove the \r\n
    length = len(friends)
    remove = friends[:length-2]
    f = remove.split('@')
    

    #the list of friends also appear on the third index and onwards
    return f[4:]



'''Send a friend request. Take a socket connection and a username as input parameters
size must be determined first which is the size of the string being sent from beginning to end
including the size field. Size should always be 5 digits long(not including null terminator)
return True if successful, false if not'''
def sendFriendRequest(s, friend):
    #get the size of the friend username
    fsize = len(friend)
    #calculate the size of the whole string and make sure the size is 5 digits long
    #partial size  = len of size + len of request + @ + len of friend + @ + fsize +@
    psize = 6 + 8 + 7 + fsize +1
    not0 = len(str(psize))
    total0 = 5 - not0
    #add the number of leading zeros
    add0 = total0*[0]
    zeros = ''.join(str(x) for x in add0)
    size = str(zeros) + str(psize)
    
    
    s.send('@%s@request@friend@%s \n' %(size,friend))
    yesorno = s.recv(512)

    if "@ok" in yesorno:
        return True
    return False


'''Accept friend request with the same algorithm as sending one
return True if successful, False if not'''
def acceptFriendRequest(s, friend):
    #get the size of the friend username
    fsize = len(friend)
    #calculate the size of the whole string and make sure the size is 5 digits long
    #partial size  = len of size + len of accept + @ + len of friend + @ + fsize +@
    psize = 6 + 7 + 7 + fsize + 1
    not0 = len(str(psize))
    total0 = 5 - not0
    #add the number of leading zeros
    add0 = total0*[0]
    zeros = ''.join(str(x) for x in add0)
    size = str(zeros) + str(psize)
    
    s.send('@%s@accept@friend@%s \n' %(size,friend))
    yesorno = s.recv(512)
    
    if "@ok" in yesorno:
        return True
    else:
        return False

'''take a socket connection, username, and string as input parameters
return True if the message is sent successfully
message input must be a string'''
def sendMessage(s, friend, message):
    #get the size of the friend username which already includes @
    fsize = len(friend) + 1
    #get the size of the message string not including @
    msize = len(message)
    #partialsize  = len of size (6 including @) + @sendmsg + fsize + msize
    psize = 6 +8 + fsize + msize + 1
    #get the number of leading zeros to make the size be 5 digits long
    not0 = len(str(psize))
    total0 = 5 - not0
    add0 = total0*[0]
    zeros = ''.join(str(x) for x in add0)
    size = str(zeros) + str(psize)
    print size, "sizE"
    print friend, "friend"
    print message, "message"
    
    
    
    s.send('@%s@sendmsg@%s@%s \n' %(size, friend, message))
    yesorno = s.recv(512)
    if "@ok" in yesorno:
        return True
    else:
        return False

'''takes a socket connection, username, and a filename as input parameters
should read the file and send it in the correct format to the friend
return True if the file was sent correctly'''
def sendFile(s, friend, filename):
    #first open and read the file to be able to send it to a friend
    thefile = open(filename)
    fileContent = thefile.read()
    print fileContent
    
    #get size of the fileContent, add 1 for the @ sign
    fcsize = len(fileContent) + 1
    #get the size of the friend username add 1 for @
    fsize = len(friend) + 1
    #get the size of the filename, add  1 for the @ sign
    fnsize = len(filename) + 1
    #partial size = 6 (for the size) + 9 + fsize + fnsize + fcsize
    psize = 6 + 9 + fsize + fnsize + fcsize
    

    #get the number of leading zeros to make the size be 5 digits long
    not0 = len(str(psize))
    total0 = 5 - not0
    add0 = total0*[0]
    zeros = ''.join(str(x) for x in add0)
    size = str(zeros) + str(psize)
    
    
    
    s.send("@%s@sendfile@%s@%s@%s \n" %(size, friend, filename, fileContent))
    yesorno = s.recv(512)

    if "@ok" in yesorno:
        return True
    else:
        return False 

'''return a list of users who requested to become your friends
use the same algortihm as getUsers'''
def getRequests(s):
    s.send('@rxrqst \n')
    reply = s.recv(512)
    length = len(reply)
    requests= reply[:length-2]
    print requests

    #split the elements on the @ signs
    g = requests.split('@')


    #username requests start on the second index, onwards
    return g[3:]
    
    
    

''' return a tuple with two lists: list of tuples (user, message) representing
all received messages and a list of tuples (user, filename) representing
all files received. Should also save all the files to a local directory
under the filename it got'''
def getMail(s):
    s.send('@rxmsg \n')
    mail = s.recv(1024)
    #newm = []
    newm = mail.split('@')
    
    messagelist = []
    filelist = []
    for i in range(len(newm)):
        if newm[i] == "msg":
            #creat a tuple (user, message) representing all received messages
            tupi = (newm[i+1],newm[i+2])
            #add the tuples in a list of messages 
            messagelist.append(tupi)

        elif newm[i] == "file":
            #create a tuple (user, filename) representing all files received
            fili = (newm[i+1],newm[i+2])
            #add the tuples in a list of files
            filelist.append(fili)
            
            '''save all the files that it receives in a local directory under the filename it got
            it will save in the same directory where you are running this python program
            file name is listed with an @ sign in the beggining, so remove that'''
            name = newm[i+2]
            filename = name
            print newm[i+3:]
            
            somefile = open(filename,"w")
            somefile.write(newm[i+3])
            somefile.close()
    
    
    #return a tuple with 2 lists, message tuples and file tuples
    return (messagelist, filelist)

########## CLIENT PROGRAM HELPER FUNCTIONS: CHANGE ONLY IF NEEDED ##########
def PrintUsage(s):
    print ">> Menu:"
    print "     Menu            Shows a Menu of acceptable commands"
    print "     Users           List all active users"
    print "     Friends         Show your current friends"
    print "     Add Friend      Send another friend a friend request"
    print "     Send Message    Send a message to a friend"
    print "     Send File       Send a file to a friend"
    print "     Requests        See your friend requests"
    print "     Messages        See the new messages you recieved"
    print "     Score           Print your current score"
    print "     Exit            Exits the chat client"
    
def ShowUsers(s):
    Users = getUsers(s)
    if Users == []:
        print ">> There are currently no active users"
    else:
        print ">> Active users:"
        for u in Users:
            print "     " + u
    
def ShowFriends(s):
    Friends = getFriends(s)
    if Friends == []:
        print ">> You currently have no friends"
    else:
        print ">> Your friends:"
        for f in Friends:
            print "     " + f
    
def AddFriend(s):
    friend = raw_input("Please insert the username of the user you would like to add as a friend: ")
    if sendFriendRequest(s, friend): print friend, "added succesfully"
    else: "Error adding " + friend + ". Please try again."
    
def AcceptFriend(s):
    friend = raw_input("Please insert the username of the user you would like to accept as a friend: ")
    if acceptFriendRequest(s, friend): print "Request from " + friend + " accepted succesfully"
    else: "Error accepting request from " + friend + ". Please try again." 
    
def SendMessage(s):
    friend = raw_input("Please insert the username of the friend you would like to message: ")
    message = raw_input("Please insert the message that you would like to send: ")
    if friend in getFriends(s):
        if sendMessage(s, friend, message): print "Mesage sent to " + friend + " succesfully"
        else: "Error sending message to " + friend + ". Please try again."
    else: print friend, "is not a Friend. You must add them as a friend before you can message them."

def SendFile(s):
    friend = raw_input("Please insert the username of the friend you would like to mail a file: ")
    filename = raw_input("Please insert the name of the file you'd like to send: ")
    if friend in getFriends(s):
        if sendFile(s, friend, filename): print "File sent to " + friend + " succesfully"
        else: "Error sending file to " + friend + ". Please try again."
    else: print friend, "is not a Friend. You must add them as a friend before you can send them a file."

    
def ShowRequests(s):
    Requests = getRequests(s)
    if Requests == []:
        print ">> You currently have no friend requests"
    else:
        print ">> The following users have asked to be your friends:"
        for r in Requests:
            print "     " + r
    
def ShowMessages(s):
    (Messages, Files) = getMail(s)
    if Messages == []:
        print ">> You have no new messages"
    else:
        print ">> You have recieved the following messages:"
        for (u, m) in Messages:
            print "     " + u + " says: " + m
    if Files == []:
        print ">> You have no new files"
    else:
       print ">> You also recieved the following Users:"
       for (u, f) in Files:
            print "File " + f +" recieved from: " + u + " and downloaded successfully."

def ShowScore(s):
    s.send("@getscore\n")
    data = s.recv(512)
    score = data.split('@')
    print "Your Score:", score[2]
    print "task 1", score[3]
    print "task 2", score[4]
    print "task 3", score[5]
    print "task 4", score[6]
    print "task 5", score[7]
    print "task 6", score[8]
    

##########  MAIN CODE, CHANGE ONLY IF ABSOLUTELY NECCESSARY  ##########
# Connect to the server at IP Address 86.36.35.17
# and port number 15112
socket = StartConnection("86.36.35.17", 15112)


# Ask the user for their login name and password
username = raw_input(">> Login as: ")
if ("Exit" == username) : exit()

password = raw_input(">> Password: ")
if ("Exit" == password) : exit()

# Run authentication
# Ask for username and password again if incorrect
while not login (socket, username, password):
    print ">> Incorrect Username/Password Combination!"
    print ">> Please try again, or type 'Exit' to close the application."
    username = raw_input(">> Login as: ")
    if ("Exit" == username) : exit()
    password = raw_input(">> Password: ")
    if ("Exit" == password) : exit()

# Now user is logged in


'''
allusers = getUsers(socket)
frands = getFriends(socket)
for i in allusers:
    if i not in frands:
        sendFriendRequest(socket, i)




mails=getMail(socket)
while mails==[]:
    getMail(socket)

messtuple=mails[0]
sender=messtuple[0][0]
mesg=messtuple[0][1]
if mesg == "What is your menu today?":
    sentit = sendFile(s,sender, "papajmenu.txt")
    print sendFile(s,sender, "papajmenu.txt")


'''





# Set up your commands options
menu = {
        "Menu": PrintUsage,
        "Users" : ShowUsers,
        "Friends": ShowFriends,
        "Add Friend": AddFriend,
        "Accept Friend": AcceptFriend,
        "Send Message": SendMessage,
        "Send File": SendFile,
        "Requests": ShowRequests,
        "Messages": ShowMessages,
        "Score": ShowScore
    }

# Prompt the user for a command
print ">> Welcome", username, "!"
print ">> Insert command or type Menu to see a list of possible commands"
prompt = "[" + username + "]>>"
command = raw_input(prompt)

while (command != "Exit"):
    if not command in menu.keys():
        print ">> Unidentified command " + command + ". Please insert valid command or type Menu to see a list of possible commands."
        prompt = "[" + username + "]>>"
        command = raw_input(prompt)
    else:
        menu[command](socket)
        command = raw_input(prompt)

