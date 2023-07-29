# Your task is to complete this function
# Function should return True/False or 1/0
def f(s):
    t = s
    ans = 0
    while t:
        temp = t%10
        ans = ans*10+temp
        t //= 10
    
    if s==ans:
        return True
    
    return False    
    


def PalinArray(arr ,n):
    flag = True
    for i in arr:
        if f(i)== False:
            flag = False
            break
    
    if flag:
        return True
    
    else:
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