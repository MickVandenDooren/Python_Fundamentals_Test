dictionary = {}

def frequency(list):
    for x in list:
        dictionary[x]=dictionary.get(x,0) + 1
    return dictionary

#test
products=['appel','aap','opa','bompa',5,True,True]
print(products)
print(frequency(products))

    
