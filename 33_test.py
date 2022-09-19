#uses files
#33_test.py

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

mdtest=hashlib.md5(open('33_test.py','rb').read()).hexdigest()
numvar=4

md=hashlib.md5(mdtest.encode('utf-8')).hexdigest()
fmd=open('files/md5.txt')
line=fmd.readline().split()
while line[0]!='33':
  line=fmd.readline().split()
if md!=line[1]:
  print('Аварийное завершение программы. Код ошибки 1001. Несанкционированное изменение программы')
  sys.exit(1001)
fmd.close()

abc='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'

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

##ftr=open('files/troiki.txt','r')
##fop=open('files/operations_3_4.txt','r')
##tro=list(map(lambda s:s[:-1],ftr))
##opr=list(map(lambda s:s[:-1],fop))
##ftr.close()
##fop.close()
def gen_prob(var,sc,diff):
  if var==1:
    pswd=randint(6,30)
    symbrand=list(abc)
    shuffle(symbrand)
    numsymb=randint(5,17)
    symbset=', '.join(symbrand[:numsymb])
    numpwd=randint(3,12)
    answer=(((len(bin(numsymb-1))-2)*pswd-1)//8+1)*numpwd*5
    print('При регистрации в компьютерной системе каждому пользователю выдаётся пароль, состоящий из %i символов и содержащий только символы %s (таким образом, используется %i различных символов). Каждый такой пароль в компьютерной программе записывается минимально возможным и одинаковым целым количеством байт (при этом используют посимвольное кодирование и все символы кодируются одинаковым и минимально возможным количеством бит). Определите объём памяти, отводимый этой программой для записи %i паролей.'%(pswd,symbset,numsymb,numpwd*5))
    return(answer)
  if var==2:
    numl=randint(4,12)
    numsymb=randint(15,33)
    numnum=randint(3,12)*5
    answer=(((len(bin(numsymb+9))-2)*numl-1)//8+1)*numnum
    print('B некоторой стране автомобильный номер длиной %i символов составляют из заглавных букв (задействовано %i различных букв) и десятичных цифр в любом порядке. Каждый такой номер в компьютерной программе записывается минимально возможным и одинаковым целым количеством байтов (при этом используют посимвольное кодирование и вcе СИМВОЛЫ кодируются одинаковым и минимально возможным количеством битов). Определите объём памяти, отводимый этой программой для записи %i номеров. (Ответ дайте в байтах.)'%(numl,numsymb,numnum))
    return(answer)
  if var==3:
    numsp=randint(30,120)
    qminbit=len(bin(numsp-1))-2
    bitor=randint(0,1)
    numm=randint(numsp//2,numsp-1)
    if bitor:
      while qminbit*numm%8:
        numm=randint(numsp//2,numsp-1)
      answer=qminbit*numm//8
      edm='байтах'
    else:
      answer=qminbit*numm
      edm='битах'
    print('В велокроссе участвуют %i спортсменов. Специальное устройство регистрирует прохождение каждым из участников промежуточного финиша, записывая его номер с использованием минимально возможного количества бит, одинакового для каждого спортсмена. Какой объём памяти будет использован устройством, когда промежуточный финиш прошли %i велосипедистов? (Ответ дайте в %s.)'%(numsp,numm,edm))
    return(answer)
  if var==4:
    lenpswd=randint(6,30)
    symbrand=list(abc)
    shuffle(symbrand)
    numsymb=randint(5,50)
    symbset=', '.join(symbrand[:numsymb])
    dop=randint(3,20)
    numuser=randint(3,12)*5
    allmem=(((len(bin(numsymb-1))-2)*lenpswd-1)//8+1+dop)*numuser
    var4=randint(1,2)
    if var4==1:
      print('При регистрации в компьютерной системе каждому пользователю выдаётся пароль, состоящий из %i символов и содержащий только символы из %i буквенного набора %s. В базе данных для хранения сведений о каждом пользователе отведено одинаковое и минимально возможное целое число байт. При этом используют посимвольное кодирование паролей, все символы кодируются одинаковым и минимально возможным количеством бит. Кроме пароля для каждого пользователя в системе хранятся дополнительные сведения, для чего отведено %i байт.Определите объём памяти, необходимый для хранения сведений о %i пользователях. (Ответ дайте в байтах.)'%(lenpswd,numsymb,symbset,dop,numuser))
      answer=allmem
    #print('При регистрации в компьютерной системе каждому пользователю выдаётся пароль, состоящий из %i символов и содержащий только символы %s (таким образом, используется %i различных символов). Каждый такой пароль в компьютерной программе записывается минимально возможным и одинаковым целым количеством байт (при этом используют посимвольное кодирование и все символы кодируются одинаковым и минимально возможным количеством бит). Определите объём памяти, отводимый этой программой для записи %i паролей.'%(pswd,symbset,numsymb,numpwd*5))
    if var4==2:
      print('При регистрации в компьютерной системе каждому пользователю выдаётся пароль, состоящий из %i символов и содержащий только символы из %i-символьного набора: %s. В базе данных для хранения сведений о каждом пользователе отведено одинаковое и минимально возможное целое число байт. При этом используют посимвольное кодирование паролей, все символы кодируют одинаковым и минимально возможным количеством бит. Кроме собственно пароля, для каждого пользователя в системе хранятся дополнительные сведения, для чего выделено целое число байт; это число одно и то же для всех пользователей. Для хранения сведений о %i пользователях потребовалось %i байт. Сколько байт выделено для хранения дополнительных сведений об одном пользователе? В ответе запишите только целое число – количество байт.'%(lenpswd,numsymb,symbset,numuser,allmem))
      answer=dop
    #print('При регистрации в компьютерной системе каждому пользователю выдаётся пароль, состоящий из %i символов и содержащий только символы %s (таким образом, используется %i различных символов). Каждый такой пароль в компьютерной программе записывается минимально возможным и одинаковым целым количеством байт (при этом используют посимвольное кодирование и все символы кодируются одинаковым и минимально возможным количеством бит). Определите объём памяти, отводимый этой программой для записи %i паролей.'%(pswd,symbset,numsymb,numpwd*5))
    return(answer)
    
sc=0.0#scores
diff=0#difficulty
diffval=[1.4,1.6,1,2]
while diff<1 or diff>2**numvar-1:
  try:
    diff=int(input('Введите код работы (от 1 до %i)'%(2**numvar-1)))
  except ValueError:
    continue
vardiff=list({i*int(bin(16+diff)[7-i]) for i in range(1,5)}-{0})
diff=sum([diffval[i-1] for i in vardiff])

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
  print('Ваш ответ:',end='')
  ##validation  
  answer=input().strip()
  #print(answer)
  test+=1
  if answer==str(right):
    rightnum+=1
    print('Правильно. ')
    wronganswer=False#timeroption
    answers+=str(test)+'|'
    sc+=1
  else:
    answer=input('Неправильно. Попробуйте ещё раз:').strip()
    sc=sc*(0.96-0.01*diff)
    if answer==str(right):
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
