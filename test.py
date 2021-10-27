def get_money():
    
    balanc = 0
    accaunt= []
    while True:
        bank = int(input("Введите сумму: "))
        total = 0
        year = int(input("На сколько лет хотите: "))
        i = 0
        while i < year:
            
            balanc = bank + (bank* 0.1)* i
            dep = balanc + (balanc*0.10) 
            print(dep)
            
            i+=1
            
            
          
        total+=dep 
        accaunt.append(total)
        

        qt = input("Хотите еще положить: (y/n): ")
        # total.append(balanc)
        if qt == 'y':
            print("Сколько хотите?")
                
            
        elif qt == 'n':
            
            print(f' Ваш счет: {sum(accaunt)}')
            break

get_money()

    

