#User function Template for python3

class Solution:
    def transform(self, s):
        # code here
        lst = list(s)
        if lst[0].islower():
            lst[0] = lst[0].upper()
        for i in range(1,len(lst)):
            if lst[i] == ' ' and lst[i+1].islower():
                lst[i+1] = lst[i+1].upper()
            else:
                continue
        return ''.join(lst)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        print(ob.transform(s))
# } Driver Code Ends