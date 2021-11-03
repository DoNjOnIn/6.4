import random

def max(imax,nmax,a,i):
    if i>len(a)-1:
        return imax
    else:
        if a[i] > nmax:
            nmax = a[i]
            imax = i
        return max(imax,nmax, a, i + 1)

def mult(b,i,v):
    v*=b[i]
    if i==len(b)-1:
        return '1 нуль'
    if b[i+1]!=0:
        return mult(b,i+1,v)
    else:
        return v

def shift(b,i,k):
    if len(b)%2==1:
        t=0
    else:
        t=-1
    if i<=len(b)//2+t and k<=len(b)//2+t:
        b[i], b[i+k] = b[i+k], b[i]
        shift(b,i+1,k+1)

def main():
    b=[]
    n=(int(input('n=')))
    m=0
    for i in range(n):
        b.append(random.randint(-5, 5))
    print(b)
    print('N='+str(max(0, b[0], b, 0)+1))
    while m <len(b):
        if b[m]==0:
            print(mult(b,m+1,1))
            break
        if m==len(b)-1:
            print('Немає нулів')
        m+=1
    shift(b,1,1)
    print(b)

if __name__=='__main__':
    main()