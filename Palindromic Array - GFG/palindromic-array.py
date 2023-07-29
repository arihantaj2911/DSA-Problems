# Your task is to complete this function
# Function should return True/False or 1/0
def f(s):
    if s==s[::-1]:
        return True
    return False    
def PalinArray(arr ,n):
    flag = True
    for i in arr:
        if f(str(i))==False:
            flag = False
            break
    
    if flag:
        return True
    
    return False    
        



#{ 
 # Driver Code Starts
# Driver Program
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        if PalinArray(arr, n):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends