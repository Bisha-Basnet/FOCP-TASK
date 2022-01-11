name= input("What is your name?")
if name.lower()!="arthur":
    seek=input("What do you seek? ")
    if "grail" in seek.lower():
        color= input("what is your favourite colour:")
        if color.lower()[0]==name.lower()[0]:
            print("You may enter")
        else:
            print("You may not enter")
            
    else:
        print("You may not enter")
        
else:
    print("You may enter")
    

    