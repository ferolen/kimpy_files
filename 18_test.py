#uses files
#18_test.py
#files/troiki.txt
#files/operations_3_4.txt

from random import randint,shuffle,choice
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

mdtest=hashlib.md5(open('18_test.py','rb').read()).hexdigest()
mdtest+=hashlib.md5(open('files/troiki.txt','rb').read()).hexdigest()
mdtest+=hashlib.md5(open('files/operations_3_4.txt','rb').read()).hexdigest()

md=hashlib.md5(mdtest.encode('utf-8')).hexdigest()
fmd=open('files/md5.txt')
line=fmd.readline().split()
while line[0]!='18':
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

ftr=open('files/troiki.txt','r',encoding='utf-8')
fop=open('files/operations_3_4.txt','r')
tro=list(map(lambda s:s[:-1],ftr))
opr=list(map(lambda s:s[:-1],fop))
ftr.close()
fop.close()

abc='ABCDE'
numchoice=[5,7,9,13,17,19,21]#number of choice
sorting=['убывания','возрастания']
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
wronganswer=thinkmore=True#timelogger

numvar=4#number of variants
test=0#test number
rightnum=0#right answers number
typo=0#misprints number
answers='|'#table of marks

while True:
  sortby=randint(0,1)
  numch=numchoice[min(int(sc),min(3,diff)*2)]
  numvar=4+(int(sc)+diff*2+randint(0,5))//18
  req=[i for i in range(numch)]#choice requests
  tr=choice(tro).split()
  good=0
  while not good:
    shuffle(req)
    good=1
    for i in range(numvar):
      for j in range(numvar):
        good*=int(opr[req[i]].split(':')[1][req[j]])
  answls=[]
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
  print('#%i'%(test+1))
  print('В таблице приведены запросы к поисковому серверу. Для каждого запроса указан его код — соответствующая буква от %s до %s. Расположите коды запросов слева направо в порядке %s количества страниц, которые нашёл поисковый сервер по каждому запросу. По всем запросам было найдено разное количество страниц. Для обозначения логической операции «ИЛИ» в запросе используется символ «|», а для логической операции «И» — «&»:'%(abc[0],abc[numvar-1],sorting[sortby]))
  print(' Код : Запрос')
  for i in range(numvar):
    reqout=opr[req[i]].split(':')[0]
    reqout=reqout.replace('a',tr[0])
    reqout=reqout.replace('b',tr[1])
    reqout=reqout.replace('c',tr[2])
    reqout=reqout.replace('d',tr[3])
    print('  %s  :  %s'%(abc[i],reqout))
    answls.append([int(opr[req[i]].split(':')[2]),abc[i]])
  answls.sort()
  right=''#right answer
  for i in range(numvar):
    right+=answls[i][1]
  right=right[::2*sortby-1]
  print('Ваш ответ (без пробелов):',end='')
  ##validation  
  answer=input().strip().upper()
  #print(answer)
  test+=1
  if answer==right:
    rightnum+=1
    print('Правильно. ')
    wronganswer=False#timeroption
    answers+=str(test)+'|'
    sc+=1
  else:
    answer=input('Неправильно. Попробуйте ещё раз:').strip().upper()
    sc=sc*(0.96-0.01*diff)
    if answer==right:
      rightnum+=1
      typo+=1
      print('Правильно. ')
      wronganswer=False#timeroption
      answers+=':%i:|'%test
      sc+=1
    else:
      print('Неправильно. Правильный ответ:',right)
      wronganswer=True#timeroption
      answers+='*|'
      sc=sc*(0.94-0.02*diff)
  #print(rightnum)
  pright(rightnum,typo,test)
  print(answers)
  print('балл = %g (сложность %i)'%(sc,diff))
