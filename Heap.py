'''
Created on Nov 25, 2018

@author: josephbaca
'''


class Heap:
    
    def __init__(self):
        self.heap_array = []
        
    def insertHelper (self, numbers):
        
        for num in numbers:
            self.insert(num)
     
    def insert(self, k):
        self.heap_array.append(k)
        print("Inserting to heap: ", k)
             
        if len(self.heap_array) > 1:
            i = len(self.heap_array)-1
            while i > 0:
                if self.heap_array[(i-1)//2] > self.heap_array[i]:
                    self.swap(i, (i-1)//2)
                i = (i-1)//2
        print(self.heap_array)
        
        
    def swap(self, smaller, bigger):
        
        temp = self.heap_array[bigger]
        self.heap_array[bigger] = self.heap_array[smaller]
        self.heap_array[smaller] = temp
        
        return self.heap_array
    
    def heapify(self):
        
        if len(self.heap_array) > 1:
            i = len(self.heap_array)-1
            while i > 0:
                if self.heap_array[(i-1)//2] > self.heap_array[i]:
                    self.swap(i, (i-1)//2)
                i = i-1
                print("Heapify: ", self.heap_array[(i-1)//2], "&", self.heap_array[i], self.heap_array )
                
                
    def extract_min(self):
        
        if self.is_empty():
            return None
         
        min_elem = self.heap_array[0] 
        self.heap_array.remove(self.heap_array[0])
        print()
        print("extracted: ", min_elem)
        self.heapify()
        return min_elem

    def is_empty(self):
        return len(self.heap_array) == 0
    
    def sortHeap(self):
        sortedArray = []
        
        while self.heap_array != []:
            mini = self.extract_min()
            sortedArray.append(mini)

        return sortedArray
    
def getNumbersFromFile(file):
    try:
        numbers= file.readline().split(',')
        numbers = list(map(int, numbers))
        print("The numbers in the file:", numbers)
        
    except:
        None
    return numbers






myHeap = Heap()
file = open("numbers.txt")
print()
numbers = getNumbersFromFile(file)
print()
myHeap.insertHelper(numbers)

print()
print("The current Heap Array After insertion: " ,myHeap.heap_array)
print("The heap Array after Sort: ", myHeap.sortHeap())


'''
print("Insertions")
myHeap.insert(8)
print(myHeap.heap_array)

myHeap.insert(5)

print(myHeap.heap_array)

myHeap.insert(15)

print(myHeap.heap_array)
myHeap.insert(3)

print(myHeap.heap_array)

myHeap.insert(1)

print(myHeap.heap_array)
print()
print("Sorted Algorithm: ")
print(myHeap.sortHeap())
'''





