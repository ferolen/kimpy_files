#uses files
#16test_b.py

from random import randint,shuffle,choice,random
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

mdtest=hashlib.md5(open('16_b_test.py','rb').read()).hexdigest()
md=hashlib.md5(mdtest.encode('utf-8')).hexdigest()
fmd=open('files/md5.txt')

line=fmd.readline().split()
while line[0]!='16b':
  line=fmd.readline().split()
if md!=line[1]:
  print('Аварийное завершение программы. Код ошибки 1001. Несанкционированное изменение программы')
  sys.exit(1001)

buset='ABCDEH'
length=4#chain length

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

def randflist(l):#probabilty density l
  n=randint(1,sum(l))
  i=0
  while True:
    if n-l[i]<=0:
      break
    n-=l[i]
    i+=1
  return(i)

def go(ch,l,st):#chain ch satisfies the condition
  rtrn=True
  if ch[l[0]] in st[l[0]]:
    for i in range(1,length):
      rtrn=rtrn and (ch[l[i-1]]!=ch[l[i]]) and (ch[l[i]] in st[l[i]])
  else:
    rtrn=False
  return(rtrn)

pr1=['в начале', 'на втором месте', 'на третьем месте', 'в конце']
pr2=['цепочки стоит', '—']
pr3=['которой нет', 'не стоящая']
pr4=['на первом месте', 'на втором месте', 'на третьем месте', 'на последнем месте']
l=[0,1,2,3]

#-------------------------------------------------------------------------
#-------------------------------------------------------------------------

sc=0.0#scores
diff=0#difficulty
while diff<1 or diff>5:
  try:
    diff=int(input('Выберите сложность от 1 до 5 (1 - самый лёгкий)'))
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
numtask=0#number of task
while True:
  numtask+=1
  shuffle(l)
  var=randflist([0,0,0,0,0,0,1,3,12,5,1])+int(0.3*diff*random())#chain quantity
  right=randint(0,var)
  st=[]
  for i in range(length):
    n=randflist([0,0,1,50,5])
    bu=list(buset)
    shuffle(bu)
    bu=bu[:n]
    bu.sort()
    st.append(''.join(bu))
  #print(st,l)
  rch,wch=0,0#right,wrong chain
  rightchset=set()#set of right chain
  chset=set()#set of chaines
  while (rch<right) or (wch<var-right):
    ch=''
    for i in range(length):
      ch+=choice(list(buset))
    if not ch in chset:
      if go(ch,l,st):
        if rch<right:
          chset.add(ch)
          rightchset.add(ch)
          rch+=1
      else:
        if wch<var-right:
          chset.add(ch)
          wch+=1
  #print(chset)
  chsetout=list(chset)
  shuffle(chsetout)
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
  print('#%i\nЦепочка из четырёх бусин, помеченных латинскими буквами, формируется по следующему правилу:\n'%numtask)
  print('— %s цепочки стоит одна из бусин %s\n'%(pr1[l[0]],', '.join(list(st[l[0]]))))
  for i in range(1,length):
    no=pr3[(i+1)//length]
    print('— %s — одна из бусин %s, %s %s\n'%(pr1[l[i]],', '.join(list(st[l[i]])),no,pr4[l[i-1]]))
  print('Определите, сколько из перечисленных цепочек созданы по этому правилу?\n')
  print('\t%s\n'%'   '.join(chsetout))
  print('Ответ:',end='')
  answer=input().strip()
  #print(answer)
  test+=1
  if answer==str(right):
    wronganswer=False
    rightnum+=1
    print('Правильно. ')
    sc+=1
    answers+=str(test)+'|'
  else:
    sc=sc*(0.94-0.01*diff)
    answer=input('Неправильно. Попробуйте ещё раз:').strip()
    if answer==str(right):
      rightnum+=1
      typo+=1
      print('Правильно. ')
      wronganswer=False
      sc=max(0,sc+1)
      answers+=':%i:|'%test
    else:
      print('Неправильно. Правильный ответ:',right,end='\n')
      wronganswer=True
      if right:
        print('Правильные цепочки: ',end='')
        chnum=0
        for chainow in chsetout:
          chnum+=1
          if chainow in rightchset:
            print('%s[#%i]'%(chainow,chnum),end=' ')
      sc=max(0,sc*(0.94-0.01*diff))
      answers+='*|'
  #print(rightnum)
  print()
  pright(rightnum,typo,test)
  print(answers)
  print('балл =%g (сложность %i)'%(sc,diff))
