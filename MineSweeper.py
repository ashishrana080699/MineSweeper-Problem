count=0
for k in range(10):
   #Enter number of rows and column seperated by space
    m,n = map(int,input().split())
    if m==0 and n==0:
        break
    print("Enter the elements of the matrix in the form of '*' and '-' :")
    a = [[str(input()) for i in range (n)] for y in range(m)] 
       
    for i in range(m):
        for j in range(n):
            if a[i][j]=="*":
                if i<m-1 and j<n-1:
                    if a[i+1][j+1]=="-" or a[i+1][j+1]==0:
                        a[i+1][j+1]=1
                    elif type(a[i+1][j+1])==int :
                        a[i+1][j+1]+=1
                if  i>0 and j>0:
                    if a[i-1][j-1]=="-" or a[i-1][j-1]==0:
                        a[i-1][j-1] =1
                    elif type(a[i-1][j-1])==int :
                        a[i-1][j-1]+=1
                if i>0:
                    if a[i-1][j]=="-" or a[i-1][j]==0:
                        a[i-1][j]=1
                    elif type(a[i-1][j])==int:
                        a[i-1][j]+=1
                if i>0 and j<n-1:
                    if a[i-1][j+1]=="-" or a[i-1][j+1]==0:
                        a[i-1][j+1]=1
                    elif type(a[i-1][j+1])==int:
                        a[i-1][j+1]+=1
                if j>0:
                    if a[i][j-1]=="-" or a[i][j-1]==0:
                        a[i][j-1]=1
                    elif type(a[i][j-1])==int :
                        a[i][j-1]+=1
                if j<n-1:
                    if a[i][j+1]=="-" or a[i][j+1]==0:
                        a[i][j+1]=1
                    elif type(a[i][j+1])==int:
                        a[i][j+1]+=1
                if i<m-1 and j>0:
                    if a[i+1][j-1]=="-" or a[i+1][j-1]==0:
                        a[i+1][j-1]=1
                    elif type(a[i+1][j-1])==int:
                         a[i+1][j-1]+=1
                if i<m-1:
                    if a[i+1][j]=="-" or a[i+1][j]==0:
                        a[i+1][j]=1
                    elif type(a[i+1][j])==int :
                        a[i+1][j]+=1
            elif a[i][j]=='-':
                a[i][j]=0
    count+=1
    print("\n\nField#",count,  end="")            
    for i in range(m):
        print("\n")
        for j in range(n):
            print(a[i][j],end="  ")
