import datetime
class queue1():
    discount = 0
    dis = 0
    sum_summary = []
    sum=0
    q = []
    a={}
    weekday=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    def update_menu(self,item,quantity,price):
        queue1.a.update({item : [quantity,price*quantity] })
    def final(self):
        print('*'*20)
        print("your final ordrer is")
        for i in queue1.a.items():
            print(f'{i[0]} : {i[1][0]}')
        print('*'*20)
        queue1.q.append(queue1.a)
        queue1.a = {}
    
    def delete_menu(self):
        print("*"*20)
        for i in queue1.q[0].items():
            print(f'item:{i[0]}   quantity:{i[1][0]}   price:{i[1][1]}')
        print(f'total price: {queue1.sum_summary}')
        print('*'*20)
        print("order is delivered")
        if(queue1.q == []):
            print("to order ro be delivered")
        else:
            queue1.sum_summary.pop(0)
            queue1.q.pop(0)
        
    def total(self):
        day = datetime.datetime.today().weekday()
        print('*'*20)
        for i in queue1.a.values():
            queue1.sum+=i[1]
        if (queue1.sum>650 and (day==0 or day == 5)):
            print(f'congrats! U get 10% discount on order of rupees {queue1.sum}')
            queue1.dis  = 0.1*queue1.sum
            queue1.discount = queue1.sum - 0.1*queue1.sum
        elif(queue1.sum>650):
            print(f'congrats! U get 5% discount on order of rupees {queue1.sum}')
            queue1.dis = 0.05*queue1.sum
            queue1.discount = queue1.sum - 0.05*queue1.sum
        elif day==0  or day == 5:
            print(f'congrats! U get 5% discount on order of rupees {queue1.sum}')
            queue1.dis = 0.05*queue1.sum
            queue1.discount = queue1.sum - 0.05*queue1.sum
        
        print("total order=",queue1.sum)
        if queue1.discount != 0:
            print("after discount=" , queue1.discount)
        queue1.sum_summary.append(queue1.discount)
        print('*'*20)

    def addtofile(self):
        day = datetime.datetime.today().weekday()
        import time
        today = time.strftime("%d/%m/%Y")
        f= open('D:/projects/ice_cream_parlour/data.csv','a')
        f.write(f'{today},{queue1.weekday[day]},')
        for i in queue1.a.items():
            f.write(f'{i[0]}:{i[1][0]}')
        f.write(f',{queue1.sum} ,{queue1.dis} , {queue1.discount}\n')
        f.close()
        queue1.sum = 0
        
        
    


        
# c = queue1()
# c.update_menu("ice",2,80)
# c.update_menu("valinaa",2,90)
# c.final()
# c.update_menu("ice1",2,80)
# c.update_menu("valinadewa",2,90)
# c.final()
# print(c.q)
# c.delete_menu()
# print(c.a)
# print(c.q)
        