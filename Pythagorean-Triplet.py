def findTriplet(arr, n):
    arr.sort(reverse=True)
    for i in range(n-2):
        j,k =i+1,n-1
        while j<=k:
            if arr[i]**2==(arr[j]**2)+(arr[k]**2):
                return 'Yes'
            else:
                if arr[i]**2<(arr[j]**2)+(arr[k]**2):
                    j+=1
                else:
                    k-=1
    return "No"
if __name__=="__main__":
    t=int(input())
    for test in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        print(findTriplet(arr,n))
