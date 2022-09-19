# -*- coding: utf-8 -*-
#uses files
#7_test.py
#files/vocqast.txt

#charcoding='utf'#win | utf

from random import randint,shuffle,choice,expovariate,random
import hashlib
import sys
import os
from time import time
def rantime(n):
  if 2<n<7:
    s=str(time()).split('.')[1]
    s+='0'*(7-len(s))
    f=open('files/log.log','a')
    f.write(s[7-n])
    f.close()
rantime(6)

abc='АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

mdtest=hashlib.md5(open('7_test.py','rb').read()).hexdigest()
mdtest+=hashlib.md5(open('files/vocqast.txt','rb').read()).hexdigest()

md=hashlib.md5(mdtest.encode('utf-8')).hexdigest()
fmd=open('files/md5.txt')
line=fmd.readline().split()
while line[0]!='7':
  line=fmd.readline().split()
if md!=line[1]:
  print('Аварийное завершение программы. Код ошибки 1001. Несанкционированное изменение программы')
  sys.exit(1001)
fmd.close()

def pright(n,t,num):
  #print('-'*30)
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
  #print('-'*30)

def cesar(w,abc,step=1):
  s=''
  for c in w.upper():
    p=abc.find(c)
    if p<0:
      print('\nError char "%s" is not in abc'%c)
    else:
      s+=abc[(p+step)%(len(abc))]
  return(s)

fop=open('files/vocqast.txt','r')
voc=list(map(lambda s:s.strip(),fop))
##ftr.close()
##fop.close()

def gen_prob(var,sc,diff=0):#problem generation
  lngth=len(voc)
  if var==1:
    wp=choice(voc[int(min(0.7,sc/20)*lngth):int((0.2+sc/8)*lngth)])
    print('Используя шифр Цезаря с единичным смещением зашифруйте слово "%s"'%wp)
    print('Русский алфавит:',abc)
    return(cesar(wp,abc))
  elif var==2:
    s=choice(voc[int(min(0.7,sc/20)*lngth):int((0.2+sc/8)*lngth)])
    wp=''
    for c in s:
      if sc*random()<5:
        wp+=c
      else:
        wp+=choice(abc)
    print('С помощью шифра Цезаря с единичным смещением зашифровали некоторое сообщение. В результате получилось "%s". Напишите зашифрованное сообщение.'%cesar(wp,abc))
    print('Русский алфавит:',abc)
    return(wp.upper())
  else:
    print('\nError no %i variant')
sc=0.0#scores
diff=0#difficulty
numvar=2
while diff<1 or diff>2**numvar-1:
  try:
    diff=int(input('Введите код работы (от 1 до %i)'%(2**numvar-1)))
  except ValueError:
    continue
vardiff=list({i*int(bin(16+diff)[7-i]) for i in range(1,5)}-{0})
#diff=sum([diffval[i-1] for i in vardiff])

minimtimefortask=30
deltatime=randint(0,99)/100
tmrnd=0
wronganswer=thinkmore=True#timelogger

test=0#test number
rightnum=0#right answers number
typo=0#misprints number
answers='|'#table of marks

while True:
#logbegin
  tmnow=time()
  #print(tmnow,tmrnd+minimtimefortask+deltatime)
  if tmnow>tmrnd+minimtimefortask+deltatime:
    rantime(6)
    deltatime=randint(0,99)/100
  elif wronganswer:
    if thinkmore:
      print('Предлагаю Вам подумать подольше')
      thinkmore=False
    continue
  tmrnd=tmnow
  thinkmore=True
#logend
  right=gen_prob(choice(vardiff),sc,diff)
  ##validation
  acc=True
  txtanswer='Ваш ответ: '
  while acc:
    answer=input(txtanswer).strip().upper()
    acc=len(answer)
    for c in answer:
      acc-= c in abc
    txtanswer='Неверный формат ввода. Введите ответ ещё раз: '
  #print(answer)
  test+=1
  diff=1+sc/2
  if answer==right:
    rightnum+=1
    print('Правильно. ')
    wronganswer=False#timeroption
    answers+=str(test)+'|'
    sc+=1
  else:
    acc=True
    txtanswer='Неправильно. Попробуйте ещё раз: '
    while acc:
      answer=input(txtanswer).strip().upper()
      acc=len(answer)
      for c in answer:
        acc-= c in abc
      txtanswer='Неверный формат ввода. Введите ответ ещё раз: '
    sc=sc*(0.96-0.01*sc)
    if answer==right:
      rightnum+=1
      typo+=1
      print('Правильно. ')
      wronganswer=False#timeroption
      answers+=':%i:|'%test
      sc+=1
    else:
      print('Неправильно. Правильный ответ: ',right)
      wronganswer=True#timeroption
      answers+='*|'
      sc=sc*(0.94-0.01*sc)
  #print(rightnum)
  pright(rightnum,typo,test)
  print(answers)
  print('-'*30)
  print('балл = %g (код работы %i)'%(sc,diff))
  print('-'*30)
