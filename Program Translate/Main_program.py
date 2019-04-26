from tkinter import *
from tkinter import messagebox
import listfile as fileloc
import module_addword as modAddword
import module_checkfile as modCheckfile
import module_find as modFind
import module_history as modHist

main = Tk()

main.bind("<Escape>", exit)
main.geometry("700x700")
main.resizable(width = False, height = False)


main.title('Program Translate')

background_image = PhotoImage(file='landscape2.png')
background_label = Label(main, image=background_image)
background_label.place(relwidth=1, relheight=1)

#--------------------------------------------------------------
def Pop_result():
  val = entry.get()
  result = modFind.main(val)
  root = Tk()
  root.title('คำแปล')
  S = Scrollbar(root)
  T = Text(root, height=18, width=50,font=("Courier", 16))
  S.pack(side=RIGHT, fill=Y)
  T.pack(side=LEFT, fill=Y)
  S.config(command=T.yview)
  T.config(yscrollcommand=S.set)
  quote = result
  T.insert(END, quote)
  T.config(state=DISABLED)
  mainloop()
#--------------------------------------------------------------
def Pop_Rank():
  hist = modHist.main()
  list_hist = hist.top()
  hist_word = ""
  j = 1
  main = Tk()
  main.geometry('500x225')
  main.resizable(width = False, height = False)
  main.title('Top 5 Search')

  frame = Frame(main)
  frame.place(relheight=1, relwidth=1)

  for i in list_hist:
    if j == 6:
      break
    hist_word += "%d. %s %s ครั้ง\n" % (j, i[0], i[1])
    j += 1

  msg1 = Message(frame,font=("Perpetua", 20),text = hist_word,width = 300)#พื้นหลัง
  msg1.place(relx=0.25,rely=0, relwidth=1, relheight=1, anchor='n')#พื้นหลัง
#--------------------------------------------------------------
def ask_user():
  if messagebox.askretrycancel('Check','Not found, Please try again',) == True:
    entry.delete(0, END)
  else:
    pass
#---------------------------------------------------------
def to_History():
  hist = modHist.main()
  list_hist = hist.printhist()
  hist_word = ""
  j = 1
  main = Tk()
  main.geometry('700x700')
  main.resizable(width = False, height = False)
  main.title('History')

  frame = Frame(main)
  frame.place(relheight=1, relwidth=1)

  label = Label(main,text ='History',font = ("Perpetua", 20), fg = 'blue')
  label.place(relx=0.5, rely=0.0000000000000000000000000001, relwidth=0.75, relheight=0.1,anchor='n')

  for i in list_hist:
    if j == 11:
      break
    hist_word += "%d. %s %s\n" % (j, i[0], i[1])
    j += 1

  msg = Message(frame,font=("Perpetua", 12),text =hist_word,width = 1000)#พื้นหลัง
  msg.place(relx=0.5,rely=0.01, relwidth=10, relheight=1, anchor='n')#พื้นหลัง

  button = Button(frame, text="Clear History", command = (clear_hist),bg = 'gray' ,fg = 'white')
  button.place(relx=0.5, rely=0.87, relwidth=0.25, relheight=0.1,anchor='n')
#---------------------------------------------------------
def clear_hist():
  messagebox.showinfo("Clear", "Done!")
  hist = modHist.main()
  hist.clear()
#---------------------------------------------------------
def about():
  main = Tk()
  main.geometry('550x300')
  main.resizable(width = False, height = False)
  main.title('เอกสารอ้างอิง & โปรแกรม')

  label = Label(main,text ='เอกสารที่ใช้ : พจนานุกรมคอมพิวเตอร์และอินเตอร์เน็ต \n (ผู้เขียน ทีมบรรณาธิการหนังสือคอมพิวเตอร์) \n ------------------------------------------------- \n โปรแกรมที่ใช้ : Python (version 3.7),กล้องถ่ายรูป,Google Sheets \n Adobe Photoshop CC,Adobe Photoshop C6,Sublime Text \n Microsoft Powerpoint,Microsoft Word,Github' ,font = ("Perpetua", 15), fg = 'blue')
  label.place(relx=0.5, relwidth=10, relheight=1, anchor='n')
  
#---------------------------------------------------------
def develop():
  main = Tk()
  main.geometry('650x450')
  main.resizable(width = False, height = False)
  main.title('Group : She sell seashell by the seashore')

  frame = Frame(main)
  frame.place(relheight=1, relwidth=1)

  label = Label(main,text ='ผู้จัดทำ',font = ("Perpetua", 30), fg = 'blue')
  label.place(relx=0.5, rely=0.09, relwidth=0.75, relheight=0.1,anchor='n')

  msg = Message(frame,font=("Perpetua", 20),text = 'น.ส.วชิรดา ท้าวนอก  600510575\nน.ส.ชนกานต์ เอกอนันต์กุล  610510648\nน.ส.นนทรพร จันทร์มณีวงศ์  610510654\nน.ส.จุฬาลักษณ์ สุจันทร์  610510801\nนายธเนศ สิงห์ลอ  610510803\nนายวสันต์ แพทย์รัตน์  610510809',width = 500)#พื้นหลัง
  msg.place(relx=0.5,rely=0.01, relwidth=1, relheight=1, anchor='n')#พื้นหลัง

#---------------------------------------------------------Menu Bar
menubar = Menu(main)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Top 5 Search", command=Pop_Rank)
filemenu.add_command(label="History", command=to_History)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=main.quit)
menubar.add_cascade(label="File", menu=filemenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Developer", command=develop)
helpmenu.add_command(label="About...", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

main.config(menu=menubar)

#--------------------------------------------------------- เฟรม Program Translate
top_frame = Frame(main, bg='white', bd=10)
top_frame.place(relx=0.28, rely=0.05, relwidth=0.45, relheight=0.125)

label = Label(top_frame,text ='Program Translate',font = ("Perpetua", 20), bg='#BFE9FF')
label.place(relwidth=1, relheight=1)

#---------------------------------------------------------เฟรม กรอกข้อความ
frame = Frame(main, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.1,anchor='n')

entry = Entry(frame, font=40,justify='center')
entry.place(relwidth=1, relheight=1)

#---------------------------------------------------------เฟรม ปุ่ม
frame = Frame(main, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.32, relwidth=0.25, relheight=0.1,anchor='n')
#---------------------------------------------------------

def click_translate():
  msg1 = Message(lower_frame,font=("Perpetua", 20),bd = 3)#พื้นหลัง
  msg1.place(relx=0.5, rely=0, relwidth=1, relheight=1, anchor='n')#พื้นหลัง
  msg2 = Message(lower_frame,text = 'คำอธิบาย',font=("Cordia New", 18),bd = 3,width = 100000) #คำแปล
  msg2.place(relx=0.4)
  val = entry.get()
  result = modFind.main(val)

  if result == None:
    ask_user()
  elif len(result) <= 200:
    msg = Message(lower_frame,text =result,font=("Cordia New", 16),width=420)  #ยาว 30 คำ 6 บรรทัด
    msg.place(relx=0.05, rely=0.1341)

  elif len(result) >= 201:
    Pop_result()

#------------------------------------------------------------------ Enter to trans
def enter(obj):
  msg1 = Message(lower_frame,font=("Perpetua", 20),bd = 3)#พื้นหลัง
  msg1.place(relx=0.5, rely=0, relwidth=1, relheight=1, anchor='n')#พื้นหลัง
  msg2 = Message(lower_frame,text = 'คำอธิบาย',font=("Cordia New", 18),bd = 3,width = 100000) #คำแปล
  msg2.place(relx=0.4)#คำแปล

  val = entry.get()
  result = modFind.main(val)
  if result == None:
    ask_user()
  elif len(result) <= 200:
    msg = Message(lower_frame,text =result,font=("Cordia New", 16),width=420)  #ยาว 30 คำ 6 บรรทัด
    msg.place(relx=0.05, rely=0.1341)

  elif len(result) >= 201:
    Pop_result()

button = Button(frame, text="Translate", font=40, command = click_translate)
button.place(relx=0.5, rely=0.009, relwidth=1, relheight=1,anchor='n')
main.bind('<Return>', enter)
#------------------------------------------------------------------

lower_frame = Frame(main, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.45, relwidth=0.75, relheight=0.5, anchor='n')
  


msg1 = Message(lower_frame,font=("Cordia New", 20),bd = 3)#พื้นหลัง
msg1.place(relx=0.5, rely=0, relwidth=1, relheight=1, anchor='n')#พื้นหลัง

msg2 = Message(lower_frame,text = 'คำอธิบาย',font=("Cordia New", 18),bd = 3,width = 100000) #คำแปล
msg2.place(relx=0.4)#คำแปล



main.mainloop()
