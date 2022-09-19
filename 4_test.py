# -*- coding: utf-8 -*-
#uses files
#4_test.py

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
rantime(4)

mdtest=hashlib.md5(open('4_test.py','rb').read()).hexdigest()

md=hashlib.md5(mdtest.encode('utf-8')).hexdigest()
fmd=open('files/md5.txt')
line=fmd.readline().split()
while line[0]!='4':
  line=fmd.readline().split()
if md!=line[1]:
  print('Аварийное завершение программы. Код ошибки 1001. Несанкционированное изменение программы')
  sys.exit(1001)
fmd.close()

d=0.6#edges density
mean=3#mean distance between vertex
p='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

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



def graph_print(g):
  n=len(g)
  print('    ',end='')
  for j in range(n):
    print(p[j],end='\t   ')
  print('\n','-'*(8*n-2))
  for j in range(n):
    print(p[j],end='')
    for k in range(n):
      if g[j][k]:
        print('  ',g[j][k],end='\t')
      elif j-k:
        print('   -',end='\t')
      else:
        print('  [x]',end='\t')
    print('\n','-'*(8*n-2))


def path(g):
  n=len(g)
  doit=1
  for i in range(n):
    doit*=(sum(g[i])>0)
  if doit==0:
    return(0)
  otm=[1]*n
  pth=[float('inf')]*n
  pth_str=['A']*n
  pth[0]=0
  while sum(otm):
    mxp=float('inf')
    now=0
    for i in range(n):
      if otm[i] and pth[i]<mxp:
        mxp=pth[i]
        now=i
    if mxp==float('inf'):
      return(0)
    if now==n-1:
      #print(pth_str,p)
      if len(pth_str[now])>2:
        graph_print(g)
      return([pth[now],pth_str[now]])
    otm[now]=0
    for i in range(n):
      if otm[i]:
        if g[now][i]:
          if pth[i]>pth[now]+g[now][i]:
            pth_str[i]=pth_str[now]+p[i]
          pth[i]=min(pth[i],pth[now]+g[now][i])
  return(0)

def gen_graph(n):
  #print(n,end='')
  while True:
    #print('c',end='')
    g=[[0 for i in range(n)] for j in range(n)]
    for j in range(n):
      for k in range(n):
        if k<j:
          g[j][k]=g[k][j]
        elif (j<k) and random()<d:
          for ix in range(k-j):
            g[j][k]+=1+int(random()*mean*(2+k-j))
    #print(g,end='')
    ng=path(g)
    if ng:
      return(ng)

def gen_prob(diff,sc):
  n=1
  lv=3+diff/2+sc/4
  r=[0,[]]
  while len(r[1])<3:
    while n<4:
      n=int((0.8+0.4*random())*lv)#vertex quantity
    #print(n,end='')
    r=gen_graph(n)
  print('\n')
  print('Самый кортокий путь из А в',p[n-1],'=',end=' ')
  return(r)

sc=0.0#scores
diff=0#difficulty
while diff<1 or diff>5:
  try:
    diff=int(input('Введите код работы (от 1 до 5)'))
  except ValueError:
    continue

minimtimefortask=60
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
    rantime(4)
    deltatime=randint(0,99)/100
  elif wronganswer:
    if thinkmore:
      print('Предлагаю Вам подумать подольше')
      thinkmore=False
    continue
  tmrnd=tmnow
  thinkmore=True
#logend
  right=gen_prob(diff,sc)
  ##validation
  acc=True
  while acc:
    answer=input().strip()
    acc=len(answer)
    for c in answer:
      acc-= c in '0123456789'
    txtanswer='Неверный формат ввода. Введите ответ ещё раз: '
  #print(answer)
  test+=1
  #diff=1+sc/2
  if int(answer)==right[0]:
    rightnum+=1
    print('Правильно. ')
    wronganswer=False#timeroption
    answers+=str(test)+'|'
    sc+=1
  else:
    acc=True
    txtanswer='Неправильно. Попробуйте ещё раз: '
    while acc:
      answer=input(txtanswer).strip()
      acc=len(answer)
      for c in answer:
        acc-= c in '0123456789'
      txtanswer='Неверный формат ввода. Введите ответ ещё раз: '
    sc=sc*(0.96-0.01*sc)
    if int(answer)==right[0]:
      rightnum+=1
      typo+=1
      print('Правильно. ')
      wronganswer=False#timeroption
      answers+=':%i:|'%test
      sc+=1
    else:
      print('Неправильно. Правильный ответ: %i (%s)'%(right[0],'-'.join(right[1])))
      wronganswer=True#timeroption
      answers+='*|'
      sc=sc*(0.94-0.01*sc)
  #print(rightnum)
  pright(rightnum,typo,test)
  print(answers)
  print('-'*30)
  print('балл = %g (код работы %i)'%(sc,diff))
  print('-'*30)

