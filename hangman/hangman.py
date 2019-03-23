import random
import sys
import string

def sports():
    f = open("sports.txt","r")
    a=random.randint(0, 4)

    for i in range (a):
        f.readline()
    s=f.readline()
    f.close()
    word=s.split(":")

    return word[0],word[1]
  
def country():
    f = open("country.txt","r")
    a=random.randint(0, 4)

    for i in range (a):
        f.readline()
    s=f.readline()
    f.close()
    word=s.split(":")

    return word[0],word[1]
def fruits():
    f = open("fruits.txt","r")
    a=random.randint(0, 4)

    for i in range (a):
        f.readline()
    s=f.readline()
    f.close()
    word=s.split(":")

    return word[0],word[1]


print ("Select Category:\n")
print ("Sports")
print ("Country in the world")
print ("Fruit")

key = input ("Please select a catagory : ")

if key=="1":
    key,hint=sports()
elif key=="2":
    key,hint=country()
elif key=="3":
    key,hint=fruits()
else :
    print ("Wrong input")
    sys.exit()


print("Hint : "+hint)
wrong,ans2="",""
count=10

while(count>0):
    st=""
    fail,score=0,0
    for i in key:
        if i in ans2:
            st=st+i+" "
            score=score+1
        elif i==" ":
            st=st+" "
        elif i in "0123456789" or i in string.punctuation:
            st=st+i+" "
        else:
            st=st+"- "
            fail=fail+1
    print (st+"        score "+str(score)+" , remaining guess "+str(count)+",  wrong guessed :"+wrong)

    if fail==0:
        print ("You Won")
        break
        
    ans=input("> :").lower()
    ans2=ans2+ans

    if ans not in key:
        count=count-1
        wrong=wrong+ans+" "
        if count==0:
            print ("You lose")
            break
