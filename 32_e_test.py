#uses files
#32_e_test.py

import random
import itertools
import hashlib
from random import randint,shuffle,choice
import sys
mdtest=hashlib.md5(open('32_e_test.py','rb').read()).hexdigest()
#mdtest+=hashlib.md5(open('32_test_servers.txt','rb').read()).hexdigest()

md=hashlib.md5(mdtest.encode('utf-8')).hexdigest()
fmd=open('files/md5.txt')
line=fmd.readline().split()
while line[0]!='32e':
  line=fmd.readline().split()
if md!=line[1]:
  print('Аварийное завершение программы. Код ошибки 1001. Несанкционированное изменение программы')
  sys.exit(1001)

def pright(n,t,num):
  print('-'*30)
  if (n%10==1) and (n%100!=11):
    print(n,'правильный, ',end='')
  else:
    print(n,'правильных, ',end='')
  if (t%10==1) and (t%100!=11):
    print(t,'опечатка ',end='')
  else:
    print(t,'опечаток ',end='')
  if (num%10==1) and (num%100!=11):
    print('из %i ответа'%num)
  else:
    print('из %i ответов'%num)
  print('-'*30)

sc=0.0#scores
diff=0#difficulty
while diff<1 or diff>5:
  try:
    diff=int(input('Выберите сложность от 1 до 5 (1 самый лёгкий)'))
  except ValueError:
    continue
test=0#test number
rightnum=0#right answers number
typo=0#misprints number
answers='|'#table of marks

while True:
  print('В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает, какая часть IP-адреса узла сети относится к адресу сети, а какая – к адресу узла в этой сети. Адрес сети получается в результате применения поразрядной конъюнкции к заданному IP-адресу узла и его маске. По заданным IP-адресу сети и адресу сети определите третий байт маски слева :\n')
  a=randint(0,255)
  b=randint(0,255)
  d=randint(0,255)
  z=randint(2,7)
  vrx='1'*8
  while 2-len(set(vrx[:z])) and (z>1):
    vrx=''
    for i in range(8):
      if z-i in [0,1]:
        vrx+='1'
      else:
        vrx+=str(randint(0,1))
  print('адрес сети: %i.%i.%i.0'%(a,b,int(vrx[:z]+'0'*(8-z),2)))
  print('адрес узла: %i.%i.%i.%i'%(a,b,int(vrx,2),d))
  answer=int(input('маска сети (запишите десятичное число):'))
  ##validation  
  test+=1
  right=int('1'*z+'0'*(8-z),2)
  if answer==right:
    rightnum+=1
    print('Правильно. ')
    answers+=str(test)+'|'
    sc+=1
  else:
    answer=int(input('Неправильно. Попробуйте ещё раз: ').strip().upper())
    sc=sc*(0.9-diff*0.02)
    if answer==right:
      rightnum+=1
      typo+=1
      print('Правильно. ')
      answers+=':%i:|'%test
      sc+=1
    else:
      print('Неправильно. Правильный ответ:',right)
      answers+='*|'
      sc=sc*(0.9-diff*0.02)
  #print(rightnum)
  pright(rightnum,typo,test)
  print(answers)
  print('балл = %g (сложность %i)'%(sc,diff))
