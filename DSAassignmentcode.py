#Libraries to be imported :

import numpy as np

#Utility funtions

def mahantan(x,y):
    dis=0
    s1=[]
    output=[]
    #X-- is the workers
    #y-- is bikes
    for i in x:
        for j in y:
            dis=i-j
            #print(i,"-",j,"=",dis)
            s1.append(abs(sum(dis)))
            #print("s1:",s1)
    s2=s1[2:]
    s1=s1[0:2]
    #print("=======")
    #print("s1:", s1,"s2:",s2)
    for i in range(len(s1)):
        if s1[i]>s2[i]:
            if 1 not in output:
                output.append(1)
            else:
                output.append(0)
        else:
            output.append(0)

    print("Output",output)
    return output

#Input formate
wo=[]
n=int(input("Enter the number of workers:"))
for i in range(n):
    o=list(map(int,input().split(',')))
    wo.append(o)
n1=int(input("enter the number of bikes:"))
bi=[]
for i in range(n1):
    o=list(map(int,input().split(',')))
    bi.append(o)
#Converting them into arrays
wo=np.array(wo)
bi=np.array(bi)

#Printing the input section
print("Input:","\n","=======")
print("workers",wo)
print("bikes",bi)

#Main code section

mahantan(wo,bi)




