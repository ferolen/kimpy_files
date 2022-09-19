# -*- coding: utf-8 -*-
#uses files
#19_test.py
#files/19_1.txt
#files/19_2.txt
#files/19_2p.txt
#files/19_2r.txt
#files/19_3.txt
#files/19_3s.txt

charcoding='utf'#win | utf

from random import randint,shuffle,choice,expovariate
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
rantime(6)

abc='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
numvar=3
diffval=[1,1,1]#len must be numvar

mdtest=hashlib.md5(open('19_test.py','rb').read()).hexdigest()
mdtest+=hashlib.md5(open('files/19_1.txt','rb').read()).hexdigest()
mdtest+=hashlib.md5(open('files/19_2.txt','rb').read()).hexdigest()
mdtest+=hashlib.md5(open('files/19_2p.txt','rb').read()).hexdigest()
mdtest+=hashlib.md5(open('files/19_2r.txt','rb').read()).hexdigest()
mdtest+=hashlib.md5(open('files/19_3.txt','rb').read()).hexdigest()
mdtest+=hashlib.md5(open('files/19_3s.txt','rb').read()).hexdigest()

md=hashlib.md5(mdtest.encode('utf-8')).hexdigest()
fmd=open('files/md5.txt')
line=fmd.readline().split()
while line[0]!='19':
  line=fmd.readline().split()
if md!=line[1]:
  print('Аварийное завершение программы. Код ошибки 1001. Несанкционированное изменение программы')
  sys.exit(1001)
fmd.close()

if not 'task' in os.listdir('../'):
  os.mkdir("../task")

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

##ftr=open('files/troiki.txt','r')
##fop=open('files/operations_3_4.txt','r')
##tro=list(map(lambda s:s[:-1],ftr))
##opr=list(map(lambda s:s[:-1],fop))
##ftr.close()
##fop.close()

def funct(var,par,table,param=[]):
#  print(par)
#  print(table)
  if var==1:
    if par==0:
      return(sum(table[0]))
    if par==1:
      return(sum(table[1]))
    elif par==2:
      return(sum(table[2]))
    elif par==3:
      return(sum(table[0])/len(table[0]))
    elif par==4:
      return(sum(table[1])/len(table[0]))
    elif par==5:
      return(sum(table[2])/len(table[0]))
    elif par==6:
      return(min(table[0]))
    elif par==7:
      return(min(table[1]))
    elif par==8:
      return(min(table[2]))
    elif par==9:
      return(max(table[0]))
    elif par==10:
      return(max(table[1]))
    elif par==11:
      return(max(table[2]))
    elif par==12:
      return(sum(table[0]+table[1]))
    elif par==13:
      return(sum(table[1]+table[2]))
    elif par==14:
      return(sum(table[0]+table[1]+table[2]))
    elif par==15:
      return(sum(table[0]+table[1])/len(table[0])/2)
    elif par==16:
      return(sum(table[1]+table[2])/len(table[0])/2)
    elif par==17:
      return(sum(table[0]+table[1]+table[2])/len(table[0])/3)
    elif par==18:
      return(max(table[0]+table[1]))
    elif par==19:
      return(max(table[1]+table[2]))
    elif par==20:
      return(max(table[0]+table[1]+table[2]))
    elif par==21:
      return(min(table[0]+table[1]))
    elif par==22:
      return(min(table[1]+table[2]))
    elif par==23:
      return(min(table[0]+table[1]+table[2]))
  if var==2:
    if par==0:
      num=0
      for st in table:
        num+=(st[0]==param[0][0])and(st[2]==param[1][0])
      return(num)
    if par==1:
      num=0
      b=0
      for st in table:
        if st[0]==param[0][0]:
          num+=1
          b+=st[3]
      return(b/num)
    if par==2:
      num=0
      b=0
      for st in table:
        if st[2]==param[1][0]:
          num+=1
          b+=st[3]
      return(b/num)
  if var==3:
    if par==0:
      num=0
      for vx in table:
        if param[1]:
          a,b=vx[2:4]
        else:
          b,a=vx[2:4]
        if param[0]==vx[1]:
          if param[4]==0:
            num+=a>b
          if param[4]==1:
            num+=a<b
          if param[4]==2:
            num+=a<=b
          if param[4]==3:
            num+=a>=b
      return(num)
    if par==1:
      mball=sum([v[3-param[1]] for v in table])/len(table)
      num=0
      #print(mball,param[4],table[0])
      for vx in table:
        if param[0]==vx[1]:
          if param[4]==0:
            num+=vx[3-param[1]]>mball
          if param[4]==1:
            num+=vx[3-param[1]]<mball
          if param[4]==2:
            num+=vx[3-param[1]]<=mball
          if param[4]==3:
            num+=vx[3-param[1]]>=mball
      return(num)
    if par==2:
      num=max([v[4]*(param[0]==v[1]) for v in table])
      return(num)
    if par==3:
      num=min([v[4]*(param[0]==v[1])+100*(param[0]!=v[1]) for v in table])
      return(num)
    if par==4:
      num=0
      for vx in table:
        if param[4]==0:
          a=(vx[3-param[1]]>param[2])
        elif param[4]==1:
          a=(vx[3-param[1]]<param[2])
        elif param[4]==2:
          a=(vx[3-param[1]]<=param[2])
        elif param[4]==3:
          a=(vx[3-param[1]]>=param[2])
        if param[5]==0:
          b=(vx[2+param[1]]>param[3])
        elif param[5]==1:
          b=(vx[2+param[1]]<param[3])
        elif param[5]==2:
          b=(vx[2+param[1]]<=param[3])
        elif param[5]==3:
          b=(vx[2+param[1]]>=param[3])
        if a*b:
          num+=1
      return(num)
    if par==5:
      num=0
      for vx in table:
        if param[4]==0:
          num+=(vx[2]>param[2])*(vx[3]>param[2])
        elif param[4]==1:
          num+=(vx[2]<param[2])*(vx[3]<param[2])
        elif param[4]==2:
          num+=(vx[2]<=param[2])*(vx[3]<=param[2])
        elif param[4]==3:
          num+=(vx[2]>=param[2])*(vx[3]>=param[2])
      return(num)
    if par==6:
      num=0
      for vx in table:
        if param[4]==0:
          num+=(vx[2]>param[2])|(vx[3]>param[2])
        elif param[4]==1:
          num+=(vx[2]<param[2])|(vx[3]<param[2])
        elif param[4]==2:
          num+=(vx[2]<=param[2])|(vx[3]<=param[2])
        elif param[4]==3:
          num+=(vx[2]>=param[2])|(vx[3]>=param[2])
      return(num)
    if par==7:
      num=0
      ball=0
      for vx in table:
        if param[4]==0:
          if vx[3-param[1]]>param[2]:
            num+=1
            ball+=vx[2]+vx[3]
        elif param[4]==1:
          if vx[3-param[1]]<param[2]:
            num+=1
            ball+=vx[2]+vx[3]
        elif param[4]==2:
          if vx[3-param[1]]<=param[2]:
            num+=1
            ball+=vx[2]+vx[3]
        elif param[4]==3:
          if vx[3-param[1]]>=param[2]:
            num+=1
            ball+=vx[2]+vx[3]
      return(ball/num)
    if par==8:
      num=0
      for vx in table:
        if param[4]==0:
          if vx[3-param[1]]>param[2]:
            num+=1
        elif param[4]==1:
          if vx[3-param[1]]<param[2]:
            num+=1
        elif param[4]==2:
          if vx[3-param[1]]<=param[2]:
            num+=1
        elif param[4]==3:
          if vx[3-param[1]]>=param[2]:
            num+=1
      return(100*num/len(table))
    if par==9:
      num=0
      allsc=0
      for vx in table:
        if param[0]==vx[1]:
          allsc+=1
          if param[4]==0:
            if vx[3-param[1]]>param[2]:
              num+=1
          elif param[4]==1:
            if vx[3-param[1]]<param[2]:
              num+=1
          elif param[4]==2:
            if vx[3-param[1]]<=param[2]:
              num+=1
          elif param[4]==3:
            if vx[3-param[1]]>=param[2]:
              num+=1
      return(100*num/allsc)
    if par==10:
      num=0
      for vx in table:
        if param[0]==vx[1]:
          if param[6]<=vx[3-param[1]]<=param[7]:
            num+=1
      return(num)
    if par==11:
      num=0
      allsc=0
      for vx in table:
        if param[0]==vx[1]:
          allsc+=1
          if param[6]<=vx[3-param[1]]<=param[7]:
            num+=1
      return(100*num/allsc)

def gen_prob(var,sc,diff):#problem generation
  with open('../task/task%i.csv'%test,'w') as csv:
    if var==1:
      numrow=randint(500,1200)
      amean=randint(5,1000)
      bmean=randint(5,1000)
      cmean=randint(5,1000)
      table=[[] for i in range(3)]
      for i in range(numrow):
        a=expovariate(1/amean)
        acsv=str(a).replace('.',',')
        b=expovariate(1/amean)
        bcsv=str(b).replace('.',',')
        c=expovariate(1/amean)
        ccsv=str(c).replace('.',',')
        table[0].append(a)
        table[1].append(b)
        table[2].append(c)
        csv.write('%s\t%s\t%s\n'%(acsv,bcsv,ccsv))
      csv.close()
      with open('files/19_1.txt') as f:
        if charcoding=='win':
          vof=list(map(lambda s:s[:-1].encode('cp1251', 'ignore').decode('utf-8', 'ignore'),f))
        else:
          vof=list(map(lambda s:s[:-1],f))
      f.close()
      #print(table)
      ch=randint(0,len(vof)-1)
      print('В папке task в файле \'task%i.csv\' на Рабочем Столе записаны числа в столбцах А, В и С. Найдите %s с точностью не менее двух знаков после запятой. '%(test,vof[ch]))
      answer=funct(1,ch,table)#
      return(answer)
    elif var==2:
      numrow=randint(500,1200)
      if numrow%10==1:
        numrow+=1
      with open('files/19_2r.txt') as f:
        if charcoding=='win':
          region=list(map(lambda s:s[:-1].encode('cp1251', 'ignore').decode('utf-8', 'ignore').split(':'),f))
        else:
          region=list(map(lambda s:s[:-1].split(':'),f))
      #print(region)
      with open('files/19_2p.txt') as f:
        if charcoding=='win':
          pred=list(map(lambda s:s[:-1].encode('cp1251', 'ignore').decode('utf-8', 'ignore').split(':'),f))
        else:
          pred=list(map(lambda s:s[:-1].split(':'),f))
      #print(pred)
      csv.write('район\tфамилия\tпредмет\tбалл\n')
      table=[]
      rg=[]
      prd=[]
      for s in region:
        rg+=[s]*randint(3,10)
      for s in pred:
        prd+=[s]*randint(3,10)
      for i in range(numrow):
        row=[choice(rg)[0],'Ученик '+str(i+1),choice(prd)[0],randint(50,200)+randint(50,799)]
        table.append(row)
        row=list(map(str,row))
        csv.write('\t'.join(row)+'\n')
      with open('files/19_2.txt') as f:
        if charcoding=='win':
          vof=list(map(lambda s:s[:-1].encode('cp1251', 'ignore').decode('utf-8', 'ignore'),f))
        else:
          vof=list(map(lambda s:s[:-1],f))
      ch=randint(0,len(vof)-1)
      param=[choice(region),choice(pred)]
      #print(param)
      paramstr=[vof[0]%(param[0][2],param[0][0],param[1][1]),
                vof[1]%(param[0][3],param[0][0]),
                vof[2]%param[1][1]][ch]
      print('В папке task в файле \'task%i.csv\' на Рабочем Столе записаны данные о тестировании учеников. В столбце А записан округ, в котором учится ученик; в столбце В — фамилия; в столбце С — любимый предмет; в столбце D — тестовый балл. Всего в электронную таблицу были занесены данные по %i ученикам. Откройте файл с данной электронной таблицей. На основании данных, содержащихся в этой таблице, ответьте, %s'%(test,numrow,paramstr))
      #print(vof)
      answer=funct(2,ch,table,param)#
      return(answer)
    elif var==3:
      numrow=randint(500,1200)
      with open('files/19_2p.txt') as f:
        if charcoding=='win':
          pred=list(map(lambda s:s[:-1].encode('cp1251', 'ignore').decode('utf-8', 'ignore').split(':'),f))
        else:
          pred=list(map(lambda s:s[:-1].split(':'),f))
      with open('files/19_3s.txt') as f:#schools
        if charcoding=='win':
          scools=list(map(lambda s:s[:-1].encode('cp1251', 'ignore').decode('utf-8', 'ignore').split(':'),f))
        else:
          scools=list(map(lambda s:s[:-1].split(':'),f))
      #print(pred)
      shuffle(pred)
      #first,second=pred[:2]
      #print(first,second)
      csv.write('фамилия\tшкола\t%s\t%s\n'%(pred[0][0],pred[1][0]))
      table=[]
      sc=[]
      for s in scools:
        sc+=[s]*randint(3,10)
      for i in range(numrow):
        row=['Ученик '+str(i+1),choice(sc)[0],randint(0,20)+randint(0,79),randint(0,20)+randint(0,79)]
        rowrite=list(map(str,row))
        csv.write('\t'.join(rowrite)+'\n')
        row.append(row[3]+row[2])
        table.append(row)
      with open('files/19_3.txt') as f:
        if charcoding=='win':
          vof=list(map(lambda s:s[:-1].encode('cp1251', 'ignore').decode('utf-8', 'ignore'),f))
        else:
          vof=list(map(lambda s:s[:-1],f))
      ch=randint(0,len(vof)-1)
      sign=[]
      sign.append(['выше','ниже','не выше','не ниже'])
      sign.append(['больше','меньше','не больше','не меньше'])
      sign.append(['более','менее','не более','не менее'])
      sign.append(['больше чем','меньше чем','не больше чем','не меньше чем'])
      scrfrom,scrto=randint(10,90),randint(10,90)
      scrfrom,scrto=min(scrfrom-1,scrto),max(scrfrom,scrto+1)
      param=[choice(sc)[0],randint(0,1),randint(25,75),randint(30,70),randint(0,3),randint(0,3),scrfrom,scrto]
      #param 0-school, 1 rev(0) or no(1), 2 first ball, 3 second ball,
      #4 sign, 5 sign, 6 scrfrom, 7 scrto
      if param[1]:
        ordpred=[0,1]
      else:
        ordpred=[1,0]
      #print(param)
      #print(vof[ch])
      sigch=randint(0,len(sign)-1)
      paramstr=[vof[0]%(param[0],pred[ordpred[0]][2],sign[0][param[4]],pred[ordpred[1]][2]),
                vof[1]%(param[0],pred[ordpred[0]][2],sign[0][param[4]]),
                vof[2]%param[0],
                vof[3]%param[0],
                vof[4]%(pred[ordpred[0]][2],sign[sigch][param[4]],param[2],pred[ordpred[1]][2],sign[sigch][param[5]],param[3]),
                vof[5]%(sign[max(sigch-1,0)][param[4]],param[2]),
                vof[6]%(sign[max(sigch-1,0)][param[4]],param[2]),
                vof[7]%(pred[ordpred[0]][2],sign[max(sigch-1,0)][param[4]],param[2]),
                vof[8]%(pred[ordpred[0]][2],sign[max(sigch-1,0)][param[4]],param[2]),
                vof[9]%(param[0],pred[ordpred[0]][2],sign[max(sigch-1,0)][param[4]],param[2]),
                vof[10]%(param[0],pred[ordpred[0]][2],param[6],param[7]),
                vof[11]%(param[0],pred[ordpred[0]][2],param[6],param[7])][ch]
      print('В папке task в файле \'task%i.csv\' на Рабочем Столе записаны данные о тестировании учеников. В столбце А записана фамлиия ученика; в столбце В — школа; в столбце С — балл по %s; в столбце D — балл по %s;. Всего в электронную таблицу были занесены данные по %i ученикам. Откройте файл с данной электронной таблицей. На основании данных, содержащихся в этой таблице, ответьте, %s'%(test,pred[0][2],pred[1][2],numrow,paramstr))
      #print('2')
      answer=funct(3,ch,table,param)
      return(answer)
    elif var==4:
      csv.write('1\t2\t3\4')
      print('При регистрации в компьютерной системе каждому пользователю выдаётся пароль, состоящий из %i символов и содержащий только символы %s (таким образом, используется %i различных символов). Каждый такой пароль в компьютерной программе записывается минимально возможным и одинаковым целым количеством байт (при этом используют посимвольное кодирование и все символы кодируются одинаковым и минимально возможным количеством бит). Определите объём памяти, отводимый этой программой для записи %i паролей.'%(pswd,symbset,numsymb,numpwd*5))
      answer=4
      return(answer)
    
sc=0.0#scores
diff=0#difficulty
print('Убедитесь, что на рабочем столе есть папка task. Убедитесь, что все лишние электронные таблицы закрыты.')
while diff<1 or diff>2**numvar-1:
  try:
    diff=int(input('Введите код работы (от 1 до %i)'%(2**numvar-1)))
  except ValueError:
    continue
vardiff=list({i*int(bin(16+diff)[7-i]) for i in range(1,5)}-{0})
#diff=sum([diffval[i-1] for i in vardiff])

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
  ##validation
  acc=True
  while acc:
    try:
      answer=float(input('Ваш ответ:').strip().replace(',','.'))
      acc=False
    except ValueError:
      print('Неверный формат ввода.')
      continue
  #print(answer)
  test+=1
  diff=1+sc/2
  if abs(answer-right)<=0.01:
    rightnum+=1
    print('Правильно. ')
    wronganswer=False#timeroption
    answers+=str(test)+'|'
    sc+=1
  else:
    acc=True
    while acc:
      try:
        answer=float(input('Неправильно. Попробуйте ещё раз:').strip().replace(',','.'))
        acc=False
      except ValueError:
        print('Неверный формат ввода.')
        continue
    sc=sc*(0.96-0.01*diff)
    if abs(answer-right)<=0.01:
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
  print('-'*30)
  print('балл = %g (сложность %i)'%(sc,diff))
  print('-'*30)
