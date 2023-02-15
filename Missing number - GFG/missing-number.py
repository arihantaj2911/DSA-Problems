#User function Template for python3

def missingNumber( A, N):
     # Your code goes here
     total=N*(N+1)//2
     s1=sum(A)
     return total-s1
     


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        print(missingNumber(a, n))

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends