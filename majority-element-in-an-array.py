#util function to find majority element in an array
def majorityUtil(arr, n):
    elem = 0
    count = 1
    for i in range(1, n):
        if arr[elem] == arr[i]:
            count+=1
        else:
            count-=1
        if count==0:
            elem = i
            count=1
    return arr[elem]

def checkMajorElem(melem, arr, n):
    count = 0
    for i in arr:
        if i == melem:
            count+=1
    # print(melem, count)
    if count > n//2:
        print(melem)
    else:
        print('NO Majority Element')

if __name__=='__main__':
    t=int(input())
    for test in range(t):
        n=int(input())
        arr = list(map(int,input().split()))
        melem = majorityUtil(arr, n)
        checkMajorElem(melem, arr, n)
            
