#   15-112 Final Project
#   Online Food Ordering System 
#   Code designed and Submitted by : Johanne Medina
#   Andrew ID: jgmedina
#   Date Created: Nov. 1, 2017 10:00 am
#   Modification History:
#   Start               End
#   11/1 5:44 pm        10:00 pm
#   11/4 10:00 am       3:00 pm
#   11/6 2:18 pm        2:52 pm
#   11/6 8:13 pm        11:05 pm
#   11/7 11:45 am       1:20 pm
#   11/8 9:15 am        12:00 pm
#   11/8 10:35 pm       11:30 pm
#   11/9 10:52 pm       11:45 pm
#   11/10 11:33 pm      12:15 am
#   11/11 8:29 am       12:00 pm
#   11/12 10:15 am      1:20 pm
#   11/12 9:18 pm       11:58 pm
#   11/13 2:16 pm       2:56 pm
#   11/13 5:00 pm       12:09 am
#   11/14 7:24 pm       12:00 am
#   11/15 2:15 pm       2:55 pm
#   11/15 9:33 pm       12:01 am
#   11/17 8:44 pm       11:30 pm
#   11/18 11:15 am      3:00 pm
#   11/20 1:10 pm       2:50 pm
#   11/21 6:12 pm       10:54 pm
#   11/22 7:00 pm       7:56 pm   



from socket import*
from Tkinter import*
from PIL import Image, ImageTk
import tkFileDialog
import os
from time import strftime


#RESTRICTIONS FOR THIS PROJECT
# menu for papa john must only consist of Pizza, Starters, and Drinks and must be named papajmenu.txt
# menu for elevation burger must only consist of Burgers, Sides, and Drinks and must be named ebmenu.txt
# menu for zaatar w zeit must only consist of Teasers, Salads, and Specialty Wraps and must be named zmenu.txt


'''First part is logging in
Only users from the server will be allowed to login with their usernames and
password. Papa John's, Elevation Burger, and Zaatar w Zeit will have their
own accounts which will be treated separately in this code'''



#VALIDATE PERSON LOGIN HERE

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

def StartConnection (IPAddress, PortNumber):
    s = socket(AF_INET,SOCK_STREAM)
    s.connect((IPAddress, PortNumber))
    return s

    
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


'''return a list of users who requested to become your friends
use the same algortihm as getUsers'''
def getRequests(s):
    s.send('@rxrqst \n')
    reply = s.recv(512)
    length = len(reply)
    requests= reply[:length-2]
    
    #split the elements on the @ signs
    g = requests.split('@')
    
    #username requests start on the second index, onwards
    return g[3:]
    
    



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
    
    
    s.send('@%s@sendmsg@%s@%s \n' %(size, friend, message))
    yesorno = s.recv(512)
    if "@ok" in yesorno:
        return True
    else:
        return False

'''takes a socket connection, username, and a filename as input parameters
should read the file and send it in the correct format to the friend
return True if the file was sent correctly
THEY MUST BE FRIENDS!!'''
def sendFile(s, friend, filename):
    #first open and read the file to be able to send it to a friend
    thefile = open(filename)
    fileContent = thefile.read()
    #print fileContent, 'fileContent'
    
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

    
def getMail(s):
    s.send('@rxmsg \n')
    mail = s.recv(8000)
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

            #print newm[i+3], 'mails'
            somefile = open(filename,"w")
            somefile.write(newm[i+3])
            somefile.close()
            #so now all the files the user receives is being saved in the local directory
            #if it doesnt exist,  a new file will be created, if it does, then it will be overwritten and updated
            
    
    #return a tuple with 2 lists, message tuples and file tuples
    return (messagelist, filelist)


def login (s, username, password):
    s.send('LOGIN %s \n' %(username)) 
    rep = s.recv(512) #in the format : LOGIN username CHALLENGE
    
    #put the reply in a list to be able to access the challenge string
    replist = rep.split()
    
    #challenge string is the second index of the list
    CH = replist[2]
    #use this challenge string in the messagedigest
    
    s.send('LOGIN %s %s \n' %(username, messagedigest(password,CH)))
    rep2 = s.recv(512)
    
    if "Login Successful" in rep2:
        return True
    else:
        return False

#GUI TO LOG IN
class LOG:
    def __init__(self,parent=None):
        self.parent=parent
        #self.parent.config(bg="SteelBlue2")
        
        #set default size of the window
        self.size = parent.geometry("500x450")
        #add tite
        self.T = self.parent.title("Welcome")


        #add HBKU picture for the background image using PIL library
        pic = Image.open("bgpic.png")
        bgpic = ImageTk.PhotoImage(pic)
        self.parent.image = bgpic
        self.putinbg = Label(self.parent,image=bgpic)
        self.putinbg.place(x=0, y=0, relwidth=1, relheight=1)

        #label the very top with welcome
        self.greeting = Label(self.parent, text="Welcome to the Student Center's Food Ordering System!")
        self.greeting.config(font=("Arial",18), bg="misty rose", fg="black")
        self.greeting.grid(row=1)
        #label the top with username
        self.un = Label(self.parent, text="Username",bg="misty rose")
        self.un.grid(row=3)        
        
        #add a text box to input the username
        self.addname = Entry(self.parent, highlightbackground="misty rose")
        self.addname.grid(row=4)
        
        #add a label to enter password
        self.pw = Label(self.parent, text="Password", bg="misty rose")
        self.pw.grid(row=5)
        
        #add a text box to input the password
        self.addpass = Entry(self.parent, show="*", highlightbackground="misty rose")
        self.addpass.grid(row=6)
        
        #add ok button
        '''i need the username and password inputted in the text boxes to be passed to the
        login function from the previous homework to be executed after the ok button'''
        self.addButton = Button(self.parent, text='Ok',command= lambda x=self.parent: self.logserver(x))
        #change button color doesnt work on Mac
        self.addButton.config(highlightbackground="misty rose")
        self.addButton.grid(row=10)
        
    def logserver(self,parent):
        '''if the users enters the correct username and password, allow him to go to the next
        window, if not, program should refresh and ask user to try again
        if usernames are papaj, zwz, elevburger, almeera, coffeetime, direct them in the food
        chains window

        if nothing is entered just close it'''

        #check the username if it belongs to a customer or a food chain
        foodchains = ["papaj", "zaatar", "elevation", "almeera"]
        if self.getUN() in foodchains:
            if login(s, str(self.getUN()), str(self.getPW())):
                self.foodchain=Toplevel()
                FC = FoodChain(self.getUN(), self.foodchain)
            else:
                #self.tg = Toplevel()
                #again = self.tryagain(self.tg)
                self.close(parent)
                #self.again = Toplevel()
                #ag = LOG(self.again)
                
        else:
            if login(s, str(self.getUN()), str(self.getPW())):
                self.client = Toplevel()
                cust = Customer(str(self.getUN()),self.client)
            else:
                #try again
                self.tg = Toplevel()
                again = self.tryagain(self.tg)
                #self.close(parent)
                #self.again = Toplevel()
                #ag = LOG(self.again)
                
                
            
    def getUN(self):
        #get the input username from the text box
        self.inputUN = self.addname.get()
        return self.inputUN

    def getPW(self):
        #get input password from the text box
        self.inputPW = self.addpass.get()
        return self.inputPW

    def close(self,parent):
        parent.destroy()
        
        

    #try again pop up window NOT WORKING FOR NOW
    def tryagain(self,parent):
        self.parent = parent
        self.parent.title("Error")
        self.parent.geometry("300x100")
        self.frame = Frame(self.parent, height=60, width=50)
        self.frame.grid()
        self.a = Label(self.parent, text = "Username or password is incorrect.\n Please try again.")
        self.a.grid(row=0, column=0)
        self.ok = Button(self.parent, text="Ok", command = lambda x=self.parent: self.close(x))
        self.ok.grid(row=1, column=0)
        

#------------------------------------  CUSTOMER WINDOW     ------------------------------------    

class Customer:
    def __init__(self,cn,parent=None):
        self.parent = parent
        #get customer's username
        self.cn = cn
        #self.parent.config(bg="mint cream")
        self.t = self.parent.title("Order here")
        #set default size of the window
        self.size = parent.geometry("500x500")

        fpic = Image.open("cute.png")
        cutepic = ImageTk.PhotoImage(fpic)
        self.parent.image = cutepic
        self.putinbgpic = Label(self.parent,image=cutepic)
        self.putinbgpic.place(x=0, y=0, relwidth=1, relheight=1)

        
        #check email for files to get updated menus
        cmails = getMail(s)
        cfiles = cmails[1]
        #once a new file is received, it will be saved and if the filename already exists, it will be overwritten.
    
                
        self.label = Label(self.parent, text = "Welcome! \n Choose where you want to order from:\n")
        self.label.config(font=("Arial", 16))
        self.label.pack()

        #create the button for Papa John's
        self.papaj = Button(self.parent, height = 100, width= 200, command = self.openPJ)
        #button will have the logo of papa johns on it
        pjpic = ImageTk.PhotoImage(file="pj.png")
        self.papaj.image = pjpic
        self.papaj.config(image=pjpic)
        self.papaj.pack()

        #create the button for Elevation Burger
        self.eb = Button(self.parent, height = 100, width=200, command = self.openEB)
        #button will have the logo of elevation burger on it
        ebpic = ImageTk.PhotoImage(file="eb.png")
        self.eb.image = ebpic
        self.eb.config(image=ebpic)
        self.eb.pack()

        #create button for Zaatar w Zeit
        self.zz = Button(self.parent, height=100, width=200, command = self.openZZ)
        #button will have the logo of zaatar w zeit on it
        zzpic = ImageTk.PhotoImage(file="zz.png")
        self.zz.image = zzpic
        self.zz.config(image=zzpic)
        self.zz.pack()


    
    def openPJ(self):
        menuname = "papajmenu.txt"
        #messages and files can only be sent if users are friends
        #the food chains already sent a friend request to all users so check friend requests
        req = getRequests(s)
        if 'papaj' in req:
            acceptFriendRequest(s,'papaj')
        self.parent.destroy()
        self.openpj = Toplevel()
        op = PJ(self.cn,menuname,self.openpj)

    def openZZ(self):
        req = getRequests(s)
        #messages and files can only be sent if users are friends
        #the food chains already sent a friend request to all users so check friend requests
        if 'zaatar' in req:
            acceptFriendRequest(s,'zaatar')
        self.parent.destroy()
        self.openzz = Toplevel()
        op = ZZ(self.cn,self.openzz)

    def openEB(self):
        req = getRequests(s)
        #messages and files can only be sent if users are friends
        #the food chains already sent a friend request to all users so check friend requests
        if 'elevation' in req:
            acceptFriendRequest(s,'elevation')
        self.parent.destroy()
        self.openeb = Toplevel()
        op = EB(self.cn,self.openeb)

    

        

#-----------------------------  PAPA JOHNS  --------------------------------------
class PJ:
    def __init__(self,cn,menuname,parent=None):
        #create a new window that will display the menu of Papa Johns
        self.parent=parent
        #get customer's username
        self.cn = cn
        
        self.parent.geometry("750x450")
        self.t = self.parent.title("Papa John's")


        pjpic = Image.open("pjbg.png")
        bigpjpic = ImageTk.PhotoImage(pjpic)
        self.parent.image = bigpjpic
        self.putinbgpic = Label(self.parent,image=bigpjpic)
        self.putinbgpic.place(x=0, y=0, relwidth=1, relheight=1)

        
        #give the user directions
        bgcolor = "peach puff"
        self.dir = Label(self.parent, text = "Click on each item you want to order:")
        self.dir.config(bg=bgcolor, font=("Arial",16))
        self.dir.grid(row=0,column=1)

        '''list of items in the menu uploaded by the food chain must appear here
        listed in buttons with the price (pictures too if you have time)
        so you must open a file here and translate whats inside to buttons'''
        
        openmenu = open(menuname)
        menu = openmenu.readlines()
        #print menu
        '''create like 3 columns for pizza, starters, and drinks
        if starters in text, put everything under it in that column
        if pizza in text, put everything under it in that column
        if drinks in text, put everything under it in that column'''

        p=menu.index("Pizza\n")
        s=menu.index("Starters\n")
        d=menu.index("Drinks\n")
        
        #Pizza column
        self.piz = Label(self.parent, text="Pizza", bg=bgcolor, font=("Arial",19))
        self.piz.grid(row=1,column=0)
        
        for i in range(p+1,s):
            item = menu[i]
            btn = Button(self.parent, text = item, width=25, command = lambda x=item, y=bgcolor: self.popdeets(x,y))
            btn.config(highlightbackground=bgcolor)
            btn.grid(row=i+2,column=0)
            
        #starters column
        self.st = Label(self.parent, text="Starters", bg=bgcolor, font=("Arial",19))
        self.st.grid(row=1, column=1)
        for j in range(s+1,d):
            item = menu[j]
            btn = Button(self.parent, text= item, width=25, command = lambda x=item, y=bgcolor: self.popdeets(x,y))
            btn.config(highlightbackground=bgcolor)
            btn.grid(row=j-s+2,column=1)

        #drinks column
        self.drinks = Label(self.parent, text="Drinks", bg=bgcolor, font=("Arial",19))
        self.drinks.grid(row=1, column=2)
        for k in range(d+1, len(menu)):
            item = menu[k]
            btn= Button(self.parent, text=item, width=25, command = lambda x=item, y=bgcolor: self.popdeets(x,y))
            btn.config(highlightbackground=bgcolor)
            btn.grid(row=k-d+2, column=2)

        #go to cart
        self.cart = Button(self.parent, text="Go to cart", command= lambda x= menuname: self.opencart(x))
        self.cart.config(highlightbackground=bgcolor)
        self.cart.grid(row=p+s+d, column=2)

    #give the order details of the item to let customer decide whether he wants the item in his cart

    def popdeets(self, item, bgcolor):
        self.deets = Toplevel()
        self.deets.config(bg = bgcolor)
        self.deets.title(item)
        self.deets.geometry("350x150")

        self.f = Frame(self.deets, height=200, width=300, bg = bgcolor)
        self.f.pack()
        #print the item the customer wants to order
        self.order = Label(self.f, text=item, bg=bgcolor)
        self.order.grid(row=0, column=0)
        
        #show the choice of quantity using an entry box
        self.q = Label(self.f, text="Quantity", bg=bgcolor)
        self.q.grid(row=0, column=1)
        self.choice = Entry(self.f, highlightbackground = bgcolor)
        #set default value to 1
        self.choice.insert(END, "1")
        self.choice.grid(row=1, column=1)
        #number = self.choice.get()
        
        #add to cart button
        self.add = Button(self.f, text="Add to Cart", command= lambda x=item, y=self.choice, z=self.deets: self.addtocart(x,y,z))
        self.add.config(highlightbackground = bgcolor)
        self.add.grid(row=5, column=1)
        
        #back button that will lead back to menu
        self.back = Button(self.f, text="Back", command = lambda x=self.deets : self.close(x))
        self.back.config(highlightbackground = bgcolor)
        self.back.grid(row=5, column=0)


    def close(self,parent):
        parent.destroy()

    #pass the menu of the food chain bc it will be needed in the cart
    def opencart(self,m):
        self.cart=Toplevel()
        crt = GoToCart(self.cn,m,'papaj',self.cart)

    def addtocart(self,item, qntity, parent):
        number=qntity.get()
        #print number
        self.close(parent)
        ords = open("ordersof%s.txt" %(self.cn), "a")
        ords.write("%s %s" %(number, item))



#----------------------     ZAATAR W ZEIT   ---------------------------------
class ZZ:
    def __init__(self,cn,parent=None):
        self.parent=parent
        #get customer's username
        self.cn = cn
        self.parent.geometry("750x450")
        self.t = self.parent.title("Zaatar w Zeit")

        zzpic = Image.open("zzbg.png")
        bigzzpic = ImageTk.PhotoImage(zzpic)
        self.parent.image = bigzzpic
        self.putinbgpic = Label(self.parent,image=bigzzpic)
        self.putinbgpic.place(x=0, y=0, relwidth=1, relheight=1)
        
        
        
        bgcolor = 'light yellow'
        #give the user directions
        self.dir = Label(self.parent, text = "Click on each item you want to order:")
        self.dir.config(bg=bgcolor, font=("Arial", 16))
        self.dir.grid(row=0,column=1)

        zzmenu = "zmenu.txt"
        openmenu = open(zzmenu)
        menu = openmenu.readlines()

        t=menu.index("Teasers\n")
        s=menu.index("Salads\n")
        w=menu.index("Specialty Wraps\n")

        #Teasers column
        self.teaser = Label(self.parent, text="Teasers", bg=bgcolor, font=("Arial",19))
        self.teaser.grid(row=1, column=0)

        for i in range(t+1, s):
            item = menu[i]
            btn = Button(self.parent, text=item, width=25,  command = lambda x=item, y=bgcolor: self.popdeets(x,y))
            btn.config(highlightbackground = bgcolor)
            btn.grid(row=i+2, column=0)

        #salads column
        self.salads = Label(self.parent, text="Salads", bg=bgcolor, font=("Arial",19))
        self.salads.grid(row=1, column=1)

        for j in range(s+1, w):
            item = menu[j]
            btn = Button(self.parent, text=item, width=25,  command = lambda x=item, y=bgcolor: self.popdeets(x,y))
            btn.config(highlightbackground = bgcolor)
            btn.grid(row=j-s+2, column=1)

        #wraps column
        self.wrap = Label(self.parent, text="Speacialty Wraps", bg=bgcolor, font=("Arial",19))
        self.wrap.grid(row=1, column=2)

        for k in range(w+1, len(menu)):
            item = menu[k]
            btn = Button(self.parent, text=item, width=25, command = lambda x=item, y=bgcolor: self.popdeets(x,y))
            btn.config(highlightbackground = bgcolor)
            btn.grid(row=k-w+2, column=2)

        #go to cart
        self.cart = Button(self.parent, text="Go to cart", command= lambda x= zzmenu: self.opencart(x))
        self.cart.config(highlightbackground = bgcolor)
        self.cart.grid(row=t+s+w, column=2)

    #give the order details of the item to let customer decide whether he wants the item in his cart
    #put pictures if you can
    def popdeets(self, item, bgcolor):
        self.deets = Toplevel()
        self.deets.config(bg = bgcolor)
        self.deets.title(item)
        self.deets.geometry("350x150")

        self.f = Frame(self.deets, height=200, width=300, bg=bgcolor)
        self.f.pack()
        #print the item the customer wants to order
        self.order = Label(self.f, text=item, bg=bgcolor)
        self.order.grid(row=0, column=0)
        
        #show the choice of quantity using an entry box
        self.q = Label(self.f, text="Quantity", bg=bgcolor)
        self.q.grid(row=0, column=1)
        self.choice = Entry(self.f, highlightbackground = bgcolor)
        #set default value to 1
        self.choice.insert(END, "1")
        self.choice.grid(row=1, column=1)
        #number = self.choice.get()
        
        #add to cart button
        self.add = Button(self.f, text="Add to Cart", command= lambda x=item, y=self.choice, z=self.deets: self.addtocart(x,y,z))
        self.add.config(highlightbackground = bgcolor)
        self.add.grid(row=5, column=1)
        
        #back button that will lead back to menu
        self.back = Button(self.f, text="Back", command = lambda x=self.deets : self.close(x))
        self.back.config(highlightbackground = bgcolor)
        self.back.grid(row=5, column=0)


    def close(self,parent):
        parent.destroy()

    #pass the menu of the food chain bc it will be needed in the cart
    def opencart(self,m):
        self.cart=Toplevel()
        crt = GoToCart(self.cn,m,'zaatar',self.cart)

    def addtocart(self,item, qntity, parent):
        number=qntity.get()
        #print number
        self.close(parent)
        ords = open("ordersof%s.txt" %(self.cn), "a")
        ords.write("%s %s" %(number, item))




#---------------------      ELEVATION BURGER    ---------------------------------
class EB:
    def __init__(self,cn,parent=None):
        self.parent=parent
        #get customer's username
        self.cn = cn
        self.parent.geometry("750x450")
        self.t = self.parent.title("Elevation Burger")

        ebpic = Image.open("elevbg.png")
        bigebpic = ImageTk.PhotoImage(ebpic)
        self.parent.image = bigebpic
        self.putinbgpic = Label(self.parent,image=bigebpic)
        self.putinbgpic.place(x=0, y=0, relwidth=1, relheight=1)

        #self.frameb = Frame(self.parent, height=100, width=100)
        #self.frameb.pack()
        #give the user directions
        bgcolor = "LightBlue1"
        self.dir = Label(self.parent, text = "Click on each item you want to order:")
        self.dir.config(bg=bgcolor, font=("Arial", 16))
        self.dir.grid(row=0,column=1)

        #fixed menu
        ebmenu = "ebmenu.txt"
        openmenu = open(ebmenu)
        menu = openmenu.readlines()

        b=menu.index("Burgers\n")
        s=menu.index("Sides\n")
        d=menu.index("Drinks\n")

        #Burger column
        self.burg = Label(self.parent, text="Burgers", bg=bgcolor, font=("Arial",19))
        self.burg.grid(row=1, column=0)
        #quantity= Label(self.frameb, text="Quantity")
        #quantity.grid(row=1, column=1)

        for i in range(b+1, s):
            item = menu[i]
            btn=Button(self.parent, text=item, width=25, command = lambda x=item, y=bgcolor: self.popdeets(x,y))
            btn.config(highlightbackground=bgcolor)
            btn.grid(row=i+2, column=0)

        #sides column
        self.side = Label(self.parent, text="Sides",bg=bgcolor, font=("Arial",19))
        self.side.grid(row=1, column=1)
        
        for j in range(s+1, d):
            item=menu[j]
            btn = Button(self.parent, text=item, width=25, command = lambda x=item, y=bgcolor: self.popdeets(x,y))
            btn.config(highlightbackground=bgcolor)
            btn.grid(row=j-s+2, column=1)
            #qntty = Text(self.frameb, width=1, height=2)
            #qntty.grid(row=j-s+2, column=3)

        #drinks column
        self.drink = Label(self.parent, text="Drinks",  bg=bgcolor, font=("Arial",19))
        self.drink.grid(row=1, column=2)

        for k in range(d+1, len(menu)):
            item=menu[k]
            btn = Button(self.parent, text=item, width=25, command = lambda x=item, y=bgcolor: self.popdeets(x,y))
            btn.config(highlightbackground=bgcolor)
            btn.grid(row=k-d+2, column=2)
            

        #go to cart
        self.cart = Button(self.parent, text="Go to cart", command= lambda x= ebmenu: self.opencart(x))
        self.cart.config(highlightbackground=bgcolor)
        self.cart.grid(row=b+s+d, column=2)

        

    #give the order details of the item to let customer decide whether he wants the item in his cart
    #put pictures if you can
    def popdeets(self, item, bgcolor):
        self.deets = Toplevel()
        self.deets.config(bg=bgcolor)
        self.deets.title(item)
        self.deets.geometry("350x150")

        self.f = Frame(self.deets, height=200, width=300, bg=bgcolor)
        self.f.pack()
        #print the item the customer wants to order
        self.order = Label(self.f, text=item, bg=bgcolor)
        self.order.grid(row=0, column=0)
        
        #show the choice of quantity using an entry box
        self.q = Label(self.f, text="Quantity", bg=bgcolor)
        self.q.grid(row=0, column=1)
        self.choice = Entry(self.f, highlightbackground = bgcolor)
        #set default quantity to 1
        self.choice.insert(END, "1")
        self.choice.grid(row=1, column=1)
        #number = self.choice.get()
        
        #add to cart button
        self.add = Button(self.f, text="Add to Cart", command= lambda x=item, y=self.choice, z=self.deets: self.addtocart(x,y,z))
        self.add.config(highlightbackground = bgcolor)
        self.add.grid(row=5, column=1)
        
        #back button that will lead back to menu
        self.back = Button(self.f, text="Back", command = lambda x=self.deets : self.close(x))
        self.back.config(highlightbackground = bgcolor)
        self.back.grid(row=5, column=0)


    def close(self,parent):
        parent.destroy()

    #pass the menu of the food chain bc it will be needed in the cart
    def opencart(self,m):
        self.cart=Toplevel()
        crt = GoToCart(self.cn,m,'elevation',self.cart)

    def addtocart(self,item, qntity, parent):
        number=qntity.get()
        #print number
        self.close(parent)
        ords = open("ordersof%s.txt" %(self.cn), "a")
        ords.write("%s %s" %(number, item))



#---------------------------- CHECK OUT CART --------------------------------------------
class GoToCart:
    def __init__(self, cn,menu, resto,parent=None):
        self.parent=parent
        self.parent.config(bg="white")
        #get customer's username
        self.cn = cn

        #text color will be needed later for the text in the cart to match the background
        if resto == "papaj":
            textcolor = "brown1"
        if resto == "elevation":
            textcolor = "RoyalBlue1"
        if resto == "zaatar":
            textcolor = "SpringGreen3"

        
        self.menu = menu
        self.resto=resto
        self.parent.geometry("600x500")
        self.parent.title("Check Out Cart")

       

        self.framec = Frame(self.parent, height=300, width=300)
        self.framec.grid(sticky=W+E+N+S)
       

        #set bg image
        cpic = Image.open("fudz.jpg")
        gtcpic = ImageTk.PhotoImage(cpic)
        self.parent.image = gtcpic
        self.putinbgpic = Label(self.framec,image=gtcpic)
        self.putinbgpic.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.co = Label(self.framec, text="Checkout Counter", fg=textcolor)
        self.co.grid(row=0, column=1)

        self.addtotal=0

        #header
        self.q = Label(self.framec, text = "Quantity", fg=textcolor, bg='white')
        self.q.grid(row=1, column=0, columnspan=6, sticky=W)

        self.i = Label(self.framec, text = "Item", fg=textcolor, bg='white')
        self.i.grid(row=1, column=6, columnspan=20, sticky=W)

        self.p = Label(self.framec, text = "Price", fg=textcolor, bg='white')
        self.p.grid(row=1, column=27, columnspan=6, sticky=W)

        self.tot = Label(self.framec, text="Total", fg=textcolor, bg='white')
        self.tot.grid(row=1, column=33, columnspan=6, sticky=W)
        

        #list all the names of the orders on the left side and the price after it
        #get orders form the clicked food from a file
        ords = open("ordersof%s.txt" %(self.cn))
        self.orders = ords.readlines()
        #print self.orders

        for i in range(len(self.orders)):
            #separate each string by category: Quantity - Item - Price
            oneitem = self.orders[i]

            #remove whitelines
            rem = oneitem.strip()
            nospaces = rem.replace(" ", "")
            #print nospaces

            #quantity is from the first character all the way util the first letter is seen
            self.endofquantity= self.startofitem(nospaces)
            self.qntty = nospaces[:self.endofquantity]
            #print self.qntty, "quantity"

            #price is indicated after the QR
            for j in range(len(nospaces)):         
                if nospaces[j] == "Q":
                    pricestart = j
                    price = nospaces[j:]
                    #print price, "price"

            #the order item is everything in between the quantity and the price
            #but this doesnt have spaces inbetween
            orderitem = nospaces[self.endofquantity:pricestart]
            #print orderitem, "item"

            #Quantity of each item ordered read from the file
            self.Qt = Label(self.framec, text=self.qntty ,fg=textcolor, bg='white')
            self.Qt.grid(row=i+3, column=0, columnspan=6, sticky=W)

            #Items
            self.It = Label(self.framec, text=orderitem, fg=textcolor, bg='white')
            self.It.grid(row=i+3, column=6, columnspan=20, sticky=W)

            #Prices of individual items
            self.Pr = Label(self.framec, text=price, fg=textcolor, bg='white')
            self.Pr.grid(row=i+3, column=27, columnspan=6, sticky=W)

            #Total price of the items based on the quantity
            self.total = Label(self.framec, text="QR"+str(int(self.qntty)*int(price[2:])), fg=textcolor, bg='white')
            self.total.grid(row=i+3, column=33, columnspan=6, sticky=W)

            #add each total price to get the final total price
            self.addtotal = self.addtotal + int(self.qntty)*int(price[2:])

            #add an x button to cancel an order next to each orders
            self.X = Button(self.framec, text="X", height=1, width=1,
                            command = lambda x="ordersof%s.txt"%(self.cn), y=oneitem: self.askifsure(x,y))
            self.X.grid(row=i+3, column=39)

        #final price
        self.Total = Label(self.framec, text= "Total = %s" %(self.addtotal))
        self.Total.config(fg="red", font=("Arial", 22), bg='white')
        self.Total.grid(row=10, column=33, columnspan=6, sticky=W)


        #get the customer details and contact information
        #put it in another frame below the first frame
        
        self.framei = Frame(self.parent, height=300, width=300)
        self.framei.grid(sticky=W+E+N+S)
        #self.framei.grid(row=11, column=0)

        #set bg image
        
        c2pic = Image.open("fudz.jpg")
        gtc2pic = ImageTk.PhotoImage(c2pic)
        self.parent.image2 = gtc2pic
        self.putinbgpic2 = Label(self.framei,image=gtc2pic)
        self.putinbgpic2.place(x=0, y=0, relwidth=1, relheight=1)

        #give instructions
        self.ins = Label(self.framei, text="\n\n\n\n\n Please fill out the following information: \n")
        self.ins.config(fg=textcolor, bg='white')
        self.ins.grid(row=0, column=0, sticky=W)
        #get the name
        self.getname = Label(self.framei, text="Name", fg=textcolor, bg='white')
        self.getname.grid(row=1,column=0, sticky=W)
        self.entername = Entry(self.framei)
        self.entername.grid(row=1, column=1, sticky=W)
        #get the phone number
        self.getnumber = Label(self.framei, text="Phone number", fg=textcolor, bg='white')
        self.getnumber.grid(row=2, column=0, sticky=W)
        self.enternum = Entry(self.framei)
        self.enternum.grid(row=2, column=1,sticky=W)
        #get the location
        self.location = Label(self.framei, text="Location", fg=textcolor, bg='white')
        self.location.grid(row=3, column=0, sticky=W)
        self.enterloc = Entry(self.framei)
        self.enterloc.grid(row=3, column=1, sticky=W)
        #ask for comments or requests
        self.comments = Label(self.framei, text="Comments / Requests", fg=textcolor, bg='white')
        self.comments.grid(row=4, column=0, sticky=W)
        self.entercom = Text(self.framei, height=5, width=20)
        self.entercom.insert('1.0', 'None')
        self.entercom.grid(row=4, column=1, sticky=W)

        #proceed button
        self.pro = Button(self.framei, text="Send my Order!", command= lambda x=resto: self.proceed(x))
        self.pro.grid(row=6, column=3, sticky=E)


        #get the customer information inside the textbox
        #initialize variables in the init definition
        self.cname = " "
        self.cnum = " "
        self.cloc = " "
        self.comm = " "
        

        
    def proceed(self,resto):
        self.cname = self.entername.get()
        self.cnum = self.enternum.get()
        self.cloc = self.enterloc.get()
        self.comm = self.entercom.get("1.0", END)

        #put these in the file
        # i need to be able to read and overwrite at the same time so mode is r+
        thefile = open("ordersof%s.txt" %(self.cn), "r+")
        #save the original content in a list
        addend = thefile.readlines()
        thefile.seek(0)
        #i want the first lines to be the customer information
        timenow = strftime("%Y-%m-%d %H:%M")
        thefile.write("Date: %s \n" %(timenow))
        thefile.write("Customer: %s \n" %(self.cname))
        thefile.write("Phone Number: %s \n" %(self.cnum))
        thefile.write("Location: %s \n" %(self.cloc))
        thefile.write("Comments: %s \n" %(self.comm))
        #print the orders afterwards
        for i in addend:
            thefile.write(i)
        #include the total
        thefile.write("Total = %s" %(self.addtotal))
        thefile.truncate()
        thefile.close()

        #send this file with all the information to the food chain the customer is ordering from
        #so the main function must pass the food chain name
        #sendFile(s, friend, filename) is the format

        self.sendorder = sendFile(s,resto,"ordersof%s.txt" %(self.cn))
        #print self.sendorder
        
        #now delete this file from the local directory so there would be no confusion on the next order made by the same
        #account
        os.remove("ordersof%s.txt" %(self.cn))

        if resto=="papaj":
            r = "Papa Johns"
        if resto=="elevation":
            r = "Elevation Burger"
        if resto=="zaatar":
            r = "Zaatar w Zeit"

        self.weout = Toplevel()
        self.weout.geometry("450x250")
        self.weout.title("Thank you!")
        

        #set bg image
        typic = Image.open("lastbgpic.png")
        tytypic = ImageTk.PhotoImage(typic)
        self.weout.image = tytypic
        self.putinbgpic = Label(self.weout,image=tytypic)
        self.putinbgpic.place(x=0, y=0, relwidth=1, relheight=1)

        self.lastl = Label(self.weout, text="Thank you for shopping at %s! \n Student Center, Education City" %(r))
        self.lastl.config(font=("Arial"))
        self.lastl.grid()
        self.reminder = Label(self.weout, text= "\n\nYour total bill is %s to be paid in cash upon delivery.\n" %(self.addtotal))
        self.lastl.config(font=("Arial"))
        self.reminder.grid()
        self.bye = Button(self.weout, text="Logout", command=self.logout)
        self.bye.grid()

    def logout(self):
        wnd.destroy()
        
        
        

    def startofitem(self, string):
        for s in range(len(string)):
            if string[s].isalpha():
                return s

    def askifsure(self,themenu,cancelthis):
        self.sure = Toplevel()
        self.sure.title("Delete this item?")

        self.frames = Frame(self.sure, height=100, width=100)
        self.frames.pack()
        self.ask = Label(self.frames, text= "Are you sure you want to cancel \n %s from your order?" %(cancelthis))
        self.ask.pack()
        self.yes = Button(self.frames, text="Yes", command = lambda a=self.cn, x=themenu, y=cancelthis, z=self.sure: self.cancel(a,x,y,z))
        self.yes.pack()
        self.no = Button(self.frames,text="No", command = lambda x=self.sure : self.close(x))
        self.no.pack()


    def close(self,parent):
        parent.destroy()


    '''when the x button is clicked, the item will be deleted from the order file and also from the
    cart window right away'''
    def cancel(self,cn,themenu, cancelthis, window):
        self.close(window)
        #get customer's username
        self.cn = cn
        #delete it from the file
        tm = open(themenu, "r+")
        readit = tm.readlines()
        tm.seek(0)
        #if its the line you want to remove, dont write it in the new file
        for i in readit:
            if i != cancelthis:
                tm.write(i)

        tm.truncate()
        tm.close()

        #just close the window and open it right away with the new file to have the updated window
        self.parent.destroy()
        self.openagain=Toplevel()
        #GoToCart(self,menu,resto,parent)
        crt = GoToCart(self.cn,themenu,self.resto,self.openagain)
        
        


    









            

        
# ----------------------------      FOOD CHAINS     --------------------------------------
class FoodChain:
    def __init__(self,name,parent=None):
        self.parent = parent
        self.name = name
        self.parent.geometry("650x550")
        
        if self.name=="papaj":
            self.fc = "Papa John's"
            self.fmen = "papajmenu.txt"
            #initialize bg color
            self.bgcolor="peach puff"
            self.parent.config(bg=self.bgcolor)
            #this is the bg image
            fcpic = Image.open("pjbg.png")
            bigfcpic = ImageTk.PhotoImage(fcpic)
            self.parent.image = bigfcpic
            self.putinbgpic = Label(self.parent,image=bigfcpic)
            self.putinbgpic.place(x=0, y=0, relwidth=1, relheight=1)
            
        elif self.name=="zaatar":
            self.fc="Zaatar w Zeit"
            self.fmen = 'zmenu.txt'
            #initialize bg color
            self.bgcolor="light yellow"
            self.parent.config(bg=self.bgcolor)
            #this is the bg image
            fcpic = Image.open("zzbg.png")
            bigfcpic = ImageTk.PhotoImage(fcpic)
            self.parent.image = bigfcpic
            self.putinbgpic = Label(self.parent,image=bigfcpic)
            self.putinbgpic.place(x=0, y=0, relwidth=1, relheight=1)
            
        elif self.name=="elevation":
            self.fc = "Elevation Burger"
            self.fmen = 'ebmenu.txt'
            #initialize bg color
            self.bgcolor="LightBlue1"
            self.parent.config(bg=self.bgcolor)
            #this is the bg image
            fcpic = Image.open("elevbg.png")
            bigfcpic = ImageTk.PhotoImage(fcpic)
            self.parent.image = bigfcpic
            self.putinbgpic = Label(self.parent,image=bigfcpic)
            self.putinbgpic.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.t = self.parent.title(self.fc)
        
        self.welc = Label(self.parent, text = "Welcome %s!" %(self.fc))
        self.welc.config(bg=self.bgcolor, font=("Arial", 20))
        self.welc.grid(row=0,column=0, sticky=W+E)
        
        self.select  = Label(self.parent, text="Select 'Update Menu' if you wish to update your menu for today")
        self.select.config(bg=self.bgcolor, font=("Arial",16))
        self.select.grid(row=1, column=0)
        

        #update menu
        self.update = Button(self.parent, text="Update menu", command= lambda x=self.name: self.updatemenu(x))
        self.update.config(highlightbackground=self.bgcolor)
        self.update.grid(row=2, column=0, rowspan=6)
        

        #check your orders
        self.see = Label(self.parent, text="Your orders will just pop up!\n")
        self.see.config(bg=self.bgcolor, font=("Arial",16))
        self.see.grid(row=8, column=0, rowspan=2, sticky=W)
        '''just list the orders in this window, so recieve messages, and list them vertically,
        with the customer name, address, phone number, orders'''


        self.getorders()

    '''if update menu was selected, the file uploaded must be sent to all the customers'''

    # SEND THE FILE TO THE USER AND THAT SHOULD AUTOMATICALLY SAVE THAT FILE IT RECEIVED AND OVERWITE THE OLD ONE
    def updatemenu(self, customer):
        self.window = Toplevel()
        self.window.config(bg=self.bgcolor)
        self.window.title("Update menu")
        self.window.geometry("450x250")
        self.frameu = Frame(self.window, height=60, width=80, bg=self.bgcolor)
        self.frameu.grid()

        self.note = Label(self.frameu, text="Browse to upload your updated menu:")
        self.note.config(bg=self.bgcolor, font=("Arial", 18))
        self.note.grid()
        self.here= Entry(self.frameu)
        self.here.config(highlightbackground = self.bgcolor)
        self.here.grid()
        self.browse = Button(self.frameu, text="Browse", command = self.browsemenu)
        self.browse.config(highlightbackground = self.bgcolor)
        self.browse.grid()

        self.ok = Button(self.frameu, text="Ok", command= lambda x=self.here, y=self.window, z=customer : self.overwrite(x,y,z)) 
        self.ok.config(highlightbackground = self.bgcolor)
        self.ok.grid()

    #pop a dialogue box to allow the user to access his files and upload the menu
    def browsemenu(self):
        thefile = tkFileDialog.askopenfilename()
        #dont insert the whole path, just the filename so when it is sent, other computers would be able to read it too
        nameonly = os.path.basename(thefile)
        self.here.insert(0, nameonly)


    '''if the foodchain doesnt want to update their menu, the default and latest menu will be read by the customer,
    else if the foodchain provides a new menu, then overwrite the previous menu with this new menu
    pass to it the entry box so you can get the value inside it '''

    # SEND THE FILE TO THE USER AND THAT SHOULD AUTOMATICALLY SAVE THAT FILE IT RECEIVED AND OVERWITE THE OLD ONE
    # BUT THE CLIENT MUST FIRST UPDATE ALL ITS MENUS BEFORE WORKING
    def overwrite(self, getfilename, pw, customer):
        #get the filename
        self.newmenu= getfilename.get()
        
        # Send File to all customer friends!
        self.cf = getFriends(s)
        #print self.cf
        for i in self.cf:
            self.sendm = sendFile(s,i,self.newmenu)
        

        #now tell the user that menu has successfully been updated
        self.suc = Toplevel()
        self.suc.config(bg=self.bgcolor)
        self.sucframe = Frame(self.suc, bg=self.bgcolor)
        self.sucframe.pack()
        self.suctext = Label(self.sucframe, text = "Menu has successfully been updated!")
        self.suctext.config(bg=self.bgcolor)
        self.suctext.pack()
        self.sucok = Button(self.sucframe, text="Ok", command = lambda x=self.suc, y=pw: self.close(x,y))
        self.sucok.config(bg=self.bgcolor)
        self.sucok.pack()


    def close(self,parent, window):
        parent.destroy()
        window.destroy()


    #------------------------------------ GETTING ORDERS --------------------------------------
    def getorders(self):
        self.parent.after(20000, self.getorders)
        fmails = getMail(s)
        #print fmails

        #the orders will be sent in a file
        #get the files

        #files are in the first index of the getMail function
        fileorders = fmails[1]
        #print fileorders

        #if it received orders
        if fileorders != []:
            #know how many orders from different clients you received
            howmanyf = len(fileorders)

            #go through each order
            for i in range(0,howmanyf):
                #pop up the orders!
                self.poporders = Toplevel()
                
                #get the sender name
                csender = fileorders[i][0]
                #get the filename
                cfname = fileorders[i][1]

                self.poporders.title("Orders of %s" %(csender))
                self.poporders.geometry("300x300")
                self.framer = Frame(self.poporders, bg = self.bgcolor)
                self.framer.pack(fill=BOTH, expand=1)
                
                #open this file
                yourorders= open(cfname)
                readthem = yourorders.readlines()
                
                
                #print each line in the file and show them on the toplevel window
                for o in range(len(readthem)):
                    content = readthem[o]
                    #dont include the \n in each item except for the last line
                    if o == (len(readthem)-1):
                        printthis = content[:len(content)]
                    else:
                        printthis = content[:len(content)-1]
                    #print printthis
                    lstorder = Label(self.framer, text=printthis, justify=LEFT)
                    lstorder.config(bg=self.bgcolor)
                    lstorder.pack()
                   

                #delete this file from the local directory after reading it so as not to fill the client's memory
                os.remove(cfname)

        
        
        

        

        

wnd = Tk()
s= StartConnection("86.36.35.17", 15112)
LG = LOG(wnd)
wnd.mainloop()

   

