def countUtil(arr, x, n):
    if n==0:
        return -1
    else:
        left = firstHalf(arr, 0, n-1, x)
        if left==-1:
            return -1
        right = secondHalf(arr, 0, n-1, x)
        return right-left+1
        
def firstHalf(arr, start, end, x):
    if start>end:
        return -1
    else:
        mid = (start+end)//2
        if arr[mid]==x and (arr[mid-1]<x or mid==0):
            return mid
        elif arr[mid]<x:
            return firstHalf(arr, mid+1, end, x)
        else:
            return firstHalf(arr, start, mid-1, x)
def secondHalf(arr, start, end, x):
    if start>end:
        return -1
    else:
        mid = (start+end)//2
        if (mid==len(arr)-1 or arr[mid+1]>x) and arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return secondHalf(arr, start, mid-1, x)
        else:
            return secondHalf(arr, mid+1, end, x)

if __name__=="__main__":
    t=int(input())
    for test in range(t):
        n, x = map(int,input().split())
        arr = list(map(int,input().split()))
        print(countUtil(arr, x, n))
