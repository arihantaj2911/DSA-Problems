class Solution:
    def duplicates(self,arr,n):
        # Step 1: Create a dictionary to store the frequency of elements
        d = {}
        
        # Step 2: Count the occurrences of each element
        for num in arr:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        
        # Step 3: Create a list to store elements occurring more than once
        d1 = []
        for k,v in d.items():
            if v > 1:
                d1.append(k)
        
        # Step 4: Return the sorted list of d1
        if len(d1)==0:
            d1.append(-1)
        return sorted(d1)


    	   
    	        
    	    


#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends