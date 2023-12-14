class Node:
    slots = ['__value','__node']

    def __init__(self,value,next=None):
        self.__value = value
        self.__next = next

    def get_value(self):
        return self.__value
    def set_value(self,value):
        self.__value = value
    def get_next(self):
        return self.__next
    def set_next(self,next):
        self.__next = next
    def __str__(self):
        return str(self.value) + " -> " + str(self.__next)
    
def main():
    node1 = Node(1)
    print(node1)
if __name__ == '__main__':
    main()

