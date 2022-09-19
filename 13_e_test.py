#uses files
#13_e_test.py

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

mdtest=hashlib.md5(open('13_e_test.py','rb').read()).hexdigest()
#mdtest+=hashlib.md5(open('13_test_servers.txt','rb').read()).hexdigest()
md=hashlib.md5(mdtest.encode('utf-8')).hexdigest()
fmd=open('files/md5.txt')

line=fmd.readline().split()
while line[0]!='13e':
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

def scoresult(srez,diff):
  summa=0
  for i in diffdef:
    summa+=srez[i]
  return(summa)

def ma(sc,diff):#choice number
  if diff>3:
    return(randint(int(50+(20+30*sc)/2*(len(bin(diff))-2)**0.5),int(100+(40+50*sc)/2*(len(bin(diff))-2)**0.5)))
  else:
    return(randint(20+int(15*sc),50+int(25*sc)))

numvartest=7#number variant test
dgt='0123456789abcdef'
srez=[0]*numvartest
minimtimefortask=60
deltatime=randint(0,99)/100
base=[2,8,16]
numtest=20
n=0
sc=0.0#scores
diff=0#difficulty 1 - only (2)2dec, 2 - dec2(2) 4 - (any<10)2dec, 8 - dec2(any<10)
#16 + (any>10)2dec, 32 - dec2(any>10), 64 - (any from[2,8,16])2(any from[2,8,16])
while diff<1 or diff>127:
  try:
    diff=int(input('Введите код работы от 1 до 127 '))
  except ValueError:
    continue
n=diff
diffdef=[]
diffstr=''
for i in range(numvartest):
  diffstr+=str(n%2)
  if n%2:
    diffdef.append(len(diffstr)-1)
  n//=2
print('Переведите числа из одной системы счисления в другую. Основание системы счисления в ответе писать не надо.\n')
tmrnd=0
test=0#test number
rightnum=0#right answers number
typo=0#misprints number
answers='|'#table of marks
variant=0
wronganswer=thinkmore=True
while True:
  tmnow=time()
  if tmnow>tmrnd+minimtimefortask+deltatime:
    rantime(6)
    deltatime=randint(0,99)/100
  elif wronganswer:
    if thinkmore:
      print('Предлагаю Вам подумать подольше')
      thinkmore=False
    continue
  tmrnd=tmnow
  sc=min([srez[i]+(1-int(diffstr[i]))*1000 for i in range(numvartest)])
  #choose test variant
  srz_choice=[]
  for i in diffdef:
    if srez[i]<=abs(sc)*1.5:
      srz_choice.append(i)
  if srz_choice:
    variant=choice(srz_choice)
  else:
    variant=choice(diffdef)
  #choose test variant
  if variant==0:
    b=2
    m=a=ma(sc,diff)
    answ=''
    while m:
      answ=dgt[m%b]+answ
      m//=b
    print(answ,'_',b,'=?x_10',sep='')
    answ=str(a)
  elif variant==1:
    b=2
    m=a=ma(sc,diff)
    answ=''
    while m:
      answ=dgt[m%b]+answ
      m//=b
    print(a,'_10=?x_',b,sep='')
  if variant==2:
    b=randint(3,9)
    m=a=ma(sc,diff)
    answ=''
    while m:
      answ=dgt[m%b]+answ
      m//=b
    print(answ,'_',b,'=?x_10',sep='')
    answ=str(a)
  elif variant==3:
    b=randint(3,9)
    m=a=ma(sc,diff)
    answ=''
    while m:
      answ=dgt[m%b]+answ
      m//=b
    print(a,'_10=?x_',b,sep='')
  if variant==4:
    b=randint(11,16)
    m=a=ma(sc,diff)
    answ=''
    while m:
      answ=dgt[m%b]+answ
      m//=b
    print(answ,'_',b,'=?x_10',sep='')
    answ=str(a)
  elif variant==5:
    b=randint(11,16)
    m=a=ma(sc,diff)
    answ=''
    while m:
      answ=dgt[m%b]+answ
      m//=b
    print(a,'_10=?x_',b,sep='')
  elif variant==6:
    shuffle(base)
    b,b2=base[:2]
    m=a=randint(1000+int(200*srez[6]),1200+int(300*srez[6]))
    answ=''
    while m:
      answ=dgt[m%b]+answ
      m//=b
    print(answ,'_',b,'=?x_',b2,sep='')
    m=a
    answ=''
    while m:
      answ=dgt[m%b2]+answ
      m//=b2
  answer=input().lower().strip()
  answer=answer.replace('а', 'a')
  answer=answer.replace('в', 'b')
  answer=answer.replace('с', 'c')
  answer=answer.replace('е', 'e')
  ##validation
  test+=1
  if answer==answ:
    rightnum+=1
    print('Правильно. ')
    wronganswer=False
    answers+=str(test)+'|'
    srez[variant]+=1
  else:
    answer=input('Неправильно, попробуйте ещё раз: \n').lower().strip()
    answer=answer.replace('а', 'a')
    answer=answer.replace('в', 'b')
    answer=answer.replace('с', 'c')
    answer=answer.replace('е', 'e')
    for i in range(numvartest):
      srez[i]=srez[i]*(0.92-(len(bin(diff))-2)*0.01)
    if answer==answ:
      rightnum+=1
      typo+=1
      print('Правильно. ')
      wronganswer=False
      answers+=':%i:|'%test
      srez[variant]+=1
    else:
      print('Неправильно. Правильный ответ: ',answ)
      wronganswer=True
      answers+='*|'
      for i in range(numvartest):
        srez[i]=srez[i]*(0.92-(len(bin(diff))-2)*0.01)
  #print(rightnum)
  pright(rightnum,typo,test)
  print(answers)
  #sc=diff*min(srez)+(sum(srez)-min(srez))/diff
  sc=scoresult(srez,diff)
  print('балл = %g (сложность %i[%s])'%(sc,diff,diffstr))
  #print(srez[:diff])#del
  thinkmore=True
