#Dynamic Programming to climb nth stairs using two steps

#function to count steps
def countWaysUtil(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    #creating array for memoisation the repeated calculation
    dp = [None]*n
    dp[0], dp[1] = 1, 1
    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n-1]
if __name__=='__main__':
    #input number of test cases to run
    t = int(input())
    for test in range(t):
        #take input to climb nth stairs
        n = int(input())
        print(countWaysUtil(n))
        
