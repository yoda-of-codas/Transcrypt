#!usr/bin/python
import transposition
import englishchecker
import pyperclip
import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import messagebox as msg

position = "+50+50"

class mainwin():
        
    def __init__(self):
        self.win = tk.Tk()
        #adding titles and creating gui components
        self.win.title("Transcrypt")
        self.win.geometry(position)
        self.create_content()
        
    def about():
        msg.showinfo('Zen_of_Python....Respect','This is a miniproject, done by Bakel B Bakel selfacclaimed Yoda_of_Codas\
\nJust to test python OOP skills...This project spilled into 3 nights,4 classes,over 20 functions and approx. 450 codes of python')

    def help():
        msg.showinfo('Help on the app','1. Encrypt or Decrypt text or file:\n   Allows user to encrypt or decrypt\n   i. file by providing the file    path and key\n   ii. text by manually providing    the text and the key\
\n\n2. Brute force encrypted file or text by providing the file location for file or encrypted text for text option')

    def startencrypt(self):
        self.win.quit()
        self.win.destroy()
        encryptt = startencryptclass()
        encryptt.win2.mainloop()
    def startdecrypt(self):
        self.win.quit()
        self.win.destroy()
        decryptt = startdecryptclass()
        decryptt.win2.mainloop()
    def startbfafile(self):
        self.win.quit()
        self.win.destroy()
        bfa = bruteforcefile()
        bfa.win2.mainloop()
    def startbfatext(self):
        self.win.quit()
        self.win.destroy()
        bfa = bruteforcetext()
        bfa.win2.mainloop()
    def create_content(self):
        #Main Window
        self.win.resizable(False, False)
        menu_bar = Menu(self.win)
        self.win.config(menu=menu_bar)
        fmenu =Menu(menu_bar, tearoff=0)
        fmenu.add_command(label='Help',command=mainwin.help)
        menu_bar.add_cascade(label='More',menu=fmenu)
        fmenu.add_command(label='About',command=mainwin.about)
        #Option Label
        tlabel= ttk.LabelFrame(self.win, text='Select the required option')
        tlabel.grid(column=0, row=0, padx= 30, pady= 10)
        #Encrypt Button
        encryptbutton = ttk.Button(tlabel, text= "Encrypt file or text", command=lambda: mainwin.startencrypt(self))
        encryptbutton.grid(column=0,row=0)
        #Decrypt Button
        decryptbutton = ttk.Button(tlabel, text= "Decrypt file or text",command=lambda: mainwin.startdecrypt(self))
        decryptbutton.grid(column=0, row=1)
        #Brute-force Attack file Button
        bfabutton = ttk.Button(tlabel, text ="Brute-force Attack an Encrypted File",command=lambda: mainwin.startbfafile(self))
        bfabutton.grid(column=0, row=2)
        #Brute-force Attack text %Button
        bfatextbutton = ttk.Button(tlabel, text ="Brute-force Attack an Encrypted Text",command=lambda: mainwin.startbfatext(self))
        bfatextbutton.grid(column=0, row=3)

        for child in tlabel.winfo_children():
            child.grid_configure(padx=8, pady=4)

    def kill(self):
        self.win.quit()
        self.win.destroy()
        
class startencryptclass():

    def back(self):
        self.win2.quit()
        self.win2.destroy()
        backward = mainwin()

    def browseFiles(nb):
        filename = filedialog.askopenfilename(initialdir = "/", title= 'Select a File to Encrypt',filetypes = (("Text files","*.txt"),("all files","*.*")))
        nb.insert(0,filename)
        return filename
    
    def encryptfile(text,nb,keyentry):

        try:
            filename= nb.get()
            file = open(filename,'r')
            key = int(keyentry.get())
            message = file.read()
        except:
            msg.showwarning('Yoda spotted an error','Invalid input or file Location')
        else:
            output = transposition.encryptMessage(key,message)
            i = -1
            c=''
            while i>-(len(filename)+1):
                if filename[i] == '.':
                    outputname = filename[:i]+'encrypted'+filename[i:]
                    break
                if '.' not in filename:
                    outputname = filename+'Encrypted'
                    break
                i-=1
            ofo = open(outputname,'w')
            ofo.write(output)
            ofo.close()
            msg.showinfo('Python as the language, Hail Yoda_of_Codas','Your encrypted text is at '+outputname)
        
    def encrypttext(key,word,textlabel):
        
        try:
            text = word.get(1.0,'end')
            
            if text.endswith('\n'):
                text = text.strip()
            keys = int(key.get())
            result = transposition.encryptMessage(keys, text)
        except:
            msg.showwarning('Coda Bakel come in...Error on southside','Invalid File, File Location or Key')
        else:
            scr = scrolledtext.ScrolledText(textlabel, width=30, height=4, wrap=tk.WORD, padx = 10,pady=10)
            scr.grid(column=0,row=2 ,columnspan=3)
            scr.insert('1.0', result)
            scr.configure(state = 'disabled')
            copy = ttk.Button(textlabel, text ='Copy Text to Clipboard',command=lambda: pyperclip.copy(scr.get(1.0,'end')))
            copy.grid(column=0,row=3)
            
    def __init__(self):
        self.win2 = tk.Tk()
        self.win2.geometry(position)
        self.win2.title('Encrypter')
        self.win2.resizable(False, False)
        
        tabcontrol = ttk.Notebook(self.win2)
        file = ttk.Frame(tabcontrol)
        tabcontrol.add(file, text='Encrypt a file')
        text = ttk.Frame(tabcontrol)
        tabcontrol.add(text, text='Encrypt a text')
        tabcontrol.pack(expand = 1,fill = 'both')
        
        #-------------------------------------|
        #GUI for First Tab (Encrypting A File)|
        #_____________________________________|

        #Option Label
        label= ttk.LabelFrame(file, text='Enter the file location,\nPress done to encrypt')
        label.grid(column=0, row=0, padx= 10, pady= 10)

        nb = ttk.Entry(label, width=25)
        nb.grid(column=0, row=0)
        nb.focus()
        
        label2= ttk.LabelFrame(file, text='Key')
        label2.grid(column=0, row=1, padx= 5, pady= 5)

        enter = ttk.Button(label, text='Browse',command=lambda: startencryptclass.browseFiles(nb))
        enter.grid(column=1, row=0)
        
        enter = ttk.Button(label, text='Encrypt',command=lambda: startencryptclass.encryptfile(text,nb,keyentry))
        enter.grid(column=1, row=1)

        keyentry = ttk.Entry(label2, width=10)
        keyentry.grid(column=0, row=1, padx=5,pady=5)

        menu_bar = Menu(self.win2)
        self.win2.config(menu=menu_bar)
        fmenu =Menu(menu_bar, tearoff=0)
        
        menu_bar.add_command(label='Back',command=lambda: startencryptclass.back(self))

        for child in label.winfo_children():
            child.grid_configure(padx=8, pady=4)

        #-------------------------------------|
        #GUI for First Tab (Encrypting A Text)|
        #_____________________________________|
        #Scrolled Text
        textlabel= ttk.LabelFrame(text,text='Enter your text maually')
        textlabel.grid(column=0, row=1, padx= 10, pady= 5)
        scr = scrolledtext.ScrolledText(textlabel, width=30, height=4, wrap=tk.WORD, padx = 10,pady=10)
        scr.grid(column=0, columnspan=3)

        textlabel2= ttk.LabelFrame(textlabel,text='Key')
        textlabel2.grid(column=0, row=1, padx= 10, pady= 5)
        keyentry2 = ttk.Entry(textlabel2, width=10)
        keyentry2.grid(column=0, row=1, padx=5,pady=5)

        encryptb = ttk.Button(textlabel, text='Encrypt',command=lambda: startencryptclass.encrypttext(keyentry2,scr,textlabel))
        encryptb.grid(column=1,row = 1)
        
class startdecryptclass():

    def back(self):
        self.win2.quit()
        self.win2.destroy()
        backward = mainwin()
    def browseFiles(nb):
        filename = filedialog.askopenfilename(initialdir = "/", title= 'Select a File to Decrypt',filetypes = (("Text files","*.txt"),("all files","*.*")))
        nb.insert(0,filename)
        return filename
    
    def decryptfile(text,nb,keyentry):
        
        try:
            filename= nb.get()
            file = open(filename,'r')
            key = int(keyentry.get())
            message = file.read()
        except:
            msg.showwarning('CipherError','Invalid input or file Location')
        else:
            output = transposition.decryptMessage(key,message)
            i = -1
            c=''
            while i>-(len(filename)+1):
                if filename[i] == '.':
                    outputname = filename[:i]+'Decrypted'+filename[i:]
                    break
                if '.' not in filename:
                    outputname = filename+'Decrypted'
                    break
                i-=1
            ofo = open(outputname,'w')
            ofo.write(output)
            ofo.close()
            msg.showinfo('Transposition decrypting algorithm...Bakel B. Bakel','Your decrypted text is at '+outputname)
           
    def decrypt(key,word,textlabel):
    
        try:
            text = word.get(1.0,'end')
            if text.endswith('\n'):
                text = text.strip()
            keys = int(key.get())
            result = transposition.decryptMessage(keys, text)
        except:
            msg.showwarning('Bakel Bakel\'s Fix Tip','Invalid Key')
        else:
            scr = scrolledtext.ScrolledText(textlabel, width=30, height=4, wrap=tk.WORD, padx = 10,pady=10)
            scr.grid(column=0,row=2 ,columnspan=3)
            scr.insert('1.0', result)
            scr.configure(state = 'disabled')
            copy = ttk.Button(textlabel, text ='Copy Text to Clipboard',command=lambda: pyperclip.copy(scr.get(1.0,'end')))
            copy.grid(column=0,row=3)
        
    def __init__(self):
        
        self.win2 = tk.Tk()
        self.win2.geometry(position)
        self.win2.title('Decrypter')
        self.win2.resizable(False, False)
        
        tabcontrol = ttk.Notebook(self.win2)
        file = ttk.Frame(tabcontrol)
        tabcontrol.add(file, text='Decrypt a file')
        text = ttk.Frame(tabcontrol)
        tabcontrol.add(text, text='Decrypt a text')
        tabcontrol.pack(expand = 1,fill = 'both')
        
        #-------------------------------------|
        #GUI for First Tab (Decrypting A File)|
        #_____________________________________|

        #Option Label
        label= ttk.LabelFrame(file, text='Enter the file location,\nPress Decrypt to decrypt')
        label.grid(column=0, row=0, padx= 10, pady= 10)

        nb = ttk.Entry(label, width=25)
        nb.grid(column=0, row=0)
        nb.focus()
        
        label2= ttk.LabelFrame(file, text='Key')
        label2.grid(column=0, row=1, padx= 5, pady= 5)
        
        enter = ttk.Button(label, text='Browse',command=lambda: startdecryptclass.browseFiles(nb))
        enter.grid(column=1, row=0)
        
        enter2 = ttk.Button(label, text='Decrypt',command=lambda: startdecryptclass.decryptfile(text,nb,keyentry))
        enter2.grid(column=1, row=1)

        keyentry = ttk.Entry(label2, width=10)
        keyentry.grid(column=0, row=1, padx=5,pady=5)

        menu_bar = Menu(self.win2)
        self.win2.config(menu=menu_bar)
        fmenu =Menu(menu_bar, tearoff=0)
        
        menu_bar.add_command(label='Back',command=lambda: startencryptclass.back(self))

        keyentry = ttk.Entry(label2, width=10)
        keyentry.grid(column=0, row=1, padx=5,pady=5)

        menu_bar = Menu(self.win2)
        self.win2.config(menu=menu_bar)
        fmenu =Menu(menu_bar, tearoff=0)
        
        menu_bar.add_command(label='Back',command=lambda: startencryptclass.back(self))

        for child in label.winfo_children():
            child.grid_configure(padx=8, pady=4)

        #-------------------------------------|
        #GUI for First Tab (Encrypting A Text)|
        #_____________________________________|
        #Scrolled Text
        textlabel= ttk.LabelFrame(text,text='Enter your text maually')
        textlabel.grid(column=0, row=1, padx= 10, pady= 5)
        scr = scrolledtext.ScrolledText(textlabel, width=30, height=4, wrap=tk.WORD, padx = 10,pady=10)
        scr.grid(column=0, columnspan=3)

        textlabel2= ttk.LabelFrame(textlabel,text='Key')
        textlabel2.grid(column=0, row=1, padx= 10, pady= 5)
        keyentry2 = ttk.Entry(textlabel2, width=10)
        keyentry2.grid(column=0, row=1, padx=5,pady=5)
        #decrypt button
        encryptb = ttk.Button(textlabel, text='Decrypt',command=lambda: startdecryptclass.decrypt(keyentry2,scr,textlabel))
        encryptb.grid(column=1,row = 1)

class bruteforcefile():

    def back(self):
        self.win2.quit()
        self.win2.destroy()
        backward = mainwin()
        
    def filter(useful,label):
        scr2 = scrolledtext.ScrolledText(label, width=30, height=25, wrap=tk.WORD)
        scr2.grid(column=1,row=1)
        if useful == []:
            scr2.insert('end', 'No Reasonable English text detected change dictionary (dictionary.txt file) for other languages')
        else:
            uselist=[]
            for i in sorted(useful):
                uselist.append('With '+str(round(i*100,2))+'% English Match\n'+useful[i])
            scr2.insert('end', '\n\n'.join(uselist[::-1]))
        scr2.configure(state='disabled')
        
    def browseFiles(nb):
        filename = filedialog.askopenfilename(initialdir = "/", title= 'Select a File to Brute Force Attack',filetypes = (("Text files","*.txt"),("all files","*.*")))
        nb.insert(0,filename)
        return filename
    
    def brutefile(nb):
        try:
            filename = nb.get()
            file = open(filename,'r')
            texts = file.read()
        except:
            msg.showwarning('Bakel, What Happened?','Invalid file or file location')
        else:
            win2 = tk.Tk()
            win2.geometry(position)
            win2.resizable(False,False)
            win2.title('Brute force file operation')

        #Scrolled Text
            label3= ttk.LabelFrame(win2,text='Brute Force Results')
            label3.grid(column=0, row=0, padx= 10, pady= 5)
            scr2 = scrolledtext.ScrolledText(label3, width=40, height=25, wrap=tk.WORD)
            scr2.grid(column=0,row=1)
            progress = ttk.Progressbar(label3, orient ='horizontal',length=286,mode='determinate')
            progress.grid(column=0,row=0)
        
            progress['maximum']=len(texts)-1
            result,key,useful,usefultext,i,show ='',1,{},[],0,'Output File Locations: '
            while key<len(texts)+1:
                progress ['value'] = i
                x = transposition.decryptMessage(key,texts)
                j=-1
                while j>-(len(filename)+1):
                    if filename[j] == '.':
                        outputname = filename[:j]+'_decrypted_with_key_#'+str(key)+filename[j:]
                        break
                    if '.' not in filename:
                        outputname = filename+'_decyptred_with_key_#'+str(key)
                        break
                    j-=1
                result = x
                ofo = open(outputname,'w')
                ofo.write(result)
                ofo.close()
                show = show + '\n'+str(key)+': '+outputname+'\n'
                scr2.delete('1.0','end')
                scr2.insert('end', show)
                rating = englishchecker.isenglish(x)
            
                if rating > 0.4:
                    useful[rating]= outputname
                    #useful.append('Reasonable output at #'+str(key)+': '+outputname)
                
                progress.update()
                i+=1
                key+=1
            scr2.configure(state='disabled')
    
            menu_bar = Menu(win2)
            win2.config(menu=menu_bar)
            fmenu =Menu(menu_bar, tearoff=0)
            menu_bar.add_command(label='Filter for useful text',command=lambda: bruteforcefile.filter(useful,label3))
        
    def __init__(self):
        
        self.win2 = tk.Tk()
        self.win2.geometry(position)
        self.win2.title('Brute-Force File')
        self.win2.resizable(False, False)

        menu_bar = Menu(self.win2)
        self.win2.config(menu=menu_bar)
        fmenu =Menu(menu_bar, tearoff=0)
        
        menu_bar.add_command(label='Back',command=lambda: startencryptclass.back(self))

        #Option Label
        label= ttk.LabelFrame(self.win2, text='Enter the file location,\nPress Decrypt to decrypt')
        label.grid(column=0, row=0, padx= 10, pady= 10)

        nb = ttk.Entry(label, width=20)
        nb.grid(column=0, row=0)
        nb.focus()
    
        enter = ttk.Button(label, text='Browse',command=lambda: bruteforcefile.browseFiles(nb))
        enter.grid(column=1, row=0)
        
        enter2 = ttk.Button(label, text='BruteForce',command=lambda: bruteforcefile.brutefile(nb))
        enter2.grid(column=1, row=1)
        for child in label.winfo_children():
            child.grid_configure(padx=8, pady=4)
            
class bruteforcetext():

    def back(self):
        self.win2.quit()
        self.win2.destroy()
        backward = mainwin()

    def filter(useful,label):
        scr2 = scrolledtext.ScrolledText(label, width=30, height=25, wrap=tk.WORD)
        scr2.grid(column=1,row=1)
        if useful == {}:
            scr2.insert('end', 'No Reasonable English text detected change dictionary (dictionary.txt file) for other languages')
        else:
            uselist=[]
            for i in sorted(useful):
                uselist.append('With '+str(round(i*100,2))+'% English Match\n'+useful[i])
            scr2.insert('end', '\n\n'.join(uselist[::-1]))
        scr2.configure(state='disabled')
        
    def bruteforce(textlabel,scr):
        
        texts = scr.get(1.0,'end')
        
        if texts.endswith('\n'):
            texts = texts.strip()
        
        win2 = tk.Tk()
        win2.geometry(position)
        win2.resizable(False,False)
        win2.title('Brute force text operation')

        #Scrolled Text
        label3= ttk.LabelFrame(win2,text='Brute Force Results')
        label3.grid(column=0, row=0, padx= 10, pady= 5)
        scr2 = scrolledtext.ScrolledText(label3, width=30, height=25, wrap=tk.WORD)
        scr2.grid(column=0,row=1)
        progress = ttk.Progressbar(label3, orient ='horizontal',length=286,mode='determinate')
        progress.grid(column=0,row=0)
        progress['maximum']=len(texts)-1
        result,key,useful,usefultext,i ='',1,{},[],0
        while key<len(texts)+1:
            progress ['value'] = i
            x = transposition.decryptMessage(key,texts)
            result = result + '\nWith key #'+str(key)+': \n'+x+'\n'
            scr2.delete('1.0','end')
            scr2.insert('end', result)
            rating = englishchecker.isenglish(x)
            
            if rating > 0.2:
                useful[rating]=('At #'+str(key)+':\n'+x)
                
            progress.update()
            i+=1
            key+=1
        scr2.configure(state='disabled')
        
        #msg.showinfo('Python as the language, Thank Monty','Useful texts are on keys'+str(useful[0]))
        menu_bar = Menu(win2)
        win2.config(menu=menu_bar)
        fmenu =Menu(menu_bar, tearoff=0)
        menu_bar.add_command(label='Filter for useful text',command=lambda: bruteforcetext.filter(useful,label3))
         
    def __init__(self):
        
        self.win2 = tk.Tk()
        self.win2.geometry(position)
        self.win2.title('Brute-Force Text')
        self.win2.resizable(False, False)

        menu_bar = Menu(self.win2)
        self.win2.config(menu=menu_bar)
        fmenu =Menu(menu_bar, tearoff=0)
        menu_bar.add_command(label='Back',command=lambda: startencryptclass.back(self))

        #Scrolled Text
        textlabel= ttk.LabelFrame(self.win2,text='Enter your text maually')
        textlabel.grid(column=0, row=1, padx= 10, pady= 5)
        scr = scrolledtext.ScrolledText(textlabel, width=30, height=4, wrap=tk.WORD, padx = 10,pady=10)
        scr.grid(column=0, columnspan=3)

        encryptb = ttk.Button(textlabel, text='Bruteforce Attack',command=lambda: bruteforcetext.bruteforce(textlabel,scr))
        encryptb.grid(column=1,row = 1)
        
start = mainwin()
start.win.mainloop()
