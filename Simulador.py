from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk



class Tela:


    def fechar(self, event):

        janela.destroy()
        exit()
    

    def fecharPc(self, event):
        
        self.imgFundo.place_forget()

        self.imgg2.place_forget()
        self.lbGabinete.config(bg="white")
        lbMonitor.place(x=100, y=30)
        self.imggg.place_forget()

        self.imgg3.place_forget()
        

        self.imgg4.place_forget()
        

        self.imgg5.place_forget()
       

        self.imgg6.place_forget()
       

        self.imgg7.place_forget()
        

        self.imgg8.place_forget()
       

        self.imgg9.place_forget()
        



    def __init__(self, master):

        global lbMonitor
        monitor = PhotoImage(file="monitor.png")
        lbMonitor = Label(image=monitor)
        lbMonitor.monitor = monitor
        lbMonitor.place(x=100, y=30)

        gabinete = PhotoImage(file="gabinete.png")
        self.lbGabinete = Label(janela, image=gabinete)
        self.lbGabinete.gabinete = gabinete
        self.lbGabinete.place(x=970, y=285)
        self.lbGabinete.bind("<Enter>", self.abrirPc)
        self.lbGabinete.bind("<Leave>", self.fecharPc)

        teclado = PhotoImage(file="teclado.png")
        lbTeclado = Label(janela, image=teclado)
        lbTeclado.teclado = teclado
        lbTeclado.place(x=50, y=530)

        delete = PhotoImage(file="delete.png")
        lbDelete = Label(janela, image=delete)
        lbDelete.delete = delete
        lbDelete.config(bg="red")
        lbDelete.bind("<Button-1>", self.bios)
        lbDelete.place(x=842, y=722)

        self.sair = Button(janela, text="[X]")
        self.sair["font"] = ("Arial", "15")
        self.sair.config(bg="red", foreground="white")
        self.sair.place(x=1200, y=30)
        self.sair.bind("<Button-1>", self.fechar)

        

    def abrirPc(self, event):
        global lbMonitor

        lbMonitor.place(x=1800, y=10)

        
        fundobranco = PhotoImage(file="fundobranco.png")
        self.imgFundo = Label(janela, image=fundobranco)
        self.imgFundo.fundobranco = fundobranco
        self.imgFundo.config(bg="white")
        self.imgFundo.place(x=80,y=30)
        
        gabineteAberto = PhotoImage(file="gabineteAberto.png")
        self.imggg = Label(janela, image=gabineteAberto)
        self.imggg.gabineteAberto = gabineteAberto
        self.lbGabinete.config(bg="green")
        self.imggg.place(x=60,y=100)

        hd = PhotoImage(file="hd.png")
        self.imgg2 = Label(janela, image=hd)
        self.imgg2.hd = hd
        self.imgg2.config(bg="green")
        self.lbGabinete.config(bg="green")
        self.imgg2.place(x=500,y=30)

        fonte = PhotoImage(file="fonte.png")
        self.imgg3 = Label(janela, image=fonte)
        self.imgg3.fonte = fonte
        self.imgg3.config(bg="green")
        self.lbGabinete.config(bg="green")
        self.imgg3.place(x=650,y=30)

        cpu = PhotoImage(file="cpu.png")
        self.imgg4 = Label(janela, image=cpu)
        self.imgg4.cpu = cpu
        self.imgg4.config(bg="green")
        self.lbGabinete.config(bg="green")
        self.imgg4.place(x=800,y=30)

        placa = PhotoImage(file="placa.png")
        self.imgg5 = Label(janela, image=placa)
        self.imgg5.placa = placa
        self.imgg5.config(bg="green")
        self.lbGabinete.config(bg="green")
        self.imgg5.place(x=500,y=200)

        memoria = PhotoImage(file="memoria.png")
        self.imgg6 = Label(janela, image=memoria)
        self.imgg6.memoria = memoria
        self.imgg6.config(bg="green")
        self.lbGabinete.config(bg="green")
        self.imgg6.place(x=650,y=200)

        sata = PhotoImage(file="sata.png")
        self.imgg7 = Label(janela, image=sata)
        self.imgg7.sata = sata
        self.imgg7.config(bg="green")
        self.lbGabinete.config(bg="green")
        self.imgg7.place(x=800,y=200)

        cooler = PhotoImage(file="cooler.png")
        self.imgg8 = Label(janela, image=cooler)
        self.imgg8.cooler = cooler
        self.imgg8.config(bg="green")
        self.lbGabinete.config(bg="green")
        self.imgg8.place(x=500,y=370)

        gpu = PhotoImage(file="gpu.png")
        self.imgg9 = Label(janela, image=gpu)
        self.imgg9.gpu = gpu
        self.imgg9.config(bg="green")
        self.lbGabinete.config(bg="green")
        self.imgg9.place(x=650,y=370)
        
    
    

    def bios(self, event):

        janela2 = tk.Tk()
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
        self.p3 = tk.Label(janela2,foreground="yellow",background="red",text="> Advanced BIOS Features")
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
        janela2.config(cursor="hand2")
        janela2.resizable(width=False, height=False)
        janela2.mainloop()

    def fecharBios(self, event):
        janela2.destroy()   

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
        self.l14.bind("<Button-1>", self.boot)

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

        jan2.mainloop()

            
       
    
    def boot(self,event):
        
            
        messagebox.showinfo("WINDOWS 10", "Iniciando instalação...")


        #tux = PhotoImage(file="tux.png")
        #self.img0 = Label(janela, image=tux)
        #self.img0.tux = tux
        #self.img0.place(x=20, y=800)
        
        w1 = PhotoImage(file="w1.png")
        self.img1 = Label(janela, image=w1)
        self.img1.w1 = w1
        self.img1.place(x=123, y=50)

        abnts = ["(Português Brasil ABNT-2)", "(Português Brasil ABNT)"]
        abnt = ttk.Combobox(values=abnts)
        abnt.set("(Português Brasil ABNT)")
        abnt.place(x=412, y=262, width=337, height=22)

        btAvancar = PhotoImage(file="btAvancar.png")
        self.img2 = Label(janela, image=btAvancar)
        self.img2.btAvancar = btAvancar
        self.img2.place(x=740, y=324)
        self.img2.bind("<Button-1>", self.avancar)

    def avancar(self, event):
        w2 = PhotoImage(file="w2.png")
        self.img3 = Label(janela, image=w2)
        self.img3.w2 = w2
        self.img3.place(x=123, y=50)

        btInstalar = PhotoImage(file="btInstalar.png")
        self.img4 = Label(janela, image=btInstalar)
        self.img4.btInstalar = btInstalar
        self.img4.place(x=400, y=205)
        self.img4.bind("<Button-1>", self.instalar)

    def instalar(self, event):

        w3 = PhotoImage(file="w3.png")
        self.img5 = Label(janela, image=w3)
        self.img5.w3 = w3
        self.img5.place(x=113, y=52)

        chave = PhotoImage(file="chave.png")
        self.img6 = Label(janela, image=chave)
        self.img6.chave = chave
        self.img6.place(x=485, y=290)
        self.img6.bind("<Button-1>", self.chaveW)

        btAvancar2 = PhotoImage(file="btAvancar2.png")
        self.img7 = Label(janela, image=btAvancar2)
        self.img7.btAvancar2 = btAvancar2
        self.img7.place(x=726, y=300)
        self.img7.bind("<Button-1>", self.avancar2)

    def chaveW(self, event):

        self.img6.config(bg="lightblue")

        
    def avancar2(self, event):

        w4 = PhotoImage(file="w4.png")
        self.img8 = Label(janela, image=w4)
        self.img8.w4 = w4
        self.img8.place(x=112, y=49)

        btAvancar3 = PhotoImage(file="btAvancar3.png")
        self.img9 = Label(janela, image=btAvancar3)
        self.img9.btAvancar3 = btAvancar3
        self.img9.place(x=726, y=300)
        self.img9.bind("<Button-1>", self.avancar3)

    def avancar3(self, event):

        w5 = PhotoImage(file="w5.png")
        self.img10 = Label(janela, image=w5)
        self.img10.w5 = w5
        self.img10.place(x=112, y=49)

        btAvancar4 = PhotoImage(file="btAvancar4.png")
        self.img11 = Label(janela, image=btAvancar4)
        self.img11.btAvancar4 = btAvancar4
        self.img11.place(x=726, y=305)
        self.img11.bind("<Button-1>", self.avancar4)

    def avancar4(self, event):

        w6 = PhotoImage(file="w6.png")
        self.img12 = Label(janela, image=w6)
        self.img12.w6 = w6
        self.img12.place(x=112, y=49)

        personalizada = PhotoImage(file="personalizada.png")
        self.img13 = Label(janela, image=personalizada)
        self.img13.personalizada = personalizada
        self.img13.place(x=206, y=205)
        self.img13.bind("<Button-1>", self.avancar5)

    def avancar5(self, event):

        w7 = PhotoImage(file="w7.png")
        self.img14 = Label(janela, image=w7)
        self.img14.w7 = w7
        self.img14.place(x=112, y=49)

        formatar = PhotoImage(file="formatar.png")
        self.img15 = Label(janela, image=formatar)
        self.img15.formatar = formatar
        self.img15.place(x=460, y=238)
        self.img15.bind("<Button-1>", self.formatarW)

        btAvancar6 = PhotoImage(file="btAvancar6.png")
        self.img16 = Label(janela, image=btAvancar6)
        self.img16.btAvancar6 = btAvancar6
        self.img16.place(x=726, y=310)
        self.img16.bind("<Button-1>", self.avancar6)
    
    def formatarW(self, event):

        messagebox.showwarning("Formatação Windows 10", "TODOS OS DADOS DESSA PARTIÇÃO SERÃO EXCLUÍDOS !!")

    
    def avancar6(self, event):

        w8 = PhotoImage(file="w8.png")
        self.img18 = Label(janela, image=w8)
        self.img18.w8 = w8
        self.img18.place(x=112, y=49)
        self.img18.bind("<Button-1>", self.win)

    def win(self, event):

        w9 = PhotoImage(file="w9.png")
        self.img19 = Label(janela, image=w9)
        self.img19.w9 = w9
        self.img19.place(x=112, y=49)
        self.img19.bind("<Button-1>", self.win10)

    def win10(self, event):

        w10 = PhotoImage(file="w10.png")
        self.img20 = Label(janela, image=w10)
        self.img20.w10 = w10
        self.img20.place(x=112, y=49)

        iniciar = PhotoImage(file="iniciar.png")
        self.img21 = Label(janela, image=iniciar)
        self.img21.iniciar = iniciar
        self.img21.place(x=112, y=354)
        self.img21.bind("<Enter>", self.gerenciador)
        self.img21.bind("<Leave>", self.fecharGerenciador)

        chrome = PhotoImage(file="chrome.png")
        self.img23 = Label(janela, image=chrome)
        self.img23.chrome = chrome
        self.img23.place(x=600, y=100)
        self.img23.bind("<Enter>", self.chrome)
        self.img23.bind("<Leave>", self.chromeSair)

        winrar = PhotoImage(file="winrar.png")
        self.img26 = Label(janela, image=winrar)
        self.img26.winrar = winrar
        self.img26.place(x=700, y=100)
        self.img26.bind("<Enter>", self.winrar)
        self.img26.bind("<Leave>", self.winrarSair)

        reader = PhotoImage(file="reader.png")
        self.img27 = Label(janela, image=reader)
        self.img27.reader = reader
        self.img27.place(x=600, y=200)
        self.img27.bind("<Enter>", self.reader)
        self.img27.bind("<Leave>", self.readerSair)

        driver = PhotoImage(file="driver.png")
        self.img28 = Label(janela, image=driver)
        self.img28.driver = driver
        self.img28.place(x=700, y=200)
        self.img28.bind("<Enter>", self.driver)
        self.img28.bind("<Leave>", self.driverSair)


    def reader(self, event):

        telaReader = PhotoImage(file="telaReader.png")
        self.img27 = Label(janela, image=telaReader)
        self.img27.telaReader = telaReader
        self.img27.place(x=150, y=80)

    def driver(self, event):

        telaDriver = PhotoImage(file="telaDriver.png")
        self.img28 = Label(janela, image=telaDriver)
        self.img28.telaDriver = telaDriver
        self.img28.place(x=150, y=80)
    
    def chrome(self, event):
        telaChrome = PhotoImage(file="telaChrome.png")
        self.img24 = Label(janela, image=telaChrome)
        self.img24.telaChrome = telaChrome
        self.img24.place(x=150, y=80)

    def winrar(self, event):
        
        telaWinrar = PhotoImage(file="telaWinrar.png")
        self.img26 = Label(janela, image=telaWinrar)
        self.img26.telaWinrar = telaWinrar
        self.img26.place(x=150, y=80)

    def chromeSair(self, event):
       
        self.img24.place(x=1900, y=80)

    def driverSair(self, event):
       
        self.img28.place(x=1900, y=80)

    def readerSair(self, event):

        self.img27.place(x=1900, y=80)

    def winrarSair(self, event):

        self.img26.place(x=1900, y=80)

    def gerenciador(self, event):

        gerenciador = PhotoImage(file="gerenciador.png")
        self.img22 = Label(janela, image=gerenciador)
        self.img22.gerenciador = gerenciador
        self.img22.place(x=112, y=54)

    def fecharGerenciador(self, event):

        self.img22.place(x=1900, y=0)

        


        
        
        
    

        
    
        

        
        
        

    

    

        

janela = Tk()

Tela(janela)
janela.title("Simulador Formatação")
janela.geometry("1200x800+50+20")
janela.resizable(width=False, height=False)
janela.config(bg="white")
janela.config(cursor="hand2")
janela.attributes("-fullscreen", True)
janela.iconbitmap("placa2.ico")
janela.mainloop()
