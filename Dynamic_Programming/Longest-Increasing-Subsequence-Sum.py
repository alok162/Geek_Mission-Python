def lisUtil(arr, n):
    dp=[]
    for i in arr:
        dp.append(i)
    for i in range(1, n):
        for j in range(i):
            if arr[i]>arr[j] and dp[i]<arr[i]+dp[j]:
                dp[i] = arr[i]+dp[j]
    return max(dp)
    
if __name__=="__main__":
    t=int(input())
    for test in range(t):
        n=int(input())
        arr = list(map(int,input().split()))
        print(lisUtil(arr, n))
