from tkinter import *
from tkinter import messagebox
import tkinter as tk

class Tela:

    def __init__(self, master):

        monitor = PhotoImage(file="monitor.png")
        lbMonitor = Label(janela, image=monitor)
        lbMonitor.monitor = monitor
        lbMonitor.place(x=100, y=30)

        teclado = PhotoImage(file="teclado.png")
        lbMonitor = Label(janela, image=teclado)
        lbMonitor.teclado = teclado
        lbMonitor.place(x=50, y=530)

        delete = PhotoImage(file="delete.png")
        lbDelete = Label(janela, image=delete)
        lbDelete.delete = delete
        lbDelete.config(bg="red")
        lbDelete.bind("<Button-1>", self.bios)
        lbDelete.place(x=842, y=722)

    def bios(self, event):

        janela2 = tk.Tk()
        print("DELETE PRESSIONADO")
        #Label inicial
        p1 = tk.Label(janela2,foreground="white",background="#00008B",text="CMOS Setup Utility - Copyright (C) 1984-1999 Award Software")
        p1["font"] = ("Lucida Console","18")
        p1.pack(pady=7,padx=7,ipady=20,ipadx=7)

        linhaH = tk.Label(janela2,foreground="white",background="#00008B",text="____________________________________________________________________")
        linhaH["font"] = ("Lucida Console","18")
        linhaH.place(x=0,y=60)

        linhaV = tk.Label(janela2,foreground="white",background="#00008B",text="|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n")
        linhaV["font"] = ("Lucida Console","12")
        linhaV.place(x=470,y=90)
        
        
        #Label 1
        
        self.p2 = tk.Label(janela2,foreground="#FFD700",background="#00008B",text="> Standard CMOS Features")
        self.p2["font"] = ("Lucida Console","15")
        self.p2.place(x=80, y=100)
        
        #Label 2
        self.p3 = tk.Label(janela2,foreground="#FFD700",background="#00008B",text="> Advanced BIOS Features")
        self.p3["font"] = ("Lucida Console","15")
        self.p3.place(x=80, y=140)
        self.p3.bind("<Button-1>", self.bios2)
        

        #Label 3
        p4 = tk.Label(janela2, foreground="#FFD700",background="#00008B",text="> Advanced Chipset Features")
        p4["font"] = ("Lucida Console","15")
        p4.place(x=80, y=180)
        

        #Label 4
        p5 = tk.Label(janela2,foreground="#FFD700",background="#00008B",text="> Integrated Peripherials")
        p5["font"] = ("Lucida Console","15")
        p5.place(x=80, y=220)
        

        #Label 5
        p6 = tk.Label(janela2,foreground="#FFD700",background="#00008B",text="> Power Management Setup")
        p6["font"] = ("Lucida Console","15")
        p6.place(x=80, y=260)
        

        #Label 6
        p7 = tk.Label(janela2,foreground="#FFD700",background="#00008B",text="> PnP/PCI Configurations")
        p7["font"] = ("Lucida Console","15")
        p7.place(x=80, y=300)
        

         #Label 7
        p8 = tk.Label(janela2,foreground="#FFD700",background="#00008B",text="> PC Health Status")
        p8["font"] = ("Lucida Console","15")
        p8.place(x=80, y=340)
        

        #///////////////////////////////////////////////////////////////////////////////////

        #Label 8
        p9 = tk.Label(janela2,foreground="#FFD700",background="#00008B",text="> Frequency/Voltage Control")
        p9["font"] = ("Lucida Console","15")
        p9.place(x=520, y=100)
        

        #Label 9
        p10 = tk.Label(janela2,foreground="#FFD700",background="#00008B",text="> Load Fail-Safe Defaults")
        p10["font"] = ("Lucida Console","15")
        p10.place(x=520, y=140)
        

        #Label 10
        p11 = tk.Label(janela2,foreground="#FFD700",background="#00008B",text="> Load Optimized Defaults")
        p11["font"] = ("Lucida Console","15")
        p11.place(x=520, y=180)
        

        #Label 11
        p12 = tk.Label(janela2,foreground="#FFD700",background="#00008B",text="> Set Supervisor Password")
        p12["font"] = ("Lucida Console","15")
        p12.place(x=520, y=220)
        
        

        #Label 12
        p13 = tk.Label(janela2,foreground="#FFD700",background="#00008B",text="> Set User Password")
        p13["font"] = ("Lucida Console","15")
        p13.place(x=520, y=260)
        
        
        #Label 13
        p14 = tk.Label(janela2,foreground="#FFD700",background="#00008B",text="Save & Exit Setup")
        p14["font"] = ("Lucida Console","15")
        p14.place(x=520, y=300)

        #Label 14
        p15 = tk.Label(janela2,foreground="#FFD700",background="#00008B",text="Exit Without Saving")
        p15["font"] = ("Lucida Console","15")
        p15.place(x=520, y=300)

        

        #Esc
        esc = tk.Label(janela2,foreground="white",background="#00008B",text="Esc : Quit")
        esc["font"] = ("Lucida Console","15")
        esc.place(x=23, y=470)

        #F10
        f10 = tk.Label(janela2,foreground="white",background="#00008B",text="F10 : Save & Exit Setup")
        f10["font"] = ("Lucida Console","15")
        f10.place(x=23, y=498)

       

        #Rodapé
        rodape = tk.Label(janela2, text="Time, Date, Hard Disk Type. . .")
        rodape["font"] = ("Helvetica","16")
        rodape.configure(background="#00008B", foreground="#FFD700")
        rodape.place(x=280,y=580)

        janela2.title("BIOS")
        janela2.geometry("880x640+200+30")
        janela2.config(bg="#00008B")
        janela2.resizable(width=False, height=False)
        janela2.mainloop()

    def bios2(self, event):

        jan2= tk.Tk()
        jan2.configure(bg="#00008B")
        jan2.geometry('880x700+200+20')
        jan2.config(cursor="hand2")
        jan2.resizable(width=False, height=False)
        jan2.title("Ordem de Boot")


        #Label inicial
        self.lb1 = tk.Label(jan2,foreground="white",background="#00008B",text="Phoenix - Award BIOS CMOS Setup Utility\nAdvanced BIOS Features")
        self.lb1["font"] = ("Lucida Console","18")
        self.lb1.pack(pady=7,padx=7,ipady=15,ipadx=7)

        #Linha horizontal
        self.l1 = tk.Label(jan2,foreground="white",background="#00008B",text="____________________________________________________________________________")
        self.l1["font"] = ("Lucida Console","18")
        self.l1.place(x=0,y=70)

        #Linha vertical
        self.l2 = tk.Label(jan2,foreground="white",background="#00008B",text="|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|")
        self.l2["font"] = ("Lucida Console","15")
        self.l2.place(x=630, y=95)

        #Label 1
        self.lb3 = tk.Label(jan2,foreground="white",background="#00008B",text="Virus Warning")
        self.lb3["font"] = ("Lucida Console","15")
        self.lb3.place(x=30, y=100)

        self.lb4 = tk.Label(jan2,foreground="#FFD700",background="#00008B",text="Disabled")
        self.lb4["font"] = ("Lucida Console","15")
        self.lb4.place(x=400, y=100)

        self.lb5 = tk.Label(jan2,foreground="white",background="#00008B",text="CPU L1 Cache")
        self.lb5["font"] = ("Lucida Console","15")
        self.lb5.place(x=30, y=130)

        self.lb6 = tk.Label(jan2,foreground="#FFD700",background="#00008B",text="Enabled")
        self.lb6["font"] = ("Lucida Console","15")
        self.lb6.place(x=400, y=130)

        self.lb7 = tk.Label(jan2,foreground="white",background="#00008B",text="CPU L2 Cache")
        self.lb7["font"] = ("Lucida Console","15")
        self.lb7.place(x=30, y=160)

        self.lb8 = tk.Label(jan2,foreground="#FFD700",background="#00008B",text="Enabled")
        self.lb8["font"] = ("Lucida Console","15")
        self.lb8.place(x=400, y=160)

        self.lb9 = tk.Label(jan2,foreground="white",background="#00008B",text="Quick Power On Self Test")
        self.lb9["font"] = ("Lucida Console","15")
        self.lb9.place(x=30, y=190)

        self.lb10 = tk.Label(jan2,foreground="#FFD700",background="#00008B",text="Enabled")
        self.lb10["font"] = ("Lucida Console","15")
        self.lb10.place(x=400, y=190)

        self.l11 = tk.Label(jan2,foreground="white",background="#00008B",text="HDD Boot Sprite")
        self.l11["font"] = ("Lucida Console","15")
        self.l11.place(x=30, y=220)

        self.l12 = tk.Label(jan2,foreground="#FFD700",background="#00008B",text="Disabled")
        self.l12["font"] = ("Lucida Console","15")
        self.l12.place(x=400, y=220)

        self.l13 = tk.Label(jan2,foreground="white",background="#00008B",text="First Boot Device")
        self.l13["font"] = ("Lucida Console","15")
        self.l13.place(x=30, y=250)

        self.l14 = tk.Label(jan2,foreground="#FFD700",background="red",text="CD-ROM")
        self.l14["font"] = ("Lucida Console","15")
        self.l14.place(x=400, y=250)

        self.l15 = tk.Label(jan2,foreground="white",background="#00008B",text="Second Boot Device")
        self.l15["font"] = ("Lucida Console","15")
        self.l15.place(x=30, y=280)

        self.l16 = tk.Label(jan2,foreground="#FFD700",background="#00008B",text="HDD-0")
        self.l16["font"] = ("Lucida Console","15")
        self.l16.place(x=400, y=280)

        self.l17 = tk.Label(jan2,foreground="white",background="#00008B",text="Third Boot Device")
        self.l17["font"] = ("Lucida Console","15")
        self.l17.place(x=30, y=310)

        self.l18 = tk.Label(jan2,foreground="#FFD700",background="#00008B",text="Disabled")
        self.l18["font"] = ("Lucida Console","15")
        self.l18.place(x=400, y=310)

        self.l19 = tk.Label(jan2,foreground="white",background="#00008B",text="Boot Other Device")
        self.l19["font"] = ("Lucida Console","15")
        self.l19.place(x=30, y=340)

        self.l20 = tk.Label(jan2,foreground="#FFD700",background="#00008B",text="Disabled")
        self.l20["font"] = ("Lucida Console","15")
        self.l20.place(x=400, y=340)

        self.l21 = tk.Label(jan2,foreground="white",background="#00008B",text="Swap Floppy Seek")
        self.l21["font"] = ("Lucida Console","15")
        self.l21.place(x=30, y=370)

        self.l22 = tk.Label(jan2,foreground="#FFD700",background="#00008B",text="Disabled")
        self.l22["font"] = ("Lucida Console","15")
        self.l22.place(x=400, y=370)

        self.l23 = tk.Label(jan2,foreground="white",background="#00008B",text="Boot Up Floppy Seek")
        self.l23["font"] = ("Lucida Console","15")
        self.l23.place(x=30, y=400)

        self.l24 = tk.Label(jan2,foreground="#FFD700",background="#00008B",text="Enabled")
        self.l24["font"] = ("Lucida Console","15")
        self.l24.place(x=400, y=400)

        self.l25 = tk.Label(jan2,foreground="white",background="#00008B",text="Boot Up NumLock Status")
        self.l25["font"] = ("Lucida Console","15")
        self.l25.place(x=30, y=430)

        self.l26 = tk.Label(jan2,foreground="#FFD700",background="#00008B",text="On")
        self.l26["font"] = ("Lucida Console","15")
        self.l26.place(x=400, y=430)

        self.l27 = tk.Label(jan2,foreground="white",background="#00008B",text="Gate A20 Option")
        self.l27["font"] = ("Lucida Console","15")
        self.l27.place(x=30, y=460)

        self.l28 = tk.Label(jan2,foreground="#FFD700",background="#00008B",text="Normal")
        self.l28["font"] = ("Lucida Console","15")
        self.l28.place(x=400, y=460)

        self.l29 = tk.Label(jan2,foreground="white",background="#00008B",text="Typematic Rate Setting")
        self.l29["font"] = ("Lucida Console","15")
        self.l29.place(x=30, y=490)

        self.l30 = tk.Label(jan2,foreground="#FFD700",background="#00008B",text="Disabled")
        self.l30["font"] = ("Lucida Console","15")
        self.l30.place(x=400, y=490)

        self.l31 = tk.Label(jan2,foreground="#1E90FF",background="#00008B",text="x Typematic Rate (Chars/Sec)")
        self.l31["font"] = ("Lucida Console","15")
        self.l31.place(x=9, y=520)

        self.l32 = tk.Label(jan2,foreground="#1E90FF",background="#00008B",text="6")
        self.l32["font"] = ("Lucida Console","15")
        self.l32.place(x=400, y=520)

        self.l33 = tk.Label(jan2,foreground="#1E90FF",background="#00008B",text="x Typematic Delay (Msec)")
        self.l33["font"] = ("Lucida Console","15")
        self.l33.place(x=9, y=550)

        self.l34 = tk.Label(jan2,foreground="#1E90FF",background="#00008B",text="250")
        self.l34["font"] = ("Lucida Console","15")
        self.l34.place(x=400, y=550)

        self.l33 = tk.Label(jan2,foreground="white",background="#00008B",text="Security Option")
        self.l33["font"] = ("Lucida Console","15")
        self.l33.place(x=30, y=580)

        self.l34 = tk.Label(jan2,foreground="#FFD700",background="#00008B",text="Setup")
        self.l34["font"] = ("Lucida Console","15")
        self.l34.place(x=400, y=580)

        self.l35 = tk.Label(jan2,foreground="white",background="#00008B",text="OS Select For DRAM > 64MB")
        self.l35["font"] = ("Lucida Console","15")
        self.l35.place(x=30, y=580)

        self.l36 = tk.Label(jan2,foreground="#FFD700",background="#00008B",text="Non-OS2")
        self.l36["font"] = ("Lucida Console","15")
        self.l36.place(x=400, y=580)

        self.l35 = tk.Label(jan2,foreground="white",background="#00008B",text="HDD S.M.A.R.T. Capability")
        self.l35["font"] = ("Lucida Console","15")
        self.l35.place(x=30, y=610)

        self.l36 = tk.Label(jan2,foreground="#FFD700",background="#00008B",text="Enabled")
        self.l36["font"] = ("Lucida Console","15")
        self.l36.place(x=400, y=610)

        self.l37 = tk.Label(jan2,foreground="white",background="#00008B",text="_____________________________________________________________________________________")
        self.l37["font"] = ("Lucida Console","15")
        self.l37.place(x=0, y=630)

        self.f10 = tk.Label(jan2,foreground="white",background="#00008B",text="F10: Save & Exit")
        self.f10["font"] = ("Lucida Console","15")
        self.f10.place(x=25, y=665)
        
        self.l38 = tk.Label(jan2,foreground="white",background="#00008B",text="Item Help")
        self.l38["font"] = ("Lucida Console","15")
        self.l38.place(x=705, y=120)
        

        self.l1 = tk.Label(jan2,foreground="white",background="#00008B",text="---------------------------------")
        self.l1["font"] = ("Lucida Console","15")
        self.l1.place(x=640, y=152)

        self.p17 = tk.Label(jan2,foreground="white",background="#00008B",text="-Menu Level >")
        self.p17["font"] = ("Lucida Console","15")
        self.p17.place(x=650, y=180)

    

        

janela = Tk()
Tela(janela)
janela.title("Simulador Formatação")
janela.geometry("1200x800+50+20")
janela.resizable(width=False, height=False)
janela.config(bg="white")
janela.config(cursor="hand2")
janela.attributes("-fullscreen", True)
janela.mainloop()
