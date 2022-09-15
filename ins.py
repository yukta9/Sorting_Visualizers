import time
def insertionSort(array,a,s,speed) :
    for i in range(1,s) :
        temp=a[i]
        j=i-1
        while not (j<0) :
            time.sleep(0.1*speed)
            array(a,["red" if k==j or k==j+1 else "blue" if k<=i-1 else "green" for k in range(len(a))])
            if a[j+1] < a[j] :
                a[j+1],a[j]=a[j],a[j+1]
            else :
                break 
            j-=1
        a[j+1]=temp
    array(a,["blue"]*len(a))

#selection sort
def selectionSort(array,a,s,color,speed) :
    for i in range(s-1) :
        minn=i
        for j in range(i,s) :
            time.sleep(0.1*speed)
            array(a,["blue" if k<i else "red" if k==j else "green" for k in range(len(a))])
            if a[j]<a[minn] :
                minn=j 
        a[i],a[minn]=a[minn],a[i]
    array(a,["blue" for k in range(len(a))])
    print(a)    