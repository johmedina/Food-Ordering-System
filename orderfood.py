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
#   11/13 2:16 pm


from socket import*
from Tkinter import*
from PIL import Image, ImageTk
import time

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
return True if the file was sent correctly'''
def sendFile(s, friend, filename):
    #first open and read the file to be able to send it to a friend
    thefile = open(filename)
    fileContent = thefile.read()
    
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
    mail = s.recv(512)
    newm = []
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
        self.frame = Frame(self.parent,height=60,width=60)
        self.frame.pack()
        #set default size of the window
        self.size = parent.geometry("450x200")
        #add tite
        self.T = self.parent.title("Welcome")
        #add HBKU picture for the background image using PIL library
        '''pic = Image.open("bgpic.bmp")
        bgpic = ImageTk.PhotoImage(pic)
        self.putinbg = Label(image=bgpic)
        self.picture = pic #keep a reference
        self.putinbg.pack()'''


        
        #label the very top with welcome
        self.greeting = Label(self.frame, text="Welcome to the Student Center's Food Ordering System")
        self.greeting.pack()
        #label the top with username
        self.un = Label(self.frame, text="Username")
        self.un.pack()
        
        
        #add a text box to input the username
        self.addname = Entry(self.frame)
        self.addname.pack()
        
        #add a label to enter password
        self.pw = Label(self.frame, text="Password")
        self.pw.pack()
        
        #add a text box to input the password
        self.addpass = Entry(self.frame, show="*")
        self.addpass.pack()
        
        #add ok button
        '''i need the username and password inputted in the text boxes to be passed to the
        login function from the previous homework to be executed after the ok button'''
        self.addButton = Button(self.frame, text='Ok',command= lambda x=self.parent: self.logserver(x))
        self.addButton.pack()
        
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
                cust = Customer(self.client)
            else:
                #try again
                #self.tg = Toplevel()
                #again = self.tryagain(self.tg)
                self.close(parent)
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
        self.frame.pack()
        self.a = Label(self.parent, text = "Username or password is incorrect.\n Please try again.")
        self.a.grid(row=0, column=0)
        self.ok = Button(self.parent, text="Ok", command = lambda x=self.frame: self.close(x))
        self.ok.grid(row=1, column=0)
        

#-------------------------  CUSTOMER WINDOW     ------------------------------------    

class Customer:
    def __init__(self, parent=None):
        self.parent = parent
        self.t = self.parent.title("Order here")
        #set default size of the window
        self.size = parent.geometry("500x500")
        #create the frame
        self.framec = Frame(parent, height=400, width=400)
        self.framec.pack()

        self.label = Label(self.framec, text = "Welcome! \n Choose where you want to order from:")
        self.label.pack()

        #create the button for Papa John's
        self.papaj = Button(self.framec, height = 100, width= 200, command = self.openPJ)
        #button will have the logo of papa johns on it
        pjpic = ImageTk.PhotoImage(file="pj.png")
        self.papaj.image = pjpic
        self.papaj.config(image=pjpic)
        self.papaj.pack()

        #create the button for Elevation Burger
        self.eb = Button(self.framec, height = 100, width=200, command = self.openEB)
        #button will have the logo of elevation burger on it
        ebpic = ImageTk.PhotoImage(file="eb.png")
        self.eb.image = ebpic
        self.eb.config(image=ebpic)
        self.eb.pack()

        #create button for Zaatar w Zeit
        self.zz = Button(self.framec, height=100, width=200, command = self.openZZ)
        #button will have the logo of zaatar w zeit on it
        zzpic = ImageTk.PhotoImage(file="zz.png")
        self.zz.image = zzpic
        self.zz.config(image=zzpic)
        self.zz.pack()


    '''if papa johns was chosen, send a message to papa johns asking for the menu
    once papa johns receieves this message it will automatically send a file, you must get this file
    right away and process it'''
    def openPJ(self):
        askformenu = sendMessage(s,'papaj', 'What is your menu today?')
        time.sleep(3)
        default = "papajmenu.txt"
        menuname = self.checkfile(default) #ERROR HERE 
        self.parent.destroy()
        self.openpj = Toplevel()
        op = PJ(menuname,self.openpj)

    def openZZ(self):
        self.parent.destroy()
        self.openzz = Toplevel()
        op = ZZ(self.openzz)

    def openEB(self):
        self.parent.destroy()
        self.openeb = Toplevel()
        op = EB(self.openeb)

    
    '''once the button is pressed, check mail for the reply from the message the user sent asking for
    the menu, pass in mname which is the default menu for a specific food chain'''
    def checkfile(self, mname):
        mails = getMail(s)
        #print mails
        #only check for the files recieved, dont care abt the messages
        #[user, filenmame, filecontent]

        #if there are no files received then just send the default menu
        if mails[1] == []:
            return mname
        
        '''the user will always only receive one mail at a time! getmail automaticall saves the files
        it receives in the local directory '''
        messtuple = mails[1]
        sender = messtuple[1][0] #index out of range??????
        #get filename
        name = messtuple[1][1]
        content = messtuple[1][2]

        return name
        

        

#-----------------------------  PAPA JOHNS  --------------------------------------
class PJ:
    def __init__(self,menuname,parent=None):
        #create a new window that will display the menu of Papa Johns
        self.parent=parent
        self.parent.geometry("700x400")
        self.t = self.parent.title("Papa John's")

        self.framepj = Frame(self.parent,height=100, width=100)
        self.framepj.pack()
        #give the user directions
        self.dir = Label(self.framepj, text = "Click on each item you want to order:")
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
        self.piz = Label(self.framepj, text="Pizza")
        self.piz.grid(row=1,column=0)
        
        for i in range(p+1,s):
            item = menu[i]
            btn = Button(self.framepj, text = menu[i], width=25, command = lambda x=item: self.popdeets(x))
            btn.grid(row=i+2,column=0)
            
        #starters column
        self.st = Label(self.framepj, text="Starters")
        self.st.grid(row=1, column=1)
        for j in range(s+1,d):
            item = menu[j]
            btn = Button(self.framepj, text= menu[j], width=25, command = lambda x=item: self.popdeets(x))
            btn.grid(row=j-s+2,column=1)

        #drinks column
        self.drinks = Label(self.framepj, text="Drinks")
        self.drinks.grid(row=1, column=2)
        for k in range(d+1, len(menu)):
            item = menu[k]
            btn= Button(self.framepj, text=menu[k], width=25, command = lambda x=item: self.popdeets(x))
            btn.grid(row=k-d+2, column=2)

        #go to cart
        self.cart = Button(self.framepj, text="Go to cart", command= lambda x= menuname: self.opencart(x))
        self.cart.grid(row=p+s+d, column=2)

    #give the order details of the item to let customer decide whether he wants the item in his cart
    #put pictures if you can
    def popdeets(self, item):
        self.deets = Toplevel()
        self.deets.title(item)
        self.deets.geometry("350x150")

        self.f = Frame(self.deets, height=200, width=300)
        self.f.pack()
        #print the item the customer wants to order
        self.order = Label(self.f, text=item)
        self.order.grid(row=0, column=0)
        
        #show the choice of quantity using an entry box
        self.q = Label(self.f, text="Quantity")
        self.q.grid(row=0, column=1)
        self.choice = Entry(self.f)
        #set default value to 1
        self.choice.insert(END, "1")
        self.choice.grid(row=1, column=1)
        #number = self.choice.get()
        
        #add to cart button
        self.add = Button(self.f, text="Add to Cart", command= lambda x=item, y=self.choice, z=self.deets: self.addtocart(x,y,z))
        self.add.grid(row=5, column=1)
        
        #back button that will lead back to menu
        self.back = Button(self.f, text="Back", command = lambda x=self.deets : self.close(x))
        self.back.grid(row=5, column=0)


    def close(self,parent):
        parent.destroy()

    #pass the menu of the food chain bc it will be needed in the cart
    def opencart(self,m):
        self.cart=Toplevel()
        crt = GoToCart(m,'papaj',self.cart)

    def addtocart(self,item, qntity, parent):
        number=qntity.get()
        #print number
        self.close(parent)
        ords = open("orders.txt", "a")
        ords.write("%s %s" %(number, item))



#----------------------     ZAATAR W ZEIT   ---------------------------------
class ZZ:
    def __init__(self,parent=None):
        self.parent=parent
        self.parent.geometry("700x400")
        self.t = self.parent.title("Zaatar w Zeit")

        self.framezz = Frame(self.parent,height=100, width=100)
        self.framezz.pack()

        #set the background image to the logo of the food chain NOT WORKING
        bgpic = PhotoImage(file="zz.gif")
        bglabel = Label(image=bgpic)
        bglabel.place(x=0, y=0, relwidth=1, relheight=1)

        
        #give the user directions
        self.dir = Label(self.framezz, text = "Click on each item you want to order:")
        self.dir.grid(row=0,column=1)

        zzmenu = "zmenu.txt"
        openmenu = open(zzmenu)
        menu = openmenu.readlines()

        t=menu.index("Teasers\n")
        s=menu.index("Salads\n")
        w=menu.index("Specialty Wraps\n")

        #Teasers column
        self.teaser = Label(self.framezz, text="Teasers")
        self.teaser.grid(row=1, column=0)

        for i in range(t+1, s):
            item = menu[i]
            btn = Button(self.framezz, text=menu[i], width=25,  command = lambda x=item: self.popdeets(x))
            btn.grid(row=i+2, column=0)

        #salads column
        self.salads = Label(self.framezz, text="Salads")
        self.salads.grid(row=1, column=1)

        for j in range(s+1, w):
            item = menu[j]
            btn = Button(self.framezz, text=menu[j], width=25,  command = lambda x=item: self.popdeets(x))
            btn.grid(row=j-s+2, column=1)

        #wraps column
        self.wrap = Label(self.framezz, text="Speacialty Wraps")
        self.wrap.grid(row=1, column=2)

        for k in range(w+1, len(menu)):
            item = menu[k]
            btn = Button(self.framezz, text=menu[k], width=25, command = lambda x=item: self.popdeets(x))
            btn.grid(row=k-w+2, column=2)

        #go to cart
        self.cart = Button(self.framezz, text="Go to cart", command= lambda x= zzmenu: self.opencart(x))
        self.cart.grid(row=t+s+w, column=2)

    #give the order details of the item to let customer decide whether he wants the item in his cart
    #put pictures if you can
    def popdeets(self, item):
        self.deets = Toplevel()
        self.deets.title(item)
        self.deets.geometry("350x150")

        self.f = Frame(self.deets, height=200, width=300)
        self.f.pack()
        #print the item the customer wants to order
        self.order = Label(self.f, text=item)
        self.order.grid(row=0, column=0)
        
        #show the choice of quantity using an entry box
        self.q = Label(self.f, text="Quantity")
        self.q.grid(row=0, column=1)
        self.choice = Entry(self.f)
        #set default value to 1
        self.choice.insert(END, "1")
        self.choice.grid(row=1, column=1)
        #number = self.choice.get()
        
        #add to cart button
        self.add = Button(self.f, text="Add to Cart", command= lambda x=item, y=self.choice, z=self.deets: self.addtocart(x,y,z))
        self.add.grid(row=5, column=1)
        
        #back button that will lead back to menu
        self.back = Button(self.f, text="Back", command = lambda x=self.deets : self.close(x))
        self.back.grid(row=5, column=0)


    def close(self,parent):
        parent.destroy()

    #pass the menu of the food chain bc it will be needed in the cart
    def opencart(self,m):
        self.cart=Toplevel()
        crt = GoToCart(m,'zaatar',self.cart)

    def addtocart(self,item, qntity, parent):
        number=qntity.get()
        #print number
        self.close(parent)
        ords = open("orders.txt", "a")
        ords.write("%s %s" %(number, item))




#---------------------      ELEVATION BURGER    ---------------------------------
class EB:
    def __init__(self,parent=None):
        self.parent=parent
        self.parent.geometry("800x400")
        self.t = self.parent.title("Elevation Burger")

        self.frameb = Frame(self.parent, height=100, width=100)
        self.frameb.pack()
        #give the user directions
        self.dir = Label(self.frameb, text = "Click on each item you want to order:")
        self.dir.grid(row=0,column=1)

        #fixed menu
        ebmenu = "ebmenu.txt"
        openmenu = open(ebmenu)
        menu = openmenu.readlines()

        b=menu.index("Burgers\n")
        s=menu.index("Sides\n")
        d=menu.index("Drinks\n")

        #Burger column
        self.burg = Label(self.frameb, text="Burgers")
        self.burg.grid(row=1, column=0)
        #quantity= Label(self.frameb, text="Quantity")
        #quantity.grid(row=1, column=1)

        for i in range(b+1, s):
            item = menu[i]
            btn=Button(self.frameb, text=item, width=25, command = lambda x=item: self.popdeets(x))
            btn.grid(row=i+2, column=0)

        #sides column
        self.side = Label(self.frameb, text="Sides")
        self.side.grid(row=1, column=1)
        
        for j in range(s+1, d):
            item=menu[j]
            btn = Button(self.frameb, text=item, width=25, command = lambda x=item: self.popdeets(x))
            btn.grid(row=j-s+2, column=1)
            #qntty = Text(self.frameb, width=1, height=2)
            #qntty.grid(row=j-s+2, column=3)

        #drinks column
        self.drink = Label(self.frameb, text="Drinks")
        self.drink.grid(row=1, column=2)

        for k in range(d+1, len(menu)):
            item=menu[k]
            btn = Button(self.frameb, text=item, width=25, command = lambda x=item: self.popdeets(x))
            btn.grid(row=k-d+2, column=2)
            #qntty = Text(self.frameb, width=1, height=2)
            #qntty.grid(row=k-d+2, column=5)

        #go to cart
        self.cart = Button(self.frameb, text="Go to cart", command= lambda x= ebmenu: self.opencart(x))
        self.cart.grid(row=b+s+d, column=2)

        

    #give the order details of the item to let customer decide whether he wants the item in his cart
    #put pictures if you can
    def popdeets(self, item):
        self.deets = Toplevel()
        self.deets.title(item)
        self.deets.geometry("350x150")

        self.f = Frame(self.deets, height=200, width=300)
        self.f.pack()
        #print the item the customer wants to order
        self.order = Label(self.f, text=item)
        self.order.grid(row=0, column=0)
        
        #show the choice of quantity using an entry box
        self.q = Label(self.f, text="Quantity")
        self.q.grid(row=0, column=1)
        self.choice = Entry(self.f)
        #set default quantity to 1
        self.choice.insert(END, "1")
        self.choice.grid(row=1, column=1)
        #number = self.choice.get()
        
        #add to cart button
        self.add = Button(self.f, text="Add to Cart", command= lambda x=item, y=self.choice, z=self.deets: self.addtocart(x,y,z))
        self.add.grid(row=5, column=1)
        
        #back button that will lead back to menu
        self.back = Button(self.f, text="Back", command = lambda x=self.deets : self.close(x))
        self.back.grid(row=5, column=0)


    def close(self,parent):
        parent.destroy()

    #pass the menu of the food chain bc it will be needed in the cart
    def opencart(self,m):
        self.cart=Toplevel()
        crt = GoToCart(m,'elevation',self.cart)

    def addtocart(self,item, qntity, parent):
        number=qntity.get()
        #print number
        self.close(parent)
        ords = open("orders.txt", "a")
        ords.write("%s %s" %(number, item))



#---------------------------- CHECK OUT CART --------------------------------------------
class GoToCart:
    def __init__(self, menu, resto,parent=None):
        self.parent=parent
        self.menu = menu
        self.resto=resto
        self.parent.geometry("600x500")
        self.parent.title("Check Out Cart")

        self.framec = Frame(self.parent, height=100, width=200)
        self.framec.pack()
        #self.framec.pack(fill=X, expand=1)
        #self.framec.grid(row=0, column=0)
        self.co = Label(self.framec, text="Checkout Counter")
        self.co.grid(row=0, column=1)

        self.addtotal=0

        #header
        self.q = Label(self.framec, text = "Quantity")
        self.q.grid(row=1, column=0, columnspan=6, sticky=W)

        self.i = Label(self.framec, text = "Item")
        self.i.grid(row=1, column=6, columnspan=20, sticky=W)

        self.p = Label(self.framec, text = "Price")
        self.p.grid(row=1, column=27, columnspan=6, sticky=W)

        self.tot = Label(self.framec, text="Total")
        self.tot.grid(row=1, column=33, columnspan=6, sticky=W)
        

        #list all the names of the orders on the left side and the price after it
        #get orders form the clicked food from a file
        ords = open("orders.txt")
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
            self.Qt = Label(self.framec, text=self.qntty)
            self.Qt.grid(row=i+3, column=0, columnspan=6, sticky=W)

            #Items
            self.It = Label(self.framec, text=orderitem)
            self.It.grid(row=i+3, column=6, columnspan=20, sticky=W)

            #Prices of individual items
            self.Pr = Label(self.framec, text=price)
            self.Pr.grid(row=i+3, column=27, columnspan=6, sticky=W)

            #Total price of the items based on the quantity
            self.total = Label(self.framec, text="QR"+str(int(self.qntty)*int(price[2:])))
            self.total.grid(row=i+3, column=33, columnspan=6, sticky=W)

            #add each total price to get the final total price
            self.addtotal = self.addtotal + int(self.qntty)*int(price[2:])

            #add an x button to cancel an order next to each orders
            self.X = Button(self.framec, text="X", height=1, width=1, command = lambda x="orders.txt", y=oneitem: self.askifsure(x,y))
            self.X.grid(row=i+3, column=39)

        #final price
        self.Total = Label(self.framec, text= "Total = %s" %(self.addtotal))
        self.Total.grid(row=10, column=33, columnspan=6, sticky=W)


        #get the customer details and contact information
        #put it in another frame below the first frame
        
        self.framei = Frame(self.parent, height=100, width=200)
        self.framei.pack()
        #self.framei.grid(row=11, column=0)

        #give instructions
        self.ins = Label(self.framei, text="\n\n\n\n\n Please fill out the following information: \n")
        self.ins.grid(row=0, column=0, sticky=W)
        #get the name
        self.getname = Label(self.framei, text="Name")
        self.getname.grid(row=1,column=0, sticky=W)
        self.entername = Entry(self.framei)
        self.entername.grid(row=1, column=1, sticky=W)
        #get the phone number
        self.getnumber = Label(self.framei, text="Phone number")
        self.getnumber.grid(row=2, column=0, sticky=W)
        self.enternum = Entry(self.framei)
        self.enternum.grid(row=2, column=1,sticky=W)
        #get the location
        self.location = Label(self.framei, text="Location")
        self.location.grid(row=3, column=0, sticky=W)
        self.enterloc = Entry(self.framei)
        self.enterloc.grid(row=3, column=1, sticky=W)
        #ask for comments or requests
        self.comments = Label(self.framei, text="Comments / Requests")
        self.comments.grid(row=4, column=0, sticky=W)
        self.entercom = Text(self.framei, height=5, width=20)
        self.entercom.grid(row=4, column=1, sticky=W)

        #proceed button
        self.pro = Button(self.framei, text="Send my Order!", command= lambda x=resto: self.proceed(x))
        self.pro.grid(row=6, column=3, sticky=E)


        #get the customer information inside the textbox
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
        thefile = open("orders.txt", "a")
        thefile.write("Customer: %s \n" %(self.cname))
        thefile.write("Phone Number: %s \n" %(self.cnum))
        thefile.write("Location: %s \n" %(self.cloc))
        thefile.write("Comments: %s \n" %(self.comm))
        thefile.close()

        #send this file with all the information to the food chain the customer is ordering from
        #so the main function must pass the food chain name
        #sendFile(s, friend, filename)
        print resto

        self.sendorder = sendFile(s,resto,"orders.txt")
        print self.sendorder
        
        

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
        self.yes = Button(self.frames, text="Yes", command = lambda x=themenu, y=cancelthis, z=self.sure: self.cancel(x,y,z))
        self.yes.pack()
        self.no = Button(self.frames,text="No", command = lambda x=self.sure : self.close(x))
        self.no.pack()


    def close(self,parent):
        parent.destroy()


    '''when the x button is clicked, the item will be deleted from the order file and also from the
    cart window right away'''
    def cancel(self, themenu, cancelthis, window):
        self.close(window)
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
        crt = GoToCart(themenu,self.resto,self.openagain)
        
        


    









            

        
# ----------------------------      FOOD CHAINS     --------------------------------------
class FoodChain:
    def __init__(self,name,parent=None):
        self.parent = parent
        self.parent.geometry("400x400")
        
        if name=="papaj":
            fc = "Papa John's"
        elif name=="zaatar":
            fc="Zaatar w Zeit"
        elif name=="elevation":
            fc = "Elevation Burger"
        
        self.t = self.parent.title(fc)
        self.framef = Frame(self.parent, height= 400, width=400)
        self.framef.pack()
        self.welc = Label(self.framef, text = "Welcome %s!" %(fc))
        self.welc.pack()
        #self.welc.grid(row=1, column=1)
        self.select  = Label(self.framef, text="Select 'Update Menu' if you wish to update your menu for today")
        self.select.pack()
        #self.select.grid(row=2, column=1)

        #update menu
        self.update = Button(self.framef, text="Update menu", command = self.updatemenu)
        self.update.pack()
        #self.update.grid(row=4, column=2)

        #check your orders
        self.see = Label(self.framef, text="See your orders here!")
        self.see.pack()
        '''just list the orders in this window, so recieve messages, and list them vertically,
        with the customer name, address, phone number, orders'''

        '''if menu is updated, provide the default menu, if the user uploads a new menu, send that
        file'''

        self.sendmenu() 

    '''if update menu was selected, the file uploaded must be sent to the customer when he clicks
    the food chain's button right away'''

    def updatemenu(self):
        self.window = Toplevel()
        self.window.title("Update menu")
        self.window.geometry("550x250")
        self.frameu = Frame(self.window, height=60, width=80)
        self.frameu.pack()

        self.note = Label(self.frameu, text="Please write the complete name of the file that contains your menu")
        self.note.pack()
        self.additional = Label(self.frameu, text="Note: it must be in the same directory with the one you are working on right now")
        self.additional.pack()
        self.here= Entry(self.frameu)
        self.here.pack()

        #i need to access the filename passed here in other functions too so make it global
        global filename 
        filename = self.here.get()
        

        self.ok = Button(self.frameu, text="ok", command= self.globname) #i dont think this works 
        self.ok.pack()



    '''if the menu is updated, send the default menu
    the food chains will only receive messages and no files'''
    #this makes me access the filename passed in the other function
    def globname():
        return filename #THIS DOESNT WORK
    
    def sendmenu(self):
        self.parent.after(10000, self.sendmenu)
        fmails = getMail(s)
        print fmails

        #check which menu to send
        '''
        if self.updatemenu(): #THIS OPENS THE UPDATE MENU EVERY 10MS WRONG 
            menuname = self.globname()
        else:
            menuname = "papajmenu.txt"
            
        print menuname'''
        
        #getMail returns a tuple of lists with tuples inside (user, message)
        #get the first element (index 0) of the tuple which is  the list of tuples of messages
        fmesstuple = fmails[0]
        
        #get the length of the list of tuples to know how many messages you received
        howmanyf = len(fmesstuple)
        
        #access the list and get the username from the zero index of the tuple, and the first index
        #is the message
        for i in range(howmanyf):
            #get the customer name 
            csender = fmesstuple[i][0]
            cmesg = fmesstuple[i][1]

            if cmesg == 'What is your menu today?':
                #send the file of the menu for today
                sendit = sendFile(s, sender, "papajmenu.txt") #but i think this is still not realtime
                if sendFile(s, sender, "papajmenu.txt"):
                    print True
                print False
            
        
        
        

        

        
#Food chain class

        

wnd = Tk()
s= StartConnection("86.36.35.17", 15112)
LG = LOG(wnd)
wnd.mainloop()

   
