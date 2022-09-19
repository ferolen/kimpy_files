#uses files
#17_b_test.py
#files/names_skl.txt

import itertools
from random import randint,shuffle,choice,random
import hashlib
import sys
from time import time
def rantime(n):
  if 2<n<7:
    s=str(time()).split('.')[1]
    s+='0'*(7-len(s))
    f=open('files/log.log','a')
    f.write(s[7-n])
    f.close()
rantime(6)

mdtest=hashlib.md5(open('17_b_test.py','rb').read()).hexdigest()
mdtest+=hashlib.md5(open('files/names_skl.txt','rb').read()).hexdigest()
md=hashlib.md5(mdtest.encode('utf-8')).hexdigest()
fmd=open('files/md5.txt')

line=fmd.readline().split()
while line[0]!='17b':
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

def mulct(part):
  mul=[0.15,0.08,0.04]
  return(mul[part-2])

def check(ip):#validate ip
  n=1# validate for x.0x.x
  ipn=ip.split('.')
  if (min(list(map(len,ip.split('.'))))>0)and(max(list(map(int,ip.split('.'))))<256):
    for s in ipn:
      if (s[0]=='0') and len(s)>1:
        return(0)
    return(1)
  else:
    return(0)

names=list(map(lambda s:s[:-1],open('files/names_skl.txt','r')))
piece=['','','три обрывка','четыре обрывка','пять обрывков','шесть обрывков']
abc='ABCDEFG'
sc=0.0#score
diff=0#difficulty
while diff<1 or diff>5:
  try:
    diff=int(input('Выберите сложность от 1 до 5 (1 - самый лёгкий)'))
  except ValueError:
    continue

minimtimefortask=20
deltatime=randint(0,99)/100
tmrnd=0
wronganswer=thinkmore=True#timelogger

test=0#test number
rightnum=0#right answers number
typo=0#misprints number
answers='|'#table of marks

while True:
  p=1/(1+sc*(diff+1)/8)
  r=random()
  part=2+(p**2<r)+(p*(2-p)<r)#number of piece -1
  m=0
  while m!=1:
    per=[i for i in range(part+1)]
    ipt=[str(randint(0,255)) for i in range(4)]
    s='.'.join(ipt)
    #print(s)
    for i in range(part):
      insr=randint(1,len(s)-1)
      s=s[:insr]+':'+s[insr:]
    ipt=s.split(':')
    shuffle(ipt)
    if min(list(map(len,ipt))):
      m=0
      for ps in list(itertools.permutations(per)):
        n=0
        ipn=''
        for i in ps:
          ipn+=ipt[i]
        if check(ipn):
          m+=1
          #print(ipn,ps)
          out='\t'.join(ipt)+'\t'
          right=''
          for i in ps:
            right+=abc[i]
  #print(out,ipt)
  test+=1
  name=choice(names).split()
  name.insert(2,name[0])
  if len(name)<4:
    name.append('')
  name.append(piece[part])
  name.append(', '.join(list(abc[:part]))+' и '+abc[part])
  #print(name)
  name.insert(1,name[3])
  name.insert(1,name[1])
  paramtup=tuple(name)
#logbegin
  tmnow=time()
  #print(tmnow,tmrnd+minimtimefortask+deltatime)
  if tmnow>tmrnd+minimtimefortask+deltatime:
    rantime(5)
    deltatime=randint(0,99)/100
  elif wronganswer:
    if thinkmore:
      print('Предлагаю Вам подумать подольше')
      thinkmore=False
    continue
  tmrnd=tmnow
  thinkmore=True
#logend    
  print('#%i'%test)
  print('%s записал%s IP-адрес некоторого сервера на листке бумаги и положил%s его в карман куртки. %s мама случайно постирала куртку вместе с запиской. После стирки %s обнаружил%s в кармане %s с фрагментами IP-адреса. Эти фрагменты обозначены буквами %s:'%paramtup)
  lmx=max(map(len,ipt))+2
  print('%s\n|'%('-'*((lmx+1)*len(ipt)+1)),end='')
  for i in range(part+1):
    lftsp=(lmx-len(ipt[i]))//2#left space
    rghtsp=(lmx-len(ipt[i])+1)//2#right space
    print('%s%s%s'%(' '*lftsp,ipt[i],' '*rghtsp),'|',sep='',end='')
  print('\n%s\n|'%('-'*((lmx+1)*len(ipt)+1)),end='')
  for i in range(part+1):
    lftsp=(lmx-1)//2#left space
    rghtsp=lmx//2#right space
    print('%s%s%s'%(' '*lftsp,abc[i],' '*rghtsp),'|',sep='',end='')
  print('\n%s\n'%('-'*((lmx+1)*len(ipt)+1)),end='')

  print('Ответ:',end='')
  ##validation  
  answer=input().strip().upper()
  #print(answer)
  if answer==right:
    rightnum+=1
    print('Правильно. ')
    wronganswer=False#timeroption
    answers+=str(test)+'|'
    sc+=1
  else:
    answer=input('Неправильно. Попробуйте ещё раз:').strip().upper()
    sc=sc*(1-mulct(part))
    if answer==right:
      rightnum+=1
      typo+=1
      print('Правильно. ')
      wronganswer=False#timeroption
      answers+=':%i:|'%test
      sc=max(0,sc+1)
    else:
      print('Неправильно. Правильный ответ:',right)
      wronganswer=True#timeroption
      answers+='*|'
      sc=max(sc*(1-2*mulct(part)),0)
  #print(rightnum)
  pright(rightnum,typo,test)
  print(answers)
  print('балл = %g (сложность %i)'%(sc,diff))
