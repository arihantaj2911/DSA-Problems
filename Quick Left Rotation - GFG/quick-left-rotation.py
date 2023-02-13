class Solution:
    def leftRotate(self, arr, k, n):
        # Your code goes here
        k=k%n
        
        s=0
        e=k-1
        while s<e:
            arr[s],arr[e]=arr[e],arr[s]
            s+=1
            e-=1
        
        s=k
        e=n-1
        while s<e:
            arr[s],arr[e]=arr[e],arr[s]
            s+=1
            e-=1
            
        arr.reverse()
        
        
        
            

#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        k=l[1]
        a = list(map(int,input().split()))
        ob = Solution()
        ob.leftRotate(a,k,n)
        print(*a)
# } Driver Code Ends