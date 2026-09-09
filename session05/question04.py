#algoritm:
#get input
#jodakardan kalamat jomle
#ye a4 khali baraye max
#proccess ->  baresi hame kalamat
#aya az record ghabli > hast ya n
#print final


maxc = 0
word = ""
a = input("enter a sentence: ")
l = a.split(" ")
for i in l:
    count = 0
#for j in l: -> Bug: halghe jadid bade payan halghe ghabli ejra shavad
#bayad baraye har i kol list l ba j baresi konim,halghe jadid daron halghe ghabli bashe
    for j in l: 
        if j == i: 
            count +=1 
            if count > maxc:
                maxc = count
                word = i
print(f"{word}: {maxc}")
    
    
    
 