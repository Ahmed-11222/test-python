def binary_search(key,lst):
    li, hi=0,len(lst)-1
    low=0
    while(li<=hi):
        mid=int((hi+li)/2)
        if(lst[mid]==key):
            return mid
        elif(lst[mid]<key):
            li =mid+1
        else:
            hi =mid-1
    return -1
num=[10,50,20,70,80,40,30]
num.sort()
target=int(input("target:"))
result=print("index:", binary_search(target,num))
