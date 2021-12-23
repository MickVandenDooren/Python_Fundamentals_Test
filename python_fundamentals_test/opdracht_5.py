def list_manipulation(list, command, location,value=""):    
    if command=="remove" and location=="end":
        x=list[-1]
        del list[-1]
        print(x)
    
    if command=="remove" and location=="beginning":
        x=list[0]
        del list[0]
        print(x)
    
    if command=="add" and location=="beginning":
        list.insert(0,value)
        print(list)
        
    if command=="add" and location=="end":
        list.append(value)
        print(list)

#test
list_manipulation([1,2,3],"remove","end")
list_manipulation([1,2,3],"remove","beginning")
list_manipulation([1,2,3],"add","beginning",20)
list_manipulation([1,2,3],"add","end",30)
