#User function Template for python3

class Solution:
    def toLower (ob, S):
        # code here 
        str = S.lower()
        return str


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S = input()
        
        ob = Solution()
        print(ob.toLower(S))
# } Driver Code Ends