import time
st = time.time()


def merge(dataset, l, m, r):
    a = m - l + 1
    b = r - m
 

    L = [0] * (a)
    R = [0] * (b)
    for i in range(0, a):
        L[i] = dataset[l + i]
 
    for j in range(0, b):
        R[j] = dataset[m + 1 + j]
 
    i = 0     
    j = 0    
    k = l     
 
    while i < a and j < b:
        if L[i] <= R[j]:
            dataset[k] = L[i]
            i += 1
        else:
            dataset[k] = R[j]
            j += 1
        k += 1
 
    while i < a:
        dataset[k] = L[i]
        i += 1
        k += 1
 
    while j < b:
        dataset[k] = R[j]
        j += 1
        k += 1
 
 
def mergeSort(dataset, l, r):
    if l < r:
        m = l+(r-l)//2
        mergeSort(dataset, l, m)
        mergeSort(dataset, m+1, r)
        merge(dataset, l, m, r)
 
 
import random
dataset=[]
for i in range(4902939):
    #x=random.randrange(0, 500000339783)
    dataset.append(x)
n = len(dataset)
for i in range(n):
    print("%d" % dataset[i],end=" ")
 
mergeSort(dataset, 0, n-1)
for i in range(n):
    print("%d" % dataset[i],end=" ")


et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
