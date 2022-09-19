#uses files
#32_d_test.py

import random
import itertools
import hashlib
from random import randint,shuffle,choice
import sys
mdtest=hashlib.md5(open('32_d_test.py','rb').read()).hexdigest()
#mdtest+=hashlib.md5(open('17_test_servers.txt','rb').read()).hexdigest()

md=hashlib.md5(mdtest.encode('utf-8')).hexdigest()
fmd=open('files/md5.txt')
line=fmd.readline().split()
while line[0]!='32d':
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

def ip(adress):
  ipout=''
  for i in range(3):
    ipout+=str(int(adress[i*8:i*8+8],2))+'.'
  ipout+=str(int(adress[24:],2))
  return(ipout)
  
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
  print('В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает, какая часть IP-адреса узла сети относится к адресу сети, а какая – к адресу узла в этой сети. Адрес сети получается в результате применения поразрядной конъюнкции к заданному IP-адресу узла и его маске. По заданным IP-адресу сети и маске определите адрес сети:\n')
  mask=random.randint(4,10)+random.randint(4,10)
  if mask==16:
    mask=13
  mask='1'*(32-mask)+'0'*mask
  ver=net=''
  for k in range(32):
    if random.random()<0.5:
      ver+='0'
    else:
      ver+='1'
    net+=str(int(ver[k])*int(mask[k]))
  print('IP-адрес:',ip(ver))
  print('маска:',ip(mask))
  right=ip(net)
  print('адрес сети: ',end='')
  ##validation  
  answer=input().strip()
  #print(answer)
  test+=1
  if answer==ip(net):
    rightnum+=1
    print('Правильно. ')
    answers+=str(test)+'|'
    sc+=1
  else:
    answer=input('Неправильно. Попробуйте ещё раз: ').strip().upper()
    sc=sc*(0.95-diff*0.01)
    if answer==ip(net):
      rightnum+=1
      typo+=1
      print('Правильно. ')
      answers+=':%i:|'%test
      sc+=1
    else:
      print('Неправильно. Правильный ответ:',ip(net))
      answers+='*|'
      sc=sc*(0.94-diff*0.02)
  #print(rightnum)
  pright(rightnum,typo,test)
  print(answers)
  print('балл = %g (сложность %i)'%(sc,diff))
