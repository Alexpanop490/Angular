import turtle as t
# set-up object
f = open('C:/Users/alex/Downloads/VScode/status.txt', mode = "r", encoding = 'UTF-8')
r = f.readlines()
count1 =  r.count('up')
count11 = r.count('up\n')
count2 =  r.count('down')
count21 = r.count('down\n')
count3 =  r.count('none')
count31 = r.count('none\n')
n = 1
count = count1+count11+count2+count21+count3+count31
print(r)
print(count1/1000,count11/1000,count2/1000,count21/1000,count3/1000,count31/1000)
print(count/1000)
i = 0
t.setheading(90)
t.title("Movement")
t.pencolor("red")
t.fillcolor("red")
for i in range (0,count):
    if r[i] == 'up':
      t.forward(count1/1000)
      i += 1
    elif r[i] == "up\n":
      t.forward(count11/1000)
      i += 1
    elif r[i] == "down":
      t.backward(count2/1000)
      i += 1
    elif  r[i] == 'down\n':
      t.backward(count21/1000)
      i += 1
    elif r[i] == "none" or r[i] == 'none\n':
      i += 1

 
