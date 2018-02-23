#Dynamic programming

#finding max stoling value function
def max_Stolen_Util(arr, n):
    val1 = arr[0]
    if n==1:
        return val1
    val2 = max(arr[0], arr[1])
    if n==2:
        return val2
    max_stolen = 0
    for i in range(2,n):
        #Avoiding calculation of subproblem by 
        #storing into val1 and val2 variable
        max_stolen = max((val1 + arr[i]), val2)
        val1 = val2
        val2 = max_stolen
    return max_stolen

#main function or driven programa
if __name__=='__main__':
    #take number of test cases input
    t=int(input())
    for test in range(t):
        #input number of element in a array
        n=int(input())
        arr = list(map(int,input().split()))
        print(max_Stolen_Util(arr, n))
    