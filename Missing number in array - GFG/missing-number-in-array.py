#User function Template for python3


class Solution:
    def MissingNumber(self,array,n):
        # code here
        total = int(n*(n+1)/2)
        sum_A = sum(array)
        return total - sum_A
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().MissingNumber(a,n)
    print(s)
# } Driver Code Ends