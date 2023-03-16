#User function template for Python 3

class Solution:
    def majorityElement(self, A, N):
        #Your code here
        d = dict({})
        for i in A:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        ans =-1
        for i in d:
            if d[i] > len(A)/2:
                ans = i
        
        return ans        
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends