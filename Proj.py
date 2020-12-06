from tkinter import *
from tkcalendar import *

screen = Tk()
screen.minsize(800,600)
screen.title("Calendar Beta Version")
screen.configure(background = "yellow2")
def selectDate():
    myDate = myCal.get_date()
    selectedDate = Label(text = myDate)
    selectedDate.place(x = 500, y = 400)

myCal = Calendar(screen, selectmode ="day", date_pattern = "d/m/yy")
myCal.place(x = 350, y = 100)

openCal = Button(screen, text = "Select Date", command = selectDate)
openCal.place(x = 400, y = 400)
