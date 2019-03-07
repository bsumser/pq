class MaxHeap(object):

	def __init__(self, size):
		# finish the constructor, given the following class data fields:
		self.__MaxSize = size
		self.__length = 0
		self.__heap = [0]

		''' free helper functions '''
	def getHeap(self):
		return self.__heap	

	def getMaxSize(self):
		return self.__maxSize
	
	def setMaxSize(self, ms):
		self.__maxSize = ms
		# May need to add more code here if you want to use this method

	def getLength(self):
		return self.__length
	
	def setLength(self, l):
		self.__length = l
	
	''' Required Methods '''
	def insert(self, data):
		# Insert an element into your heap.
		
		# When adding a node to your heap, remember that for every node n, 
		# the value in n is greater than or equal to the values of its children, 
		# but your heap must also maintain the correct shape.
		#print("insert called in MaxHeap")
		self.__length += 1
		self.__heap.insert(self.__length, data)

                cur = self.__length

                while(cur != 1):
                    if (cur % 2) == 0:
                        #check if parent is less
                        if data < self.__heap[cur / 2]:
                            self.__heap[cur / 2], self.__heap[cur] = self.__heap[cur], self.__heap[cur / 2]
                        else:
                            cur = 1
                    elif ((cur - 1) % 2 == 0):
                        if data < self.__heap[(cur - 1) / 2]:
                            self.__heap[(cur - 1) / 2], self.__heap[cur] = self.__heap[cur], self.__heap[(cur - 1) / 2]
                        else:
                            cur = 1
	def maximum(self):
		# return the max value in the heap
		#print("maximum called in MaxHeap")
		print self.__heap[1]
		return self.__heap[1]

	def extractMax(self):
		# remove and return the maximum value in the heap
		#print("extractMax called in MaxHeap")
		if self.__length < 1:
				print("underflow error")

		maxi = self.__heap[1]


                #swap first item and last item
                self.__heap[1] = self.__heap[self.__length]
		self.__length -= 1
		self.__heapify(1)
		print maxi
		return maxi
	
	def __heapify(self, i):
		# helper function for reshaping the array
		#print("heapify called in MaxHeap")

                l = 2*i
                r = 2*i + 1

                if l < self.__length and self.__heap[l] > self.__heap[i]:
                    heapify = l
                else:
                    heapify = i
                if r < self.__length and self.__heap[r] > self.__heap[heapify]:
                    heapify = r

                if heapify != i: #one child node is larger, so swap
                    self.__heap[i], self.__heap[heapify] = self.__heap[heapify], self.__heap[i]

                    #reccursive heapify call
                    #self.__heapify(heapify)

	''' Optional Private Methods can go after this line '''
	# If you see yourself using the same ~4 lines of code more than once...
	# You probably want to turn them into a method.

	def parent(self, i):
		return (i-1)/2
	
	def printOut(self):
		print("Current queue: "),
                for item in self.__heap[1:]:
			print item,
		print ''

	def percUp(self, i):
            parentIndex = i / 2
            cur = i

            while (cur > 0 and self.__heap[parentIndex] > self.__heap[cur]):
                    self.__heap[parentIndex], self.__heap[cur] = self.__heap[cur], self.__heap[parentIndex]
                    cur = parentIndex
                    parentIndex = parentIndex / 2
