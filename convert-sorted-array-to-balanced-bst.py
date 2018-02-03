class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def sortedBst(arr, start, end):
    if start>end:
        return None
    else:
        mid = (start+end)//2
        root = Node(arr[mid])
        root.left = sortedBst(arr, start, mid-1)
        root.right = sortedBst(arr, mid+1, end)
        return root
        
def printPreorder(root):
    if root is None:
        return
    else:
        print(root.data, end=" ")
        printPreorder(root.left)
        printPreorder(root.right)
        
if __name__=="__main__":
    t=int(input())
    for test in range(t):
        n=int(input())
        arr = list(map(int,input().split()))
        root = sortedBst(arr, 0, n-1)
        printPreorder(root)
        print()
        
