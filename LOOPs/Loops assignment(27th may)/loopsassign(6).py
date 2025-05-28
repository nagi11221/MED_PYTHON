#6 Multiply Dictionary Values if Key Starts with 'a'
fruits = {
    'apple':2,'appricot':4,'berry':5
}
final = 1
for items in fruits:
    if   items[0] == 'a':
        final = final * fruits[items]
print(final)        

        

