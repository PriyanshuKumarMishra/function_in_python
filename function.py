def ask_question(k):
        print(k)
ask_question('ek baar')
ask_question('ek baar')
ask_question('ek baar')
ask_question('ek baar')
ask_question('ek baar')
###############################################
def ask_question(k):
    b=0
    while b<100:
        print(k)
        b+=1
ask_question('ek baar')
###################################################
def function_print_lines(a,k):
    print(a,'\n',k)
function_print_lines('mera naam abhishek hai','mein navgurukul ka founder hu')
###################################################
def list_of_students_name(k):
    print(k)
list_of_students_name('kutta')
################################################
def list_of_students_name(k,l):
    print(k,l)
list_of_students_name('hello','suresh')
#####################################################
def add_numbers(number1,number2):
    print(number1+number2)
add_numbers(1234,123) 
#######################################################
def add_numbers_list(k,l):
    for i in k:
        for f in l:
            if l.index(f)== k.index(i):
                print(i+f)
a= [50, 60, 10]
b= [10, 20, 13]
add_numbers_list(a,b)
#########################################################
def check_numbers(k,l):
    if k%2==0 and l%2==0:
        print('dono even hai')
    else:
        print('dono even nahi h')
check_numbers(11,23)
########################################################
def check_numbers(k,l):
    if k%2==0 and l%2==0:
        print('dono even hai')
    else:
        print('dono even nahi h')
def  check_numbers_list(p,q):
    for i in p:
        for j in q:
            if p.index(i)== q.index(j):
                check_numbers(i,j)
a=[2, 6, 18, 10, 3, 75]
b=[6, 19, 24, 12, 3, 87]
check_numbers_list(a,b)
##########################################################
def calculator(a,b,c):
    if c=='-':
        sum=a-b
        return sum
    elif c=='+':
        sum=a+b
        return sum
    elif c=='/':
        sum=a/b
        return sum
    elif c=='*':
        sum=a*b
        return sum
a,b,c=int(input()),int(input()),input()
d=calculator(a,b,c)
print(d)
######################################################
def calculator(a,b,c):
    if c=='-':
        sum=a-b
        return sum
    elif c=='+':
        sum=a+b
        return sum
    elif c=='/':
        sum=a/b
        return sum
    elif c=='*':
        sum=a*b
        return sum
a,b=int(input()),int(input())
ar=calculator(a,b,'+')
sr=calculator(a,b,'-')
mr=calculator(a,b,'*')
dr=calculator(a,b,'/')
print(ar,sr,mr,dr)
########################################
def list_change(a,b):
    c=[]
    for i in a:
        for k in b:
            if a.index(i)==b.index(k):
                d=i*k
                c.append(d)
    return c
multiple_list = list_change([5, 10, 50, 20], [2, 20, 3, 5])
print(multiple_list)
##############################################
def eligible_for_vote(k):
    if k>=18:
        print('yes you are eligible voting')
    else:
        print('no you are not eligible for voting')
a=int(input())
eligible_for_vote(a)
################################################
def perfect(a):
    b=0
    for i in range(1,a):
        if a%i==0:
            b+=i
    if b==a:
        print('yes its a perfect no.')
    else:
        print('naah its not a perfect no.')
a=int(input())
perfect(a)
#################################################
def perfect_no(a):
    for k in range(1,a):
        b=0
        for i in range(1,k):
            if k%i==0:
                b+=i
        if b==k:
            print(k)
perfect_no(10000)
#################################################
def average(a,b,c):
        d=a+b+c
        d=d/3
        return d
b=average(1,2,3)
print(b)
################################################
def showNumber(a):
    for i in range(0,a+1):
        if i%2==0:
            print(i,'is even no.')
        else:
            print(i,'is odd no.')
showNumber(10)
##############################################
def lalala(a):
    b=0
    for i in range(a+1):
        if i%3==0 or i%5==0:
            b+=i
    return b
d=lalala(10)
print(d)
##############################################
def speedometer(k):
    if k<=70:
        print('ok')
    else:
        a=k-70
        b=a//5
        if b>12:
            print(b,'liscence suspend')
        else:
            print(b,'mind your speed')
speedometer(150)
#############################################
def leat(k,l):
    if len(k)>len(l):
        print(k)
    elif len(l)>len(k):
        print(l)
    else:
        print(k,'\n',l)
leat('darkdk','kklkl')
##############################################
def la(k):
    a={}
    for i in range(1,k+1):
        a[i]=i**2
    return a
b=la(20)
print(b)
###############################################
print('meraki ends here ')
############################################
def pal(k):
    if k==k [::-1]:
        print('yes')
k='hoh'
pal(k)
##############################################
def local(a):
    if a<5:
        print(a)
        local(a+1)
    else:
        print('its over')
local(1)
#########################################
# :::::::::::::::::::::::::::::::::::::::::::::::::;: