from MaxHeap import MaxHeap

class pQueue(object):
    def __init__(self,size) :
        # Build the Constructor
        self.__myHeap = MaxHeap(size)

    def insert(self, data):
        self.__myHeap.insert(data)
        
    def maximum(self):
        return self.__myHeap.maximum()
    
    def extractMax(self):
        return self.__myHeap.extractMax()

    def isEmpty(self):
        # Return true when the priority queue is empty
	print("isEmpty called")
    
    def printQueue(self):
        # followed by each element separated by a comma. 
        # Do not add spaces between your elements.
        #
        # (Optional; python gives us ~*~ magic methods ~*~ and there happens to 
        # be one for strings (def __str__) You can replace this method (printQueue)
        # with the magic method __str__, and use it to return the string 
        # representation of your Queue if it pleases you.)
	self.__myHeap.printOut()
