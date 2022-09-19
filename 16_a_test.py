#uses files
#16_a_test.py
#files/16_a_odd.txt
#files/16_a_even.txt
#files/16_a_voc.txt

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

mdtest=hashlib.md5(open('16_a_test.py','rb').read()).hexdigest()
mdtest+=hashlib.md5(open('files/16_a_even.txt','rb').read()).hexdigest()
mdtest+=hashlib.md5(open('files/16_a_odd.txt','rb').read()).hexdigest()
mdtest+=hashlib.md5(open('files/16_a_voc.txt','rb').read()).hexdigest()
md=hashlib.md5(mdtest.encode('utf-8')).hexdigest()
fmd=open('files/md5.txt')
line=fmd.readline().split()
while line[0]!='16a':
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

    
abc='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def nx(s):
  abc='абвгдеёжзийклмнопрстуфхцчшщъыьэюяа'
  r=''
  for c in s:
    r+=abc[abc.find(c)+1]
  return(r)

def f(word,a,b):#a-for even b-for odd
  if len(word)%2:
    if a==1:
      rw=word+adeven[0]
    elif a==2:
      rw=adeven[0]+word
    elif a==3:
      rw=word+word[0]
    elif a==4:
      rw=word[-1]+word
    elif a==5:
      rw=word+word[len(word)//2]
    elif a==6:
      rw=word[len(word)//2]+word
    elif a==7:
      q=len(word)//2
      rw=word[:q]+word[q+1:]
    elif a==8:
      rw=word[0]+adeven[0]+word[1:]
    elif a==9:
      rw=word[:-1]+adeven[0]+word[-1]
    else:
      print('there is no parametr',a,'for f(word,b,a)')
      
  else:
    n=len(word)
    if b==1:
      rw=word[:n//2]+adodd[0]+word[n//2:]
    elif b==2:
      rw=word[1:n//2]+adodd[0]+word[n//2:-1]
    elif b==3:
      rw=word+adodd[0]
    elif b==4:
      rw=adodd[0]+word
    elif b==5:
      rw=word[1:]
    elif b==6:
      rw=word[:-1]
    elif b==7:
      rw=word[:n//2]+word[0]+word[n//2:]
    elif b==8:
      rw=word[:n//2]+word[-1]+word[n//2:]
    elif b==9:
      rw=word+word[0]
    elif b==10:
      rw=word[-1]+word
    elif b==11:
      rw=word[0]+word[2:]
    elif b==12:
      rw=word[:-2]+word[-1]
    elif b==13:
      rw=word[0]+adodd[0]+word[1:]
    elif b==14:
      rw=word[:-1]+adodd[0]+word[-1]
    else:
      print('there is no parametr',a,'for f(word,b,a)')
  return(nx(rw))
    
fodd=open('files/16_a_odd.txt','r')
feven=open('files/16_a_even.txt','r')
fvoc=open('files/16_a_voc.txt')
adodd=list(map(lambda s:s[:-1],fodd))
adeven=list(map(lambda s:s[:-1],feven))
voc=list(set(map(lambda s:s[:-1],fvoc)))
fodd.close()
feven.close()
fvoc.close()

evsymb={1,2,8,9}#there is a char in task
odsymb={1,2,3,4,13,14}#there is a char in task
##adodd[0]=choice(abc)
##adeven[0]=choice(abc)
adodd[0]='*'
adeven[0]='*'

#ad - algorithm change description


#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
n=0
sc=0.0#scores
diff=0#difficulty
while diff<1 or diff>5:
  try:
    diff=int(input('Выберите сложность (от 1 до 5)'))
  except ValueError:
    continue
#bg,num=1,100
test=0#test number
rightnum=0#right answers number
typo=0#misprints number
answers='|'#table of marks
minimtimefortask=60
deltatime=randint(0,99)/100
tmrnd=0
wronganswer=thinkmore=True
test=0#test number
rightnum=0#right answers number
typo=0#misprints number
answers='|'#table of marks
while True:
  ev=randint(1,len(adeven)-1)
  if ev in evsymb:
    adeven[0]=choice(abc)
  else:
    adeven[0]=''
  od=randint(1,len(adodd)-1)
  if od in odsymb:
    adodd[0]=choice(abc)
  else:
    adodd[0]=''
  wordex=['','']#example words
  wrd=''
  while not 2<len(wrd)<6:
    wrd=choice(voc)
  while not (len(wordex[0])+len(wordex[1]) in [5,7,9]) or max(len(wordex[0]),len(wordex[1]))>7:
    wordex[0]=choice(voc)
    wordex[1]=choice(voc)
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
  n+=1
  print('#%i\nНекоторый алгоритм из одной цепочки символов получает новую цепочку следующим образом. Сначала вычисляется длина исходной цепочки символов. Если она нечётна, то %s, а если чётна, то %s. В полученной цепочке символов каждая буква заменяется буквой, следующей за ней в русском алфавите (А — на Б, Б — на В и т. д., а Я — на А). Получившаяся таким образом цепочка является результатом работы алгоритма.'%(n,adeven[ev],adodd[od])%(adeven[0].upper(),adodd[0].upper()))
  print('Например, если исходной была цепочка %s, то результатом работы алгоритма будет цепочка %s, а если исходной была цепочка %s, то результатом работы алгоритма будет цепочка %s.'%(wordex[0].upper(),f(wordex[0],ev,od).upper(),wordex[1].upper(),f(wordex[1],ev,od).upper()))
  print('Дана цепочка символов %s. Какая цепочка символов получится, если к данной цепочке применить описанный алгоритм дважды (т. е. применить алгоритм к данной цепочке, а затем к результату вновь применить алгоритм)? \nРусский алфавит: АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ.'%wrd.upper())
  print('Ответ:',end='')
  answer=input().upper().strip()
  #print(answer)
  test+=1
  if answer==f(f(wrd,ev,od),ev,od).upper():
    rightnum+=1
    wronganswer=False
    print('Правильно. ')
    answers+=str(test)+'|'
    sc+=1
  else:
    answer=input('Неправильно. Попробуйте ещё раз:').upper().strip()
    sc=sc*(0.97-0.01*diff)
    if answer==f(f(wrd,ev,od),ev,od).upper():
      rightnum+=1
      wronganswer=False
      typo+=1
      print('Правильно. ')
      answers+=':%i:|'%test
      sc=max(sc+1,0)
    else:
      print('Неправильно. Правильный ответ:',f(f(wrd,ev,od),ev,od).upper())
      answers+='*|'
      sc=max(sc*(0.95-0.02*diff),0)
      wronganswer=True
  #print(rightnum)
  pright(rightnum,typo,test)
  print(answers)
  print('балл = %g  (сложность %i)'%(sc,diff))
