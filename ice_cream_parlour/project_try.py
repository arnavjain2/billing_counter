from tkinter import *
from tkinter import ttk
import ds
from PIL import ImageTk, Image
import datetime
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
smtp_server = "smtp.gmail.com"
sender_email = "arnavjain251@gmail.com"
port = 587  # For starttls
context = ssl.create_default_context()

 

root = Tk()
root.geometry("1157x1500")

def onButton(e):
    order1['fg']='red'

def leavBbutton(e):
    order1['fg'] = 'black'

def hide():
    my_notebook.add(my_frame2 , text='red tab')
    my_notebook.hide(0)

def show_3():
    global bill , discount
    global bill_sum , table
    global mybutton2
    c=[]
    sum = 0
    my_notebook.add(my_frame4 , text='4th tab')
    my_notebook.hide(0)
    if order.q ==[]:
        bill_sum= Label(my_frame4 , text='no order' , font=('',20),bg='lightblue')
        bill_sum.pack()
        bill = Label(my_frame4 , text='' ,bg='lightblue' )
        bill.pack()
    else:
        day = datetime.datetime.today().weekday()
        for i in order.q[0].items():
            c.append([i[0],i[1][0], i[1][1]])
            sum +=int(i[1][1])
        
        if sum>=650 and (day==5 or day==0):
            discount = 10
            discounted_price = sum - 0.1 *sum
        elif sum>=650:
            discount = 5
            discounted_price = sum - 0.05 *sum
        elif day==5 or day==0:
            discount = 5
            discounted_price = sum - 0.05 *sum
        else:
            discount=0
            discounted_price = sum
        

        list1=[]
        for i in order.q[0].items():
            list1.append(f'{i[0]}  {i[1][0]}  {i[1][1]}  ')
        print("discounted price after discointis" , discounted_price)
        message2 = f'Dear {user1.get()} ! \n your order has been delivered   and bill be delivered soon to your address: {address.get()} \n yout final order is:\n ' + "\n".join(map(str,list1)) + "\n AMOUNT TO BE PAID : " + f'{discounted_price}'
        try:
            
            msg1 =  MIMEMultipart() 
            msg1['From']='arnavjain251@gmail.com'
            msg1['To']= email1.get()
            msg1['Subject']="This is TEST"
            msg1.attach(MIMEText(message2, 'plain'))
            server = smtplib.SMTP(smtp_server,port)
            server.ehlo() # Can be omitted
            server.starttls(context=context) # Secure the connection
            server.ehlo() # Can be omitted
            server.login('arnavjain251@gmail.com', 'rgarzinufolwqkjn')
            server.send_message(msg1)
            
            # TODO: Send email here
        except Exception as e:
            # Print any error messages to stdout
            print(e)
        finally:
            server.quit()
        
        order.delete_menu()
        bill = Label(my_frame4, text='YOUR ORDER\n'+'*'*105 +"\n" , bg='lightblue' , font=('',20) )

        table = ttk.Treeview(my_frame4, columns=('items','QUANTITY','PRICE') , show='headings' , height=len(c) )
        
        

        if(discount != 0):
            bill_sum= Label(my_frame4 , text=f'TOTAL AMOUNT = {sum} \n Contgrats you got a discount of {discount}% \n PRICE AFTER DISCOUNT :{discounted_price}', font=('',30) , bg='lightblue')
        else:
            bill_sum= Label(my_frame4 , text=f'total amount :{discounted_price}',font=('',30) , bg='lightblue')
        table.heading('items' , text='ITEMS')
        table.heading('QUANTITY' , text='QUANTITY')
        table.heading('PRICE' , text='PRICE') 
        bill.pack()
        
        for i in range(len(c)):
            items = c[i][0]
            quantity = c[i][1]
            price = c[i][2]
            data = (items,quantity,price)
            table.insert(parent='',index='end' , values=data )
        table.pack(fill='x')
        
        table.pack()
        bill_sum.pack()

    mybutton2 = Button(my_frame4, text='go back', command=show6 , font=('',20))
    mybutton2.pack()



def both():
    if var !='' and var1 !='' and var2 !='' :
        values()
        sendmail(email1.get())
        finalize(user1.get(),email1.get(),phone.get(),address.get())
    else:
        pass
    show()
def sendmail(mail):
    list1=[]
    for i in order.a.items():
        list1.append(f'{i[0]}  {i[1][0]}  {i[1][1]}  ')

    message1 = f'Dear {user1.get()} ! \n your order has been placed and bill be delivered soon to your address: {address.get()} \n yout final order is:\n ' + "\n".join(map(str,list1)) + "\n AMOUNT TO BE PAID : " + str(order.onlytotal())
    try:
        
        msg =  MIMEMultipart() 
        msg['From']='arnavjain251@gmail.com'
        msg['To']= mail
        msg['Subject']="This is TEST"
        msg.attach(MIMEText(message1, 'plain'))
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login('arnavjain251@gmail.com', 'rgarzinufolwqkjn')
        server.send_message(msg)
        
        # TODO: Send email here
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()

def finalize(a,b,c,d):
    order.total()
    order.addtofile(a,b,c,d)
    order.final()

def show():
    my_notebook.add(my_frame1 , text='blue tab')
    my_notebook.hide(1)

def show5():
    my_notebook.add(my_frame1 , text='blue tab')
    my_notebook.hide(2)
    lab.destroy()
    lab1.destroy()
    mybutton.destroy()
    

def show6():
    my_notebook.add(my_frame1 , text='blue tab')
    my_notebook.hide(3)
    bill.destroy()
    bill_sum.destroy()
    mybutton2.destroy()
    table.destroy()
    

    
def close():
    root.destroy()
    

    

def values():
    if int(var.get()) !=0:
        a = int(var.get())
        order.update_menu("chocolate",a,70)
    if int(var1.get()) !=0:
        b= int(var1.get())
        order.update_menu("tooti-frooti",b,70)
    if int(var2.get()) !=0:
        c= int(var2.get())
        order.update_menu("Strawberry",c,70)
    print(order.a)
    
        
def waiting():
    global lab , lab1
    global mybutton
    my_notebook.add(my_frame3 , text='red tab')
    new_line= '\n'
    lab1 = Label(my_frame3 , text = 'WAITING LIST\n'+'*'*105 , font=('',20,) , bg='lightblue')
    lab1.pack()
    if order.q==[]:
        lab = Label(my_frame3 , text = 'NO ORDER IN WAITING' , font=('',30), bg='lightblue')
        lab.pack()
    else:
        lab = Label(my_frame3 , text= f' {new_line.join(map(str, order.q))}' , font=('',20), bg='lightblue')
        lab.pack()
    mybutton = Button(my_frame3 , text='go back', command=show5 , font=('',20))
    mybutton.pack()
    my_notebook.hide(0)
    
    


my_notebook  = ttk.Notebook(root)
my_notebook.pack()
my_frame1 = Frame(my_notebook , bg='lightblue' )
my_frame2 = Frame(my_notebook , bg='lightblue' )
my_frame3 = Frame(my_notebook , bg='lightblue')
my_frame4 = Frame(my_notebook , bg='lightblue')
my_frame1.pack()
my_frame2.pack()
my_frame3.pack()
my_frame4.pack()

my_notebook.add(my_frame1)
my_notebook.add(my_frame2)
my_notebook.add(my_frame3)
my_notebook.add(my_frame4)
my_notebook.hide(1)
my_notebook.hide(2)
my_notebook.hide(3)


#PAGE-1
Label(my_frame1 , text='WELCOME TO ICRECREAM PARLOUR' , font=('',25,) , bg='lightblue').pack()
Label(my_frame1 , text='*'*105 , font=('',20,) , bg='lightblue').pack()
order1 = Button(my_frame1 , text='1. placeorder' , font=('',20) , command=hide)
order1.pack(anchor=W)
order1.bind('<Enter>', onButton)
order1.bind('<Leave>', leavBbutton)

button2 = Button(my_frame1 , text='2. show waiting list' , font=('',20) , command=waiting)
button2.pack(pady=20, anchor=W)
button2.bind('<Enter>', lambda e: button2.config(fg='red'))
button2.bind('<Leave>', lambda e: button2.config(fg='black'))
button3 = Button(my_frame1 , text='3.order delivered' , font=('',20) , command=show_3)
button3.pack(pady=20 ,anchor=W)
button3.bind('<Enter>', lambda e: button3.config(fg='red'))
button3.bind('<Leave>', lambda e: button3.config(fg='black'))
button4 = Button(my_frame1 , text='4. exit' , font=('',20) , command=close)
button4.pack(pady=20 ,anchor=W)
button4.bind('<Enter>' , lambda e: button4.config(fg='red'))
button4.bind('<Leave>', lambda e: button4.config(fg='black'))
image1 = Image.open('D:/projects/tkinter/download.jpg')
image1 = image1.resize((500, 300))

img = ImageTk.PhotoImage(image1)
Label(my_frame1 , image=img , bg='lightblue').pack()
Label(my_frame1 , text='' ,bg='lightblue' ).pack(pady=5)

#PAGE-2
order = ds.queue1()
Label(my_frame2 , text='ENTER YOUR ORDER',fg='red',bg='pink' , font=('',25)).pack()
buttonframe = Frame(my_frame2 , bg='lightblue')
buttonframe.columnconfigure(0,weight=1)
buttonframe.columnconfigure(1,weight=1)
buttonframe.columnconfigure(2,weight=1)

Label(buttonframe , text='chocolate - $70/each' , font=('',20) , bg='lightblue').grid( pady=10, row=0,column=0 , sticky=W+E)
var = StringVar()
spin1 = Spinbox(buttonframe  , from_=0,to_=10, width=35 ,textvariable=var ).grid(row=0, column=2,sticky=W)
Label(buttonframe , text='tooti-frooti - $60/each' , font=('',20), bg='lightblue').grid(pady=10 ,row=1 , column=0 , sticky=W+E)
var1 = StringVar()

Spinbox(buttonframe ,  from_=0,to_=10, width=35 , textvariable=var1).grid(row=1, column=2,sticky=W)
Label(buttonframe , text='strawberry - $60/each' , font=('',20), bg='lightblue').grid(pady=10 ,row=2 , column=0 ,sticky=W+E)
var2 = StringVar()

Spinbox(buttonframe ,  from_=0,to_=10, width=35, textvariable=var2).grid(row=2, column=2,sticky=W)
buttonframe.pack(fill='x')
Label(my_frame2 , text='' , font=('',20) , bg='lightblue').pack(pady=3)
Label(my_frame2 , text='NAME:' , font=('',20) , bg='lightblue').pack()
user1 = StringVar()
Entry(my_frame2  , textvariable=user1, width=40).pack()

email1  =StringVar()
Label(my_frame2 , text='' , font=('',20) , bg='lightblue').pack(pady=3)
Label(my_frame2 , text='ENTER YOUR EMAIL:' , font=('',20) , bg='lightblue').pack()
Entry(my_frame2  , textvariable=email1,  width=55).pack()




phone  = StringVar()
Label(my_frame2 , text='' , font=('',20) , bg='lightblue').pack(pady=3)
Label(my_frame2 , text='PHONE NUMBER:' , font=('',20) , bg='lightblue').pack()
Entry(my_frame2  , textvariable=phone,  width=55).pack()

address =StringVar()
Label(my_frame2 , text='' , font=('',20) , bg='lightblue').pack(pady=3)

Label(my_frame2 , text='ADDRESS:' , font=('',20) , bg='lightblue').pack()

Entry(my_frame2  , textvariable=address,  width=55).pack()

Label(my_frame2 , text='' , font=('',20) , bg='lightblue').pack(pady=3)


button5 = Button(my_frame2, text='place order' , width=20,height=1,command= both , font=('',15))
button5.pack()
button5.bind('<Enter>', lambda e: button5.config(fg='red'))
button5.bind('<Leave>', lambda e: button5.config(fg='black'))
button6 = Button(my_frame2, text='go back' , width=20 , height=1,command= show , font=('',15))
button6.pack(pady=3)
button6.bind('<Enter>', lambda e: button6.config(fg='red'))
button6.bind('<Leave>', lambda e: button6.config(fg='black'))


#page 3



#page=4


root.mainloop()