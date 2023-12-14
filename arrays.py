class Array:
    def __init__(self, length, prototype=None):
        self.__length = length
        self.__data = [prototype] * length
    
    def __len__(self):
        return self.__length

    def __getitem__(self, index):
        self.__index_check(index)

        return self.__data[index]

    def __setitem__(self, index, value):
        self.__index_check(index)
        self.__data[index] = value

    def __index_check(self, index):
        if index < 0 or index >= self.__length:
            raise IndexError("Index out of range: " + str(index))

    def __repr__(self):
        return self.__data.__repr__()

    def __str__(self):
        return self.__data.__str__()
   
    def __iter__(self):
        raise TypeError("'Array' object is not iterable")

    