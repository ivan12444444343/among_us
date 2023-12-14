import arrays

class Queue:
    __slots__ = ['__elements','__front','__back','__size']

    def __init__(self,size=3):
        self.__elements = arrays.Array(size)
        self.__front = 0
        self.__back = 0
        self.__size = 0

    def __str__(self):
        string = ''
        i = self.__front
        while i != self.__back:
            string += str (self.__elements [i]) + ', '
            i = (i + 1) % len (self.__elements)
        return '[' + string[:-2] + ']'
    
    def is_empty(self):
        return self.__size == 0
    def size(self):
        return self.__size
    def enqueue(self, value):

        self.__elements[self.__back] = value

        self.__back = (self.__back + 1) % len(self.__elements)

        self.__size += 1

        if self.__back == self.__front:
            self.__resize ()

            
    def front(self):
        if self.__size != 0:
            return self.__elements[self.__front]
        else:
            raise IndexError("front not defined")
        
    def back(self):
        if self.__size != 0:
            return self.__elements[self.__back-1]
        else:
            raise IndexError("back not defined")
        
    def dequeue(self):
        if self.__size != 0:
            front = self.__elements[self.__front]

            self.__elements[self.__front] = None

            self.__front = (self.__front + 1) % len(self.__elements)

            self.__size -= 1

            return front
        
    def __resize(self):

        new_array_size = self.__size * 2
        new_array = arrays.Array(new_array_size)

        i = 0
        j = self.__front

        for _ in range(self.__size):
            if j == self.__size:
                j = 0
            
            new_array[i] = self.__elements[j]

            j+=1
            i+=1

        self.__elements = new_array
        self.__front = 0
        self.__back = self.__size

        
        

        
def main():
    queue = Queue(3)
    print(queue)

    queue.enqueue("Mary Smith")
    queue.enqueue("Barack Obama")

    print("add some people")
    print(queue)

    item_removed = queue.dequeue()
    print("Remove From Line:",item_removed)
    print("line after removed:",queue)

    print("add somemore people...")
    queue.enqueue("Stefon Diggs")
    queue.enqueue("pinta Diggs")
    queue.enqueue("Rhyleigh")
    print(queue)

if __name__ == "__main__":
    main()