import ds

print("welcome")
print("*********************************************************")


b= '''press:
1. To place Order
2. To view waiting list
3. waiting
4. exit '''

order = ds.queue1()
print(type(order))
quan_choc , quan_tut , quan_straw = 0,0,0

while True:
    to_do = int(input(b))
    if to_do==1:
                while True:
                    print('*'*30)
                    print('''     1 for chocolate   70 rs
        2 for tutti-frooti   50rs
        3 for strawberry   60rs''')
                    print('*'*20)
                    ice = int(input("enter the number "))
                    quantity = int(input("enter quantity"))
                    if ice==1:
                        quan_choc += quantity
                        order.update_menu("chocolate",quan_choc,70)
                    elif ice==2:
                        quan_tut += quantity
                        order.update_menu("tutti-frooti",quan_tut,50)
                    elif ice==3:
                        quan_straw += quantity
                        order.update_menu("strawberry",quan_straw,60)
                    e=input("do you want to add more ice-cream?(y/n)")
                    if e=="y":
                        continue
                    else:
                        order.total()
                        order.addtofile()
                        order.final()
                        quan_choc , quan_tut , quan_straw= 0,0,0
                        break
                
    elif to_do==2:
        order.delete_menu()
    elif to_do==3:
        print('*'*30)
        if(order.q ==[]):
            print("there is no waiting")
        else:
            print(order.q)
        print('*'*30)
    elif to_do==4 :
        print('exiting...')
        break