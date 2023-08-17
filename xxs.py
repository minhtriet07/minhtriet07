n=int(input("nhap so pt"))


a=[]

b=[]
for i in range (n):


    num=int(input('nhap pt thu'+str(i+1)+':'))


    a.append(num)
for i in range (len(a)):
    b.append(min(a))
    a.remove(min(a))
print(b)

    

