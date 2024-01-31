def solve(A):

    def partition(l,r):
        p=l
        p1=l+1
        p2=r

        while(p2>=p1):
            if(A[p1]<A[p]):
                p1+=1
            elif(A[p2]>A[p]):
                p2-=1
            else:
                A[p1],A[p2]=A[p2],A[p1]
                p1+=1
                p2-=1

        A[p],A[p2]=A[p2],A[p]

        return p2

    def quicksort(l,r):
        if l>r:
            return
        pivot = partition(l,r)
        quicksort(l,pivot-1)
        quicksort(pivot+1,r)


    quicksort(0,len(A)-1)
    return A




A=[127,3,1124,7,2,3]

print(solve(A))







