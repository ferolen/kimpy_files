#uses files
#17_a_test.py
#files/17_a_files.txt

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

mdtest=hashlib.md5(open('17_a_test.py','rb').read()).hexdigest()
mdtest+=hashlib.md5(open('files/17_a_files.txt','rb').read()).hexdigest()
md=hashlib.md5(mdtest.encode('utf-8')).hexdigest()

fmd=open('files/md5.txt')
line=fmd.readline().split()
while line[0]!='17a':
  line=fmd.readline().split()
if md!=line[1]:
  print('Аварийное завершение программы. Код ошибки 1001. Несанкционированное изменение программы')
  sys.exit(1001)
fmd.close()


def genword():
  gl='qwrtpsdfghklzxcvbnm'
  sg='aeyuio'
  s=''
  for i in range(randint(3,8)):
    if i>1:
      if s[i-1] in gl and s[i-2] in gl:
        nx=1
      elif s[i-1] in sg and s[i-2] in sg:
        nx=0
      elif s[i-1] in sg:
        nx=int(randint(0,5)/5)
      else:
        nx=randint(0,1)
    else:
      nx=randint(0,1)
    if nx:
      s+=choice(sg)
    else:
      s+=choice(gl)
  return(s)

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

lfs=list(map(lambda s:s[:-1],open('files/17_a_files.txt','r')))
vrs='abcdefg'
l=[0,1,2,3,4,5,6]
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
test=1#test number
rightnum=0#right answers number
typo=0#misprints number
answers='|'#table of marks
while True:
  if randint(0,2):
    st=choice(lfs).split()
  else:
    st=[genword(),genword()]
  shuffle(l)
  domen=['com','org','name','info','biz','net','ru','kz','by','kg']
  ext=['txt','doc','rtf','docx','pdf','htm','html','csv','py','png','jpg']
  protocol=['http','https','ftp','file']
  exdom=[randint(0,len(ext)-1),randint(0,len(domen)-1)]
  flname=st[0]
  srv=st[1]
  pr=choice(protocol)
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
  print('#%i'%test)
  print('Доступ к файлу %s.%s, \nнаходящемуся на сервере %s.%s, \nосуществляется по протоколу %s. \nФрагменты адреса файла закодированы буквами от a до g. Запишите последовательность этих букв, кодирующую адрес указанного файла в сети Интернет.'%(flname,ext[exdom[0]],srv,domen[exdom[1]],pr))
  adr=[pr,'://',srv,'.'+domen[exdom[1]],'/',flname,'.'+ext[exdom[0]]]
  adright=['']*7
  for i in range(7):
    print('%s) %s'%(vrs[i],adr[l[i]]))
    adright[l[i]]=vrs[i]
  right=''.join(adright)
  print('Ответ:',end='')
  ##validation  
  answer=input().strip().upper()
  #print(answer)
  if answer==right.upper():
    rightnum+=1
    print('Правильно. ')
    wronganswer=False#timeroption
    answers+=str(test)+'|'
    sc+=1
  else:
    answer=input('Неправильно. Попробуйте ещё раз:').strip().upper()
    sc=sc*(0.98-0.01*diff)
    if answer==right.upper():
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
      sc=max(sc*(0.98-0.01*diff),0)
  #print(rightnum)
  pright(rightnum,typo,test)
  print(answers)
  print('балл = %g  (сложность %i)'%(sc,diff))
