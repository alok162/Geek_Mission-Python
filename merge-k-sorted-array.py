class MinHeap:
    def __init__(self,element,i,j):
        self.element=element
        self.i=i
        self.j=j
def minHeapify(heap,i,n):
    l=(2*i)+1
    r=(2*i)+2
    minimum=i
    if l<n and heap[l].element<heap[i].element:
        minimum=l
    if r<n and heap[r].element<heap[minimum].element:
        minimum=r
    if minimum!=i:
        heap[minimum],heap[i]=heap[i],heap[minimum]
        minHeapify(heap,minimum,n)
    
def mergeKArrays(arr, n):
    heap=[None]*(len(arr[0]))
    for i in range(len(arr[0])):
        heap[i]=(MinHeap(arr[i][0],i,1))
    for i in range((n-2)//2,-1,-1):
        minHeapify(heap,i,len(heap))
    output=[]
    for i in range(n*n):
        temp=heap[0]
        output.append(temp.element)
        if temp.j<n:
            temp.element=arr[temp.i][temp.j]
            temp.j=temp.j+1
        else:
            temp.element=float('inf')
        heap[0]=temp
        minHeapify(heap,0,len(heap))
    return output