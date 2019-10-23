
# coding: utf-8

# In[ ]:


# 查看当前挂载的数据集目录, 该目录下的变更重启环境后会自动还原
# View dataset directory. This directory will be recovered automatically after resetting environment. 
get_ipython().system('ls /home/aistudio/data')


# In[ ]:


# 查看工作区文件, 该目录下的变更将会持久保存. 请及时清理不必要的文件, 避免加载过慢.
# View personal work directory. All changes under this directory will be kept even after reset. Please clean unnecessary files in time to speed up environment loading.
get_ipython().system('ls /home/aistudio/work')


# 请点击[此处](https://ai.baidu.com/docs#/AIStudio_Project_Notebook/a38e5576)查看本环境基本用法.  <br>
# Please click [here ](https://ai.baidu.com/docs#/AIStudio_Project_Notebook/a38e5576) for more detailed instructions. 

# 
# # 作业要求
# 
# 完成5.6节中1-18精彩案例，19-23选做；
# 编写的程序要尽可能规范，提交的作业要保留运行结果；
# 提交前要生成版本，提交时要等待提交成功后方可退出。

# In[8]:


def demo(*para):
    avg=sum(para)/len(para)
    g=[i for i in para if i>avg]
    return (avg,) +tuple(g)
    
demo(1,2,3,4,5,6)


# In[20]:


def demo(s):
    result=[0,0]
    for ch in s:
        if ch.islower():
            result[1] +=1
        elif ch.isupper():
            result[0] +=1
    return tuple(result)

demo('b,g,s,g,D,d')


# In[25]:


def demo(lst,k):
    x=lst[k-1::-1]
    y=lst[:k-1:-1]
    return list(reversed(x+y))
    
demo([1,2,3,4,5,6,7,7],5)


# In[3]:


def demo(lst,k):
    temp=lst[:]
    for i in range(k):
        temp.append(temp.pop(0))
    return temp
    
demo([1,2,3,4,5,5,6,6,6],4)


# In[5]:


def demo(lst,k):
    return lst[k:]+lst[k:]
    
demo ([1,2,3,3,3,3,4,4,5,6,7,7,],7)


# In[5]:


def yanghui(t):
    print([1])
    line=[1,1]
    print(line)
    for i in range(2,t):
        r=[]
        for j in range(0,len(line)-1):
            r.append(line[j]+line[j+1])
        line=[1]+r+[1]
        print(line)
    
yanghui(6)


# In[6]:


from collections import defaultdict

def yanghui(n):
    triangle=defaultdict(int)
    for row in range(n):
        triangle[row,0]=1
        print(triangle[row,0],end='\t')
        for col in range(1,row+1):
            triangle[row,col]=triangle[row-1,col-1]+triangle[row-1,col]
            print(triangle[row,col],end='\t')
            print()
            
yanghui(14)


# In[13]:


def demo(n):
    def IsPrime(p):
        if p==2:
            return True
        if p%2==0:
            return False
        for i in range(3,int(p**0.5)+1,2):
            if p%i==0:
                return False
        return True
        
    if isinstance(n,int) and n>0 and n%2==0:
        for i in range(2,n//2+1):
            if IsPrime(i) and IsPrime(n-i):
                print(i,'+',n-i,'=',n)
    
demo(78)


# In[17]:


def demo(m,n):
    p=m*n
    while m%n!=0:
        m,n=n,m%n
    return (n,p//n)
    
demo(6,33)


# In[18]:


def demo(m,n):
    import math
    r=math.gcd(m,n)
    return (r,(m*n)//r)
    
demo(6,33)


# In[19]:


def demo(m,n):
    import math
    r=math.gcd(m,n)
    return (r,(m*n)//r)
    
demo(5,76)


# In[21]:


def demo(x,n):
    t1=[i for i in x if i<n]
    t2=[i for i in x if i>n]
    return t1 + [n] + t2
    
demo([1,2,3,4,5,6],4)


# In[23]:


def demo(x,n):
    t1=[]
    t2=[]
    for i in x:
        if i<n:
            t1.append(i)
        elif i>n:
            t2.append(i)
    return t1 + [n] +t2
    
demo([1,4,6,2,5,7,8],6)


# In[28]:


def Rate(origin,userInput):
    if not (isinstance(origin,str) and isinstance(userInput,str)):
        print('The two parameters must be strings.')
        return
    right=sum((1 for o,u in zip(origin,userInput) if o==u))
    return round(right/len(origin),2)
    


# In[1]:


from random import randint
from math import sqrt

def factoring(n):
    if not isinstance(n,int):
        print('You must give me an integer')
        return
    result=[]
    for p in primes:
        while n!=1:
            if n%p==0:
                n=n/p
                result.append(p)
            else:
                break
            else:
                result='*'.join(map(str,result))
                return result
        if not result:
            return n
    testData=[randint(10,100000) for i in range(50)]
    maxData=max(testData)
    primes=[p for p in range(2,maxData) if 0 not in
             [p%d for d in range(2,int(sqrt(p))+1)]]
    
    for data in testData:
        r=factoring(data)
        print(data,'=',r)
        print(data==eval(r))


# In[8]:


from random import randint

def guess(maxValue=100,maxTime=5):
    value=randint(1,maxValue)
    for i in range(maxTimes):
        prompt='Start to Guess:' if i==0 else 'Guess again:'
        
        try:
            x=int(input(prompt))
        except:
            print('Must input an integer between 1 and',maxValue)
        else:
            if x==value:
                print('Congratulations!')
                break
            elif x>value:
                print('Too big')
            else:
                print('Too little')
            
    else:
                print('Game over.FALL.')
                print('The value is ',value)


# In[10]:


def demo(v,n):
    assert type(n)==int and 0<v<10,'v must be integer between 1 and 9'
    result,t=0,0
    for i in range(n):
        t=t * 10+v
        result += t
    return result
    
print(demo(3,4))


# In[12]:


from itertools import cycle

def demo(lst,k):
    t_lst=lst[:]
    while len(t_lst)>1:
        c=cycle(t_lst)
        for i in range(k):
            t=next(c)
        index=t_lst.index(t)
        t_lst=t_lst[index+1:] +t_lst[:index]
    return t_lst[0]
    
lst=list(range(1,11))
print(demo(lst,3))


# In[2]:


def hannoi(num,src,dst,temp=None):
    global times
    assert type(num)==int,'num must be an integer'
    assert num>0,'num must>0'
    if num==1:
        print('The {0} Times move:{1}==>{2}'.format(times,src,dst))
        times+=1
    else:
        hannoi(num-1,src,temp,dst)
        hannoi(1,src,dst)
        hannoi(num-1,temp,dst,src)

times=1
hannoi(3,'A','C','B')


# In[3]:


def main(n):
    start=10**(n-1)
    end=10**n
    for i in range(start,end):
        big=''.join(sorted(str(i),reverse=True))
        little=''.join(reversed(big))
        big,little=map(int,(big,little))
        if big-little==i:
            print(i)

n=4
main(n)


# In[9]:


from random import randint
from itertools import permutations

exps=('((%s%s%s)%s%s)%s%s',
      '(%s%s%s)%s(%s%s%s)',
      '(%s%s(%s%s%s))%s%s',
      '%s%s((%s%s%s)%s%s)',
      '%s%s(%s%s(%s%s%s))')
ops=r'+-*/'

def test24(v):
    result=[]
    
    def check(exp):
        try:
            return eval(exp)==24
        except:
            return False
            
for a in permutations(v):
    t=[exp%(a[0],op1,a[1],op2,a[2],op3,a[3])for op1 in ops for op2 in ops 
    for op3 in ops for exp in exps if check(exp%(a[0],op1,a[1],op2,
    a[2],op3,a[3]))]
    
        if t:
            result.append(t)
return result
    
for i in range(20):
    print('='*20)
    lst=[randint(1,13) for j in range(4)]
    r=test24(lst)
    if r:
        print(r)
    else:
        print('No answer for',lst)


# In[12]:


def myMaxMin(iterable):
    tMax=tMin=iterable[0]
    for item in iterable[1:]:
        if item>tMax:
            tMax=item
        elif item<tMin:
            tMin=item
            
    return (tMax,tMin)
    
myMaxMin((4,1,3,5,6,7,3,2))


# In[14]:


def myAll(iterable):
    for item in iterable:
        if not item:
            return False
    return Ture
    
def myAny(iterable):
    for item in iterable:
        if item:
            return True
    return False
    
def myZip(*iterables):
    min_length=min(map(len,iterables))
    
    for i in range(min_length):
        yield tuple((it[i] for it in iterables))
        


# In[15]:


from random import randint

def bubbleSort(lst,reverse=False):
    length=len(lst)
    for i in range(0,length):
        flag=False
        for j in range(0,length-i-1):
            exp='lst[j]>lst[j+1]'
            if reverse:
                exp='lst[j]<lst[j+1]'
            if eval(exp):
                lst[j],lst[j+1]=lst[j+1],lst[j]
                flag=True
        if not flag:
            break
        
lst=[randint(1,100)for i in range(20)]
print('Before sort:\n',lst)
bubbleSort(lst,True)
print('After sort:\n',lst)


# In[20]:


from random import randint

def bubleSort(lst,end=None,reserve=False):
   if end==None:
       length=len(lst)
   else:
       length=end
   if length<=1:
       return
   flag=False
   for i in range(length-1):
       exp='lst[j]>lst[j+1]'
       if reserve:
           exp='lst[j]<lst[j+1]'
       if eval(exp):
           lst[j],lst[j+1]=lst[j+1],lst[j]
           flag=True
   if flag==False:
       return
   else:
       bubbleSort(lst,length-1,reserve)
       
lst=[randint(1,100) for i in range(20)]
print('Before sorted:\n',lst)
bubbleSort(lst)
print('After sorted:\n',lst)


# In[21]:


def selectSort(lst,reverse=False):
    length=len(lst)
    for i in range(0,length):
        m=i
        for j in range(i+1,length):
            exp='lst[j]<lst[m]'
            if reverse:
                exp='lst[j]>lst[m]'
            if eval(exp):
                m=j
        if m!=i:
            lst[i],lst[m]=lst[m],lst[i]
            

