#uses files
#101_test.py
#files/101_voc.txt
#files/101_games.txt

from random import randint,shuffle,choice
from time import time
import hashlib
import sys
import os
import shutil
mdtest=hashlib.md5(open('101_test.py','rb').read()).hexdigest()
mdtest+=hashlib.md5(open('files/101_games.txt','rb').read()).hexdigest()
mdtest+=hashlib.md5(open('files/101_voc.txt','rb').read()).hexdigest()
md=hashlib.md5(mdtest.encode('utf-8')).hexdigest()
fmd=open('files/md5.txt')

line=fmd.readline().split()
while line[0]!='101':
  line=fmd.readline().split()
if md!=line[1]:
  print('Аварийное завершение программы. Код ошибки 1001. Несанкционированное изменение программы')
  sys.exit(1001)

qabc='оеаинтсрвлкмдпуяыьгзбчйхжшюцщэфъё'
qlit=[10983, 8483, 7998, 7367, 6700, 6318, 5473, 4746, 4533, 4343, 3486, 3203, 2977, 2804, 2615, 2001, 1898, 1735, 1687, 1641, 1592, 1450, 1208, 966, 940, 718, 639, 486, 361, 331, 267, 37, 14]
fieldsize=5#field size
def rantime():
  s=str(time()).split('.')[1]
  f=open('files/log.log','a')
  f.write(s[1:]+'0'*(7-len(s)))
  f.close()

def choiceliter(l,abc):
  n=randint(1,sum(l))
  i=0
  while n>0:
    n-=l[i]
    i+=1
  return(abc[i-1])

def wordexist(word,field):
  chain=[]
  for i in range(fieldsize):
    for j in range(fieldsize):
      if word[0]==field[i][j]:
        chain.append([[i,j]])
  lw=1#index of liter
  while lw<len(word) and len(chain):
    newchain=[]
    for s in chain:
      last=s[-1]
      for i in range(max(0,last[0]-1),min(last[0]+1,fieldsize-1)+1):
        for j in range(max(0,last[1]-1),min(last[1]+1,fieldsize-1)+1):
          if (word[lw]==field[i][j]) and (not [i,j] in s):
            newchain.append(s+[[i,j]])
    chain=newchain.copy()
    lw+=1
  return([chain])

def printfield(field):
  for i in range(fieldsize):
    print(''.join(field[i]))

f=open('files/101_voc.txt')
voc=list(map(lambda s:s[:-1],f))
f.close()

f=open('files/101_games.txt')
games=list(map(lambda s:s[:-1],f))
f.close()

gm=-1
noch=''
rantime()
while True:
  tmrnd=time()
  gm=int(input('Введите код игры '+noch))
  noch='ещё раз '
  if 0<gm<len(games):
    break
  else:
    print('Некорректный код игры')

field=[[0]*fieldsize for i in range(fieldsize)]

cg=int(games[int(gm)].split()[0])
#!--preliminary field generation
for i in range(fieldsize):
  for j in range(fieldsize):
    field[i][j]=qabc[cg%len(qabc)]
    cg//=len(qabc)
printfield(field)
#print(mxscore)
score=0
penalty=0
noword=0
guessed=set()
added=[]
while True:
  a=input().strip()
  tmnow=time()
  if tmnow>tmrnd+1:
    rantime()
  tmrnd=tmnow
  if a.strip()=='':
    break
  if wordexist(a,field)!=[[]]:
    if not a in guessed:
      if  a in voc:
        score+=(len(a)-2)**2
        guessed.add(a)
      else:
        print("не знаю такого слова '%s'"%a)
        added.append(a)
        noword+=1
    else:
      print("уже писали слово '%s'"%a)
  else:
    print("нельзя составить слово '%s'"%a)
    penalty+=1
  print('-'*10)
  printfield(field)
  print('-'*10)
  print("score",score-penalty-noword*0.1)
