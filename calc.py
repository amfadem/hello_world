def add (a,b):
    c = a + b
    return c
def sub (a,b):
    c= a-b
    return c
def multi (a,b):
    c = a * b
    return c
def div (a,b):
    c = a / b
    return c



def main ():
    a= input("enter a: ")
    a= float (a)
    b= input("enter b: ")
    b= float (b)
    fun= input ("add/sub/multi/div: ")
    c=0
    if fun=="add":
        c = add (a,b)
    elif fun== "sub":
        c= sub (a,b)
    elif fun=="multi":
        c= multi (a,b)
    elif fun== "div":
        c= div (a,b)
    print (c)
    
    
    
    

if __name__=="__main__":
    main()
        
