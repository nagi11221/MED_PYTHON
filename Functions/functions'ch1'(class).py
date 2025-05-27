   #_________numbers printing_____
def one_two_three():
    print("1\n2\n3")
def three_to_seven():
    print("3\n4\n5\n6\n7")
def seven_to_ten():
    print("7\n5\n6\n8\n9\n10")

three_to_seven()
one_two_three()
seven_to_ten()
   #__________Greeting with name by calling function___________
name = "Messi"
def greeting_name(lang,name):
    if lang == 'en':
        print(f"hello {name}")
    elif lang == 'esp':
        print(f'Hola{name}')
    else:
        print(f'bonjour{name}')
    
greeting_name('en',name)  
                  #  _____________Extracting NAMES ______________________
 
data = [{"name" : "Messi","age" :37},
        {"name" : "Ronaldo" ,"age":39}]
def Extracting_names(details):
    name_1 = details[0]["name"]
    name_2 = details[1]["name"]
    return [name_1,name_2]    
names = Extracting_names(data)
print(names)



