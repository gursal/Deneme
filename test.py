from Tkinter import *
import ImageTk
hoca_penc = Tk()
baslik1 = hoca_penc.title("BULGU Hoca Penceresi")
hoca_penc.geometry("300x150+15+100")


class Test(object) :

    def __init__(self):
        self.buton1 = Button(text = "Rontgen" , command = self.film_ac , fg="blue" , bg = "red")
        self.buton1.pack()
        
        self.buton2 = Button(text = "CIKIS" , command = hoca_penc.destroy , fg="blue" , bg = "red")
        self.buton2.pack()

    def film_ac(self):
        penc2=Toplevel()
        baslik = penc2.title("Rontgen Filmi")
        film = ImageTk.PhotoImage(file = "ekg.jpg")
        ekran = Label(image = film)
       
        ekran.place(relx=0.4, rely= 0.1)
        mainloop()
        
calistir = Test()
mainloop()
