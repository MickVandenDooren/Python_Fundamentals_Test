import random

actually_sick = random.choice([True, False])
kinda_sick = random.choice([True, False])
dont_feel_like_it = random.choice([True, False])

random_sequence=[0,1,2,3,4,5,6,7,8,9,10] 
sick_days=random.choice(random_sequence)

print('\n','actually sick:',actually_sick,'\n','kinda sick:',kinda_sick ,'\n',"don't feel like it:",dont_feel_like_it,'\n','amount of sickdays:', sick_days)
print()

calling_in_sick=False

while sick_days>0:
    
    if actually_sick==True and sick_days>0:
        calling_in_sick=True
        sick_days-=1
        print('feeling really sick today? ',calling_in_sick,'\n','amount of sickdays left:', sick_days)
    
    elif kinda_sick==True and dont_feel_like_it==True and sick_days>0:
        calling_in_sick=True
        sick_days-=1
        print('taking a break today? ',calling_in_sick,'\n','amount of sickdays left:', sick_days)
        
    #reset values
    actually_sick = random.choice([True, False])
    kinda_sick = random.choice([True, False])
    dont_feel_like_it = random.choice([True, False])
    calling_in_sick = False
    


