import node

class Stack:
    __slots__ = ['__top','__size']
    
    def __init__(self):
        self.__top = None
        self.__size = 0

    def __str__(self):

        node = self.__top
        string = ""

        if self.__top is not None:
            string += str(node.get_value())

            node = node.get_next()

            while node is not None:
                string += "," + str(node.get_value())
                node = node.get_next()

        return "[" + string + "]"
    

    def __len__(self):
        return self.__size
 

    def push(self,value):
        new_node = node.Node(value, self.__top )
        self.__top = new_node
        self.__size = 0

    def peek(self):
        if self.__top  is None:
            raise IndexError("peek from empty list")
        value = self.__top.get_value()
        return value
    
    def pop(self):
        if self.__top is None:

            raise IndexError("pop from empty list")
        
        top = self.__top
        value = top.get_value()

        self.__size -= 1

        self.__top = top.get_next()

        return value
    
    def main():
        book_stack = Stack()
        book_stack.push("Intro to CS")
        book_stack.push("HTML for dummies")
        book_stack.push("QR Codes")

        print(book_stack)

        print("length of book: ",len(book_stack))

        print("book at the top of the pile (peek): ",book_stack.peek())

        print("now lets pop a book")
        book_stack.pop()
        print("book at the top of of pile(peek) after pop" ,book_stack.peek())
        book_stack.pop()
        print("book at the top of of pile(peek) after pop" ,book_stack.peek())
        book_stack.pop()
        print("book at the top of of pile(peek) after pop" ,book_stack.peek())
        book_stack.pop()
        
    if __name__ == "__main__":
        main()