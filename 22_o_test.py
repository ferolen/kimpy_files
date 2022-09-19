#uses files
#22_o_test.py

from random import randint,shuffle,choice,random
#import random
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

mdtest=hashlib.md5(open('22_o_test.py','rb').read()).hexdigest()
#mdtest+=hashlib.md5(open('conf.txt','rb').read()).hexdigest()

md=hashlib.md5(mdtest.encode('utf-8')).hexdigest()
fmd=open('files/md5.txt')
line=fmd.readline().split()
while line[0]!='22o':
  line=fmd.readline().split()
if md!=line[1]:
  print('Аварийное завершение программы. Код ошибки 1001. Несанкционированное изменение программы')
  sys.exit(1001)
fmd.close()

op='∧∨→≡⊕'#logic operators
n=5#numbers of operators
numtest=20
a='abc'#logic variables

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

def br(n): #generation all mask with braces // a+(a+a)
  if n == 1:
    return({'a'})
  else:
    brs={'a+'*(n-1)+'a'}
    for i in range(1,n):
      br1=br(i)
      br2=br(n-i)
      for s1 in br1:
        for s2 in br2:
          brs.add(s1+'+'+s2)
          if i>1:
            brs.add('('+s1+')+'+s2)
          if 1<i<n-1:
            brs.add('('+s1+')+('+s2+')')
          if i<n-1:
            brs.add(s1+'+('+s2+')')
    return(brs)

def rs(s):#formulas validator
  r=w=0
  for i in op:
    for j in a:
      w+=s.find(j+i+j)
      w+=s.find(j+i+'¬'+j)
      r-=2
  return(r==w)

def inf2pos(k):#k=list(input()+'#')#valiable infix
    k+='#'
    po=''#postfix
    sign=set('(¬)#'+op)
    def rank(s):#rank of operator s
        if s=='%':
            return(100)
        if s=='(':
            return(0)
        elif s=='→':
            return(5)
        elif s=='¬':
            return(1)
        elif s=='∨':
            return(3)
        elif s=='⊕':
            return(4)
        elif s=='∧':
            return(2)
        elif s=='≡':
            return(6)
        elif s=='#':
            return(100)
        else:
            return(-1)

    stk=['%']
    for s in k:
        #print('::',po,s)
        if s in sign:
            if s==')':
                while stk[0]!='(':
                    po+=stk.pop(0)
                stk.pop(0)
                continue
            #po+=str(rank(s))
            #print('#',s)
            while stk:
                #print('!',s)
                if rank(stk[0])<=rank(s):
                    if stk[0]=='(':
                        stk.insert(0,s)
                        break
                    else:
                        po+=stk.pop(0)
                else:
                    stk.insert(0,s)
                    break
        else:
            po+=s
    return(po[:-1])

'''def genbin(s,l):
    if l:
        s[l-1]=0
        genbin(s,l-1)
        s[l-1]=1
        genbin(s,l-1)
    else:
        print(s)'''
        
def pos2inf_calc(k):#calculate postfix fomula k
    outpic=['' for i in range(-1,8)]
    outpic[0]='000'
    outpic[1]='001'
    outpic[2]='010'
    outpic[3]='011'
    outpic[4]='100'
    outpic[5]='101'
    outpic[6]='110'
    outpic[7]='111'
    stk=[[] for i in range(8)]
    sign=set(op+'¬')
    var=set()
    varlist='abc'
    for s in k:
        if s in sign:
            outpic[-1]+=' '+s
            for j in range(8):
                if s=='¬':
                    if stk[j][0]=='0':
                        stk[j][0]='1'
                    else:
                        stk[j][0]='0'
                else:
                    a=stk[j].pop(0)
                if s=='→':
                    if a=='0' and stk[j][0]=='1':
                        stk[j][0]='0'
                    else:
                        stk[j][0]='1'
                if s=='∨':
                    if stk[j][0]+a=='00':
                        stk[j][0]='0'
                    else:
                        stk[j][0]='1'
                if s=='∧':
                    if stk[j][0]+a=='11':
                        stk[j][0]='1'
                    else:
                        stk[j][0]='0'
                if s=='≡':
                    stk[j][0]=str((int(stk[j][0])+int(a)+1)%2)
                if s=='⊕':
                    stk[j][0]=str((int(stk[j][0])+int(a))%2)
                outpic[j]+=' '+stk[j][0]
        else:
            if not s in var:
                var.add(s)
                varlist+=s
            num=0
            while varlist[num]!=s:
                num+=1
            for j in range(8):
                stk[j].insert(0,outpic[j][num])
    #print(varlist,end='')
    answ=1
    pw=['']*8
    for i in range(8):
      qw=outpic[i].split()
      print(qw[0],end=' ')
      if (input()==qw[len(qw)-1]):
        pw[i]='+'
      else:
        pw[i]='-'
        answ/=2
      #print(outpic[i])
        
    for i in range(8):
      print(outpic[i]+' ('+pw[i]+')')
      
    return(answ)

def randflist(l):#probabilty with density l
  n=random()*sum(l)
  i=0
  while True:
    if n-l[i]<=0:
      break
    n-=l[i]
    i+=1
  return(i)

def operation_num(diff,sc):
  numop=2+diff//3
  if diff==0:
    l=[2+sc,2+sc,1+sc/2]
  elif diff==1:
    l=[2+2*sc/3,3+sc,1+sc/2,sc/4]
  elif diff in [2,3]:
    l=[1+sc/2,4+sc,1.5+2*sc/3,sc/3]
  else:
    l=[1+sc*diff/18,1+sc*diff/12,1.5+sc*diff/6,sc*diff/12]
  numop+=randflist(l)
  return numop

def fgen(diff,sc):#formula generator
  while True:
    numop=operation_num(diff,sc)
    numnot=0#number of ¬
    for i in range(numop):
      numnot+=(random()<1/(5*i+1))
    numnot%=3
    if numnot==0:
      numnot=randflist([1,4])
    #print(numnot)
    ops=''.join(choice(list(op[:1+diff])) for i in range(numop))
    #print(ops)
    nt=False
    if numop>2:
      while not nt:
        vrs=''.join(choice(list(a)) for i in range(numop))
        nt=(vrs.find('a')+1)*(vrs.find('b')+1)*(vrs.find('c')+1)
    else:
      vrs='ab'
    #print(vrs)

    msk=choice(list(br(numop)))
    nmb=msk.count('a')+msk.count('(')
    nn=set()
    while len(nn)<numnot:
      nn.add(randint(0,nmb-1))
    nmb=0
    s=''
    for i in msk:
      if i=='a':
        if nmb in nn:
          s+='¬'
        nmb+=1
        s+=vrs[0]
        vrs=vrs[1:]
      elif i=='+':
        s+=ops[0]
        ops=ops[1:]
      elif i=='(':
        if nmb in nn:
          s+='¬'
        nmb+=1
        s+=i
      else:
        s+=i
    if rs(s):
      break
  return(s)
    #print(s)
  #print(s,rs(s))    
#end formula generator

sc=0.0#scores
diff=0#difficulty
while diff<1 or diff>9:#1 ¬∧∨ 2→ 3≡ 4+⊕ 
  try:
    diff=int(input('Выберите сложность от 1 до 9 (1 самый лёгкий)'))
  except ValueError:
    continue

minimtimefortask=150
deltatime=randint(0,99)/100
tmrnd=0
wronganswer=thinkmore=True#timelogger

test=0#test number
rightnum=0#right answers number
typo=0#misprints number
answers='|'#table of marks
w=r=0
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
  s=fgen(diff,sc)
  print(s,'\nabc')
  #print(inf2pos(s))
  now=pos2inf_calc(inf2pos(s))
  if now==1:
    wronganswer=False#timeroption
    sc+=1
    answers+=str(r+1)+"|"
  elif now==0.5:
    wronganswer=False#timeroption
    sc=sc*(0.98-0.001*diff/2)+0.5
    answers+=":%i:|"%(r+1)
  else:
    sc*=0.93-0.001*diff+now
    answers+="*|"
  r+=1
  print (answers)
  print ('-'*50,'\n',sc,' баллов из ',r,'\n','-'*50,sep='')
  
##  
##notend=True
##l=[0]*n
##l[0]=2
##l[1]=1
##while notend:
##  l=l
