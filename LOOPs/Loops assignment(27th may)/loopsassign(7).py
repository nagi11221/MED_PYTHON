#7
Random =['python','code','loop','if','python','else','if']
stop_words =("if","else")
unique_words =set()
for items in Random:
    if items not in stop_words:
     unique_words.add(items)

print("Unique words: ",unique_words)    
