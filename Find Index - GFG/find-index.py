#User function Template for python3

class Solution:
    def findIndex (self,a, N, k):
        # code he
        # cnt=[]
        # for i in range(N):
        #     if a[i] ==k:
        #         cnt.append(i)
        # if len(cnt)==0:
        #     return [-1,-1]
        
        # return cnt[0],cnt[-1]    
        res = []
        j =0
        for i in range(N):
            if a[i]==k:
                j =i
                res.append(i)
                break
        for i in range(N-1,j-1,-1):
            if a[i] == k:
                res.append(i)
                break
            
            if len(res)==0:
                return [-1,-1]
        return res
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    key=int(input())
    ob = Solution()
    ans=ob.findIndex(a, n, key )
    print(*ans)
    
# } Driver Code Ends