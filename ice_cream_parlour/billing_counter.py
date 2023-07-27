import ds

print("welcome")
print("*********************************************************")
menu = (''' menu:
1 for icecream:
2 for dishes:
3 for breads:
''')


b= '''press:
1. To place Order
2. To view waiting list
3. waiting
4. exit '''

order = ds.queue1()
quan_choc , quan_tut , quan_straw,quan_paneer,quan_naan,quan_butternaan,quan_dal,quan_chicken = 0,0,0,0,0,0,0,0

while True:
    print('*'*20)
    to_do = int(input(b))
    print('*'*20)
    if to_do==1:
        while True:
            print('*'*20)
            print(menu)
            print('*'*20)
            item_type = int(input("enter the type of item"))
            if(item_type==2):
                while True:
                    print('*'*20)
                    print('''     1 for Paneer   150 rs
     2 for dal   120rs
     3 for chicken   200rs ''')
                    print('*'*20)
                    ice = int(input("enter the number "))
                    quantity = int(input("enter quantity"))
                    if ice==1:
                        quan_paneer += quantity
                        order.update_menu("paneer",quan_paneer,150)
                    elif ice==2:
                        quan_dal += quantity
                        order.update_menu("dal",quan_dal,120)
                    elif ice==3:
                        quan_chicken += quantity
                        order.update_menu("chicken",quan_chicken,200)
                    e=input("do you want to add more dishes(y/n)")
                    if e=="y":
                        continue
                    else:
                        break
            
            elif item_type==1:
                while True:
                    print('*'*20)
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
                        break
            elif item_type==3:
                while True:
                    print('*'*20)
                    print('''     1 for naan   10rs
     2 for stuffed-naan   15rs''')
                    print('*'*20)
                    ice = int(input("enter the number "))
                    quantity = int(input("enter quantity"))
                    if ice==1:
                        quan_naan += quantity
                        order.update_menu("naan",quan_naan,10)
                    elif ice==2:
                        quan_butternaan += quantity
                        order.update_menu("stuffed-naan",quan_butternaan,15)
                    e=input("do you want to add more breads?(y/n) ")
                    if e=="y":
                        continue
                    else:
                        break
            ask = input("do u wanna add more items(y/n)")
            if(ask=='y'):
                continue
            else:
                order.total()
                order.addtofile()
                order.final()
                quan_choc , quan_tut , quan_straw,quan_paneer,quan_naan,quan_butternaan,quan_dal,quan_chicken = 0,0,0,0,0,0,0,0
                break
    elif to_do==2:
        order.delete_menu()
    elif to_do==3:
        print(order.q)
    elif to_do==4 :
        print('exiting...')
        break