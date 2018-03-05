#A algorithm to count pairs with given sum

from collections import defaultdict
#function to calculate number of paris in an array
def countPairSum(d, arr, sum):
    count = 0
    #storing every array element in dictionary and
    #parallely checking every element of array is previously
    #seen in dictionary or not
    for i in arr:
        if sum-i in d:
            count+=d[sum-i]
            d[i]+=1
        else:
            d[i]+=1
    return count
    
#main function or driven program
if __name__=='__main__':
    #taking input number of test cases
    t=int(input())
    for test in range(t):
        #taking input n number of element in an array
        #and sum is to find pair through array element
        n, sum = map(int,input().split())
        arr = list(map(int,input().split()))
        #defining dictionary
        d = defaultdict(int)
        print(countPairSum(d, arr, sum))
