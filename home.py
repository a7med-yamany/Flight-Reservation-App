from tkinter import *
from booking import *

home = Tk()
# basic start of the looking of the page

home.state('zoomed')
home.resizable(True, True)
home.minsize(1300, 600)
home.title("FlightMate")
home.config(background=("#121316"))
logo = PhotoImage (file="D:\Learn Python\Flight Reservation App\Flight-Reservation-App\images\logo.png")
home.iconphoto(True, logo)
# end of basics

# book a flight code
planeIMG = PhotoImage(file=r"D:\Learn Python\Flight Reservation App\Flight-Reservation-App\images\airplane3.png")

bookingCard = Frame (home, bg= '#2A2C33', bd=1, relief= 'groove', padx=10, pady=10,
                     highlightbackground= '#E8AF11', highlightthickness=1,
                     width= 400, height= 250)
# bookingCard.pack(padx=20, pady=20)
# bookingCard.place(x= 400,y= 400)
bookingCard.place(relx= 0.35, rely= 0.5, anchor= 'n')
bookingCard.pack_propagate(False)

bookFBold = Label(bookingCard, text='Book a Flight', 
                 font=('Bodoni Moda', 20, 'bold'), 
                 fg= '#F2F3F5',
                 bg= '#2A2C33',
                 image= planeIMG, compound= 'top')
bookFBold.pack(padx= 10, pady= 10)

bookDetail = Label(bookingCard, text='''Secure your next trip by entering your traveler details 
                   and flight information.''',
                    font=('Bodoni Moda', 10), 
                    fg= '#B9BEC7',
                    bg= '#2A2C33')
bookDetail.pack(padx= 10, pady= 10)

bookButton = Button(bookingCard, text= 'Book Flight', 
                    font=('Bodoni Moda', 15),
                    bg= '#C99200',
                    fg= '#2A2C33',
                    activebackground='#E8AF11',
                    command= openBookingWindow)
bookButton.pack(padx= 10, pady= 10)

# view reservation code

listIMG = PhotoImage (file= r"D:\Learn Python\Flight Reservation App\Flight-Reservation-App\images\view list1.png")

viewCard = Frame (home, bg= '#2A2C33', bd=1, relief= 'groove', padx=10, pady=10,
                     highlightbackground= '#E8AF11', highlightthickness=1,
                     width= 400, height= 250)
# viewCard.pack(padx=20, pady=20)
# viewCard.place(x= 800,y= 400)
viewCard.place(relx= 0.65, rely= 0.5, anchor= 'n')
viewCard.pack_propagate(False)

viewFBold = Label(viewCard, text='View Reservations', 
                 font=('Bodoni Moda', 20, 'bold'), 
                 fg= '#F2F3F5',
                 bg= '#2A2C33',
                 image= listIMG, compound= 'top')
viewFBold.pack(padx= 10, pady= 10)

viewDetail = Label(viewCard, text='''Review itineraries and modify or cancel any
                    existing reservations.''',
                    font=('Bodoni Moda', 10), 
                    fg= '#B9BEC7',
                    bg= '#2A2C33')
viewDetail.pack(padx= 10, pady= 10)

viewButton = Button(viewCard, text= 'Book Flight', 
                    font=('Bodoni Moda', 15),
                    bg= '#C99200',
                    fg= '#2A2C33',
                    activebackground='#C99200')
viewButton.pack(padx= 10, pady= 10)

# the top bar
barIMG = PhotoImage(file= r"D:\Learn Python\Flight Reservation App\Flight-Reservation-App\images\logo1.png")

bar = Label (home, text= 'FlightMate Reservations', padx=10, pady=20, 
                font=('Bodoni Moda', 15, 'bold'),
                bg= '#C99200',
                fg= '#2A2C33', 
                image= barIMG, compound= 'left')
bar.pack(fill='x')

# welcom message
welcomeCard = Frame (home, bg= '#121316')
welcomeCard.pack(padx=0, pady=0, anchor= 'n')

welcomeBold = Label(welcomeCard, text='Welcome to FlightMate Reservations', 
                 font=('Bodoni Moda', 25, 'bold'), 
                 fg= '#C99200',
                 bg= '#121316')
welcomeBold.pack(padx= 10, pady= 10)

welcomeDetail = Label(welcomeCard, text='Reserve flights and stay in control of your bookings with our clean, intuitive FlightMate experience.',
                    font=('Bodoni Moda', 15), 
                    fg= '#B9BEC7',
                    bg= '#121316')
welcomeDetail.pack(padx= 10, pady= 10)





home.mainloop()