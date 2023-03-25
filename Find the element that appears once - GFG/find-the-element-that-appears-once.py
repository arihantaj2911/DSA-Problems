#User function Template for python3
class Solution:
    def search(self, A, N):
        # your code here
        # maxi = A[0]
        # for i in range(len(A)):
        #     maxi = max(maxi,A[0])
        # hash[maxi] = 0
        # for i in range(len(A)):
        #     hash[A[i]] += 1
        
        # for i in range(len(A)):
        #     if(hash[A[i]]) == 1:
        #         return arr[i]
        d = dict({})
        for i in A:
            if i in d.keys():
                d[i] += 1
            
            else:
                d[i] = 1
        
        for i in d:
            if d[i]==1:
                return i


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		n = int (input ())
		arr = list(map(int, input().split()))
		ob = Solution()
		print(ob.search(arr, n)) 
# } Driver Code Ends