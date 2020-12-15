
from tkinter import *
from tkcalendar import *
from datetime import date, datetime
import pickle

FONT = ("Rockwell", 32)
SMALL = ("Rockwell", 14)
SMALLER = ("Rockwell", 8)
MEDIUM = ("Rockwell", 12)

###https://www.geeksforgeeks.org/tkinter-application-to-switch-between-different-page-frames/
class CalApp(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        
        container = Frame(self)   
        container.pack(side = "top", fill = "both", expand = True)  
   
        container.grid_rowconfigure(0, weight = 1) 
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}   

        for F in (MenuPage, Register, Login, Page2, Page3): 
   
            frame = F(container, self) 

            self.frames[F] = frame  
   
            frame.grid(row = 0, column = 0, sticky ="nsew") 
   
        self.show_frame(MenuPage) 

    def show_frame(self, cont): 
        frame = self.frames[cont] 
        frame.tkraise()

class MenuPage(Frame): 
    def __init__(self, parent, controller):  
        Frame.__init__(self, parent, background = "Black") 
####
        Main_menu = Label(self, text =" Main Menu" , font = FONT, bg = "yellow2") 
          
        Main_menu.grid(row = 0, column = 2, padx = 5, pady = 10)  


        ##BUTTON
        button1 = Button(self, text ="Login", font = SMALL, cursor = "dot",
                         bg = "yellow2",highlightbackground = "white",
        command = lambda : controller.show_frame(Login))
        button1.grid(row = 4, column = 2, padx = 5, pady = 10)
        button2 = Button(self, text ="Register", font = SMALL, cursor = "dot",
                         bg = "yellow2",highlightbackground = "white",
        command = lambda : controller.show_frame(Register))
        button2.grid(row = 5, column = 2, padx = 5, pady = 10)
        exit_btn = Button(self, text = "Exit", font = SMALL,bg = "yellow2",
                          cursor = "dot",highlightbackground = "red",
        command = quit)
        exit_btn.grid(row = 6, column = 2, padx = 5, pady = 10)

        #LABEL
        NameBox = Label(self, text =" Discover your schedule",font =SMALL, fg = "white", bg = "black")
        NameBox.grid(row =2,column = 2)
        FreeBox = Label(self, text =" Either Run the Day or the Day Runs You",font =SMALLER, fg = "white", bg = "black")
        FreeBox.grid(row =1,column = 2)

class Register(Frame): 
    def __init__(self, parent, controller):  
        Frame.__init__(self, parent, background = "Black")

        def save():
            if user_id.get() == "":
                pass
            elif user_pass.get() == "":
                pass
            else:
                with open("filename.txt", 'rb') as readfile:
                    storage=pickle.load(readfile)
                id_info = user_id.get()
                pass_info = user_pass.get()
                storage[id_info] = pass_info
                with open("filename.txt", 'wb') as outfile:
                    pickle.dump(storage, outfile)
    
                button1 = Button(self, text ="Go to Menu", font = SMALL, cursor = "dot",
                         bg = "yellow2",highlightbackground = "white",
                                 command = lambda : controller.show_frame(MenuPage))
                button1.grid(row = 5,column =0)
        ##LABEL
        la = Label(self, text = "USER_ID ", font = MEDIUM)
        la.grid(row = 0, column = 0, padx = 5, pady = 20)
        password = Label(self, text = "Password", font = MEDIUM)
        password.grid(row =2,column=0, padx = 5, pady = 20)

        #BUTTON
        confirm = Button(self, text = "Confirm", font = MEDIUM,command = save)
        confirm.grid(row =4,column=0, padx = 5, pady = 20)

        #ENTRY
        user_id = Entry(self)
        user_id.grid(row = 0, column = 1, padx = 5, pady = 20)
        user_pass = Entry(self,show = "*")
        user_pass.grid(row =2,column=1, padx = 5, pady = 20)

class Login(Frame): 
    def __init__(self, parent, controller):  
        Frame.__init__(self, parent, background = "Black")
        with open("filename.txt","rb") as infile:
            user = pickle.load(infile)
        print(user)
        def check():
            idu = user_id.get()
            passu = user_pass.get()
            if idu == "":
                pass
            else:
                if idu in user:
                    if passu == "":
                        pass
                    else:
                        if passu in user[idu]:
                            go = Button(self, text ="Next", font = SMALL, cursor = "dot",
                             bg = "red",highlightbackground = "white",
                                     command = lambda : controller.show_frame(Page2))
                            go.grid(row =4 ,column =1,padx = 30, pady = 20)
                        else:
                            Inc = Label(self, text = "Nice Try ;)", font = MEDIUM)
                            Inc.grid(row = 5, column = 0, padx = 5, pady = 20)
        infile.close()

        la = Label(self, text = "USER_ID ", font = MEDIUM)
        la.grid(row = 0, column = 0, padx = 5, pady = 20)
        password = Label(self, text = "Password", font = MEDIUM)
        password.grid(row =2,column=0, padx = 5, pady = 20)

        #BUTTON
        confirm = Button(self, text = "Login", font = MEDIUM, command = check )
        confirm.grid(row =4,column=0, padx = 5, pady = 20)

        #ENTRY
        user_id = Entry(self)
        user_id.grid(row = 0, column = 1, padx = 5, pady = 20)
        user_pass = Entry(self,show = "*")
        user_pass.grid(row =2,column=1, padx = 5, pady = 20)

        
        


class Page2(Frame):

    def __init__(self,parent,controller):
        Frame.__init__(self, parent, background = "red")
        myCal = Calendar(self,background = "black",disabledbackground="black", bordercolor="black", headersbackground="black",
             normalbackground="black", foreground='white', normalforeground='white',
             headersforeground='white', selectmode ="day",
             date_pattern = "d/m/yy")
        myCal.grid(row=0,column=0)

        def get():
            global myDate
            myDate = myCal.get_date()
            show = Label(self, text = myDate)
            show.grid(row = 4,column =0)
            return myDate

        def adds():
            Date_info = myDate
            Events_info = event.get()
            file = open("Event.txt","a")
            file.write(Date_info + ":" + Events_info + "\n")
            file.close()

##        def remove():
##            Date_info = myDate
##            Remove_event = 

        def show0():
            lst = []
            lst2 = []
            myDate = myCal.get_date()
            file = open("Event.txt","r")
            for line in file:
                a = line.split(":")
                if myDate == a[0]:
                    lst.append(a[-1])
                else:
                    pass
##                for words in line: 
##                    if myDate == a[0]:
##                        if a[1] == None:
##                            return "FREE"
##                        else:
##                            shown = a[count+1]
##                            count += 1
            file.close()
            if lst == []:
                lst2 = "FREE"
            else:
                for word in lst:
                    if word == "\n":
                        lst.remove(word)
                    else:
                        lst2.append(word.strip())
            
            NameBox = Label(self, text = lst2, bg = "yellow2")
            NameBox.grid(row =7,column = 0, padx = 20)

    
              
        #BUTTON
        save = Button(self, text = "Select Date", font = SMALLER,command = get)
        save.grid(row = 3, column = 0)
        add = Button(self, text = "Add event", font = SMALLER,command = adds)
        add.grid(row =5,column=0)
        show = Button(self, text = "Display event/s", font = SMALLER,command = show0)
        show.grid(row =6,column=0)
        nxt = Button(self,text ="Next", font = SMALL, cursor = "dot",
                         bg = "yellow2",highlightbackground = "white",
                        command = lambda : controller.show_frame(Page3))
        nxt.grid(row =8 ,column = 0)


        #ENTRY
        event = Entry(self)
        event.grid(row = 2,column = 0)
    


class Page3(Frame):

    def __init__(self,parent,controller):
        Frame.__init__(self, parent, background = "red")
        title = Label(self, text = "Here is your Schedule", font =SMALL, bg = "yellow2"
                      )
        title.grid(row = 0,column =0,padx = 24,pady = 10)
        
        def event():
            a = []
            b = []
            count = 0
            accept = open("Event.txt","r")
            for line in accept:
                line = line.strip("\n")

                a.append(line)

            for j in a:
                b.append(j)

            b.reverse()
            for k in b:
                for j in range(len(b)):
                    if b.count(k) > 1:
                        b.remove(k)
                        print(b)
            b.reverse()
            print(b)
            
##            show = Label(self, text = b[1:], font = SMALLER)
            for i in b:
                if b.count(i) > 1:
                    b.remove(i)
                else:
                    show = Label(self, text = i, font = SMALLER, bg = "yellow2")
                    show.grid(row = count + 3, column = 0, padx = 24, pady =10)
                    count += 1

        
        showevent = Button(self, text = "Show", bg = "yellow2", command = event)
        showevent.grid(row = 1,column =0,padx = 24,pady = 10)
        back = Button(self,text ="Back",cursor = "dot",
                         bg = "yellow2",highlightbackground = "white",
                        command = lambda : controller.show_frame(Page2))
        back.grid(row =2 ,column = 0)        
        
     


            

app = CalApp()
app.mainloop()  

##        Frame.__init__(self, parent, background = "yellow2")
##        next_func = Button(self, text = "Customize your Calendar")
##
##        v = StringVal()
##        click = Entry(self,textvariable = v)
##        myCal = DateEntry(self,background = "black",disabledbackground="black", bordercolor="black", headersbackground="black",
##             normalbackground="black", foreground='white', normalforeground='white',
##             headersforeground='white', selectmode ="day",
##             date_pattern = "d/m/yy")
##        myCal.pack(padx=10, pady=10)
##        myCal.config(background = "black")
##    
##        
##
##        
##     
##        
##
##
##class Page2(Frame):
##
##    def __init__(self,parent,controller):
##        Frame.__init__(self, parent, background = "yellow2")
##
##        cal = Calendar(self, selectmode='none')
##        date = cal.datetime.today() + cal.timedelta(days=2)
##        cal.calevent_create(date, 'Hello World', 'message')
##        cal.calevent_create(date, 'Reminder 2', 'reminder')
##        cal.calevent_create(date + cal.timedelta(days=-2), 'Reminder 1', 'reminder')
##        cal.calevent_create(date + cal.timedelta(days=3), 'Message', 'message')
##
##        cal.tag_config('reminder', background='red', foreground='yellow')
##
##        cal.pack(fill="both", expand=True)
##        Label(self, text="Hover over the events.").pack()
##        
##
##
##
##
##
##




       




