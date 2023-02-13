#User function Template for python3

class Solution:
    def leftRotate(self, arr, n, d):
        # code here
        d=d%n
        s=0
        e=d-1
        while s<e:
            arr[s],arr[e] = arr[e],arr[s]
            s+=1
            e-=1
        
        s=d
        e=n-1
        while s<e:
            arr[s],arr[e] = arr[e],arr[s]
            s+=1
            e-=1
        
        arr.reverse()


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        d = int(input())
        ob = Solution()
        ob.leftRotate(arr, n, d)
        for xx in arr:
            print(xx, end=" ")
        print()
        tc -= 1

# } Driver Code Ends