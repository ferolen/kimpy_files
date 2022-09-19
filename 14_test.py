#uses files
#14_test.py
#files/isp.txt

import itertools
from random import randint,shuffle,choice
import hashlib
import sys
from time import time
def rantime(n):
  if 2<n<7:
    s=str(time()).split('.')[1]
    s+='0'*(7-len(s))
    f=open('files/log.log','a')
    f.write(s[7-n:])
    f.close()
rantime(6)

mdtest=hashlib.md5(open('14_test.py','rb').read()).hexdigest()
mdtest+=hashlib.md5(open('files/isp.txt','rb').read()).hexdigest()
md=hashlib.md5(mdtest.encode('utf-8')).hexdigest()
fmd=open('files/md5.txt')

line=fmd.readline().split()
while line[0]!='14':
  line=fmd.readline().split()
if md!=line[1]:
  print('Аварийное завершение программы. Код ошибки 1001. Несанкционированное изменение программы')
  sys.exit(1001)
fmd.close()

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

def f(n,numop,param):
  if n<0 or n>1000:
    return(-1)
  r=-1
  if numop==0:
    r=n-param
  if numop==1:
    r=n+param
  if numop==2:
    r=n*param
  if numop==3:
    if n%param:
      r=-1
    else:
      r=n//param
  if numop==4:
    if n<10:
      r=-1
    else:
      r=n//10
  if numop==5:
    if n<10:
      r=-1
    else:
      r=int(str(n)[1:])
  if numop==6:
    r=n*n
  if numop==7:
    r=int(str(n)[::-1])
  if numop==8:
    r=1
    for i in list(str(n)):
      r*=int(i)
  if r<0 or r>1000:
    return(-1)
  else:
    return(r)

def genbin(n):#generation of all binary seq
  nl=['']
  a=0
  while a<n:
    nl+=[c+'1' for c in nl]+[c+'2' for c in nl]
    nl=list(set(nl))
    a+=1
  nl.sort()
  return(nl[1:])

def randflist(l):#probabilty density l
  n=randint(1,sum(l))
  i=0
  while True:
    if n-l[i]<=0:
      break
    n-=l[i]
    i+=1
  return(i)

def fprog(prog,firstop,firstpar,secop,secpar,num):#calculates result program = prog for number = num
  beginum=num
  for c in prog:
    if c=='1':
      beginum=f(beginum,firstop,firstpar)
    else:
      beginum=f(beginum,secop,secpar)
  return(beginum)

def equch(l):# 1 - if all command in l are same, 0 if there are different
  f=1
  if len(l)<2:
    return(f)
  for i in range(1,len(l)-1):
    f*=(l[i]==l[i-1])
  return(f)
    
op=['вычти','прибавь','умножь на','подели на','зачеркни справа','зачеркни слева','возведи в квадрат','запиши наоборот','запиши произведение цифр']
opout1=['уменьшает число на экране на','увеличивает число на экране на','умножает число на экране на ','делит число на экране (если оно делится) на','убирает у числа на экране одну цифру справа','убирает у числа на экране одну цифру слева','возводит число на экране во вторую степень','записывает число на экране в обратном порядке','заменяет число на экране на произведение его цифр']
opout2=['уменьшает его на','увеличивает его на','умножает его на ','делит его (если оно делится) на','убирает у него одну цифру справа','убирает у него одну цифру слева','возводит его во вторую степень','записывает его в обратном порядке','заменяет его на произведение цифр']
diapopfrom=[0,0,1,1,0,0,0,0,0]#diapason of param for op from (-1)
diapop=[9,9,4,4,1,1,1,1,1]#diapason of param for op to
exeptop=[[0,1],[2,3],[2,6],[3,6]]
fr=[11,12,8,5,3,3,6,3,1]#operation frequency
fisp=open('files/isp.txt','r')
isp=list(map(lambda s:s[:-1],fisp))
fisp.close()

#isp=[]

#-------------------------------------------------------------------------
#-------------------------------------------------------------------------

sc=0.0#scores
diff=0#difficulty
while diff<1 or diff>5:
  try:
    diff=int(input('Выберите сложность от 1 до 5 (1 самый лёгкий)'))
  except ValueError:
    continue
minimtimefortask=60
deltatime=randint(0,99)/100
tmrnd=0
wronganswer=thinkmore=True
test=0#test number
rightnum=0#right answers number
typo=0#misprints number
answers='|'#table of marks
while True:
  pbn=randint(2,100)#input number
  numcom=randflist([15-3*diff,50+3*diff,5+3*diff])+4#maximum number of comand in prog
  prog=genbin(numcom)#list of all instructions
  uni=set()#unic values
  rep={-1}#repeated values
  firstop=secop=randflist(diapop)
  ispolnitel=[]
  while secop==firstop or ([secop,firstop] in exeptop):#choose the operations for executor
    secop=randflist(diapop)
    if secop>firstop:
      secop,firstop=firstop,secop
  if randint(0,1):
    secop,firstop=firstop,secop
  firstpar=randint(1,diapop[firstop])+diapopfrom[firstop]
  secpar=randint(1,diapop[secop])+diapopfrom[secop]

  for pr in prog:
    num=fprog(pr,firstop,firstpar,secop,secpar,pbn)
    if num in uni:
      rep.add(num)
    else:
      uni.add(num)
  uni-=rep

  answ=[]
  for pr in prog:
    if len(pr)>3:
      num=fprog(pr,firstop,firstpar,secop,secpar,pbn)
      if (1<num<1000) and (num in uni):
        answ.append(pr)
  if len(answ)<3:
    continue

  progch=examprog=choice(list(answ))
  quaex=100#number of trying
  while quaex:
    quaex-=1    
    examprog=choice(list(answ))
    pexamp=randint(2,100)#input number for explanation test
    numex=fprog(examprog,firstop,firstpar,secop,secpar,pexamp)
    if 0<numex<100:
      break
  if progch==examprog:
    continue
  numch=fprog(progch,firstop,firstpar,secop,secpar,pbn)
  if numch>99 or equch(progch) or equch(examprog):
    continue
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
# problem text output
  print('#%i'%test)
  if not ispolnitel:
    ispolnitel=isp.copy()
    shuffle(ispolnitel)
  ispitem=ispolnitel.pop()
  print('У исполнителя %s две команды, которым присвоены номера:'%choice(isp))
  fops=op[firstop]
  seps=op[secop]
  if firstop<4:
    fops+=' '+str(firstpar)
  if secop<4:
    seps+=' '+str(secpar)
  print('1. %s\n2. %s'%(fops,seps))
  ex='(Например, %s — это алгоритм: '%examprog
  for c in examprog:
    if c=='1':
      ex+=fops+', '
    else:
      ex+=seps+', '
  ex+='который преобразует число %d в число %d.)'%(pexamp,numex)
  fops=opout1[firstop]
  seps=opout2[secop]
  if firstop<4:
    fops+=' '+str(firstpar)
  if secop<4:
    seps+=' '+str(secpar)
  fromnum=''
  if numch == pbn:
    fromnum='не менее 3 и '
  print('Первая из них %s, вторая %s. Исполнитель работает только с натуральными числами. Составьте алгоритм, получающий из числа %d число %d и содержащий %sне более %d команд. В ответе запишите только номера команд.\n %s Если таких алгоритмов более одного, то запишите любой из них.'%(fops,seps,pbn,numch,fromnum,numcom,ex))
  right=progch
  print('Ваш ответ (без пробелов):',end='')
  ##validation  
  answer=input().strip().upper()
  #print(answer)
  test+=1
  if answer==right:
    rightnum+=1
    print('Правильно. ')
    wronganswer=False
    answers+=str(test)+'|'
    sc+=1
  else:
    answer=input('Неправильно. Попробуйте ещё раз:').strip().upper()
    sc=sc-(0.3+0.1*diff)*sc/5
    if answer==right:
      rightnum+=1
      typo+=1
      print('Правильно. ')
      wronganswer=False
      answers+=':%i:|'%test
      sc=max(sc+1,0)
    else:
      print('Неправильно. Правильный ответ:',right)
      wronganswer=True
      answers+='*|'
      sc=max(sc-(0.5+0.1*diff)*sc/5,0)
  #print(rightnum)
  pright(rightnum,typo,test)
  print(answers)
  print('балл = %g  (сложность %i)'%(sc,diff))
