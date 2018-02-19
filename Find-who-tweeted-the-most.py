from collections import defaultdict,OrderedDict

#print the data
def printDict(d):
    count = d[0][1]
    for i in d:
        if i[1]==count:
            print(i[0],i[1])

#a functiona to sort alphabetically and value of dictionary
def sortDict(d):
    sorted_list=sorted(d.items(), key=lambda x: x[0])
    myOrdDic = OrderedDict(sorted_list)
    copyD = sorted(myOrdDic.items(), key=lambda x: x[1], reverse=True)
    printDict(copyD)
    
# a function to store the data into dictionary
def findUtil(d, n):
    for i in range(n):
        user_name, tweet_id = map(str,input().split())
        d[user_name]+=1
    sortDict(d)

# main or driven function
if __name__=='__main__':
    t=int(input())
    for test in range(t):
        n=int(input())
        d=defaultdict(int)
        findUtil(d, n)
            
