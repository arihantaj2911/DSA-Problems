class Solution:
    def duplicates(self,arr,n):
        # Step 1: Create a dictionary to store the frequency of elements
        freq_dict = {}
        
        # Step 2: Count the occurrences of each element
        for num in arr:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1
        
        # Step 3: Create a list to store elements occurring more than once
        duplicates = []
        for num, freq in freq_dict.items():
            if freq > 1:
                duplicates.append(num)
        
        # Step 4: Return the sorted list of duplicates
        if len(duplicates)==0:
            duplicates.append(-1)
        return sorted(duplicates)


    	   
    	        
    	    


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