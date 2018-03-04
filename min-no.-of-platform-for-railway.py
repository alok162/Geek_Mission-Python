t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().strip().split()))
    d=list(map(int,input().strip().split()))
    a.sort()
    d.sort()
    result=1
    platform=i=j=0
    while i<n and j<n:
        if a[i]<d[j]:
            platform+=1
            i+=1
            if platform>result:
                result=platform
        else:
            platform-=1
            j+=1
    print(result)
        
        
        
    
