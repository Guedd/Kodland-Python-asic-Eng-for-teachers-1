# The envirment is showing sysntax error,
# even using the main to show the tests,

# you'll find the code on the link below:

# https://github.com/Guedd/Kodland-Python-asic-Eng-for-teachers-1/blob/main/N1.py

class n1:
    def init(self, num_List) -> list:
        self.num_List = []
     
    def get_n1(self) -> str:
        print(f'{self.num_List}')
        
    def set_n1(self, num_list) -> list:
        self.num_List = num_list
        
    def shrink(self) -> list:
        if self.num_List == []:
            print("The list is empty!!!")
            return 0
            
        if str in map(type, self.num_List):
            print('\nError: The list contains string(s)!!!')

        if 0 not in self.num_List:
           # check if the list don't cantain zeros
            print("\nthe list donn't contains zeros")
            print("the list is: {}\n".format(self.num_List))
            return self.num_List

        else:
            print("\nthe Original list: {}".format(self.num_List))
            self.num_List = self.zero_drop()
            print("the final list: {}\n".format(self.num_List))
            return self.num_List

    def zero_drop(self) -> list:
       # drop all the zeros from the list
       self.orignal_length = len(self.num_List)
       self.num_List = [i for i in self.num_List if i != 0]
       self.length = self.orignal_length - len(self.num_List)
       return self.zero_append(self.length)
    
    def zero_append(self, length) -> list:
       # add the exact number of zeros we drop at the end
        for i in range(length):
            self.num_List.append(0)
        return self.num_List


if __name__ == '__main__':

    A = [1, 0, 0, 5]
    B = [0, 0, 5]
    C = [1, 4, 0, 5, 0]
    D = [1, 5, '3', 5]
    E = [1, 0, 5]
    F = [1, 4, 7, 9, 21, 20, 5]
    X = []

    test = n1()
    test.set_n1(A)
    test.shrink()
    test.set_n1(C)
    test.shrink()
    test.set_n1(D)
    test.shrink()
    test.set_n1(F)
    test.shrink()
    test.set_n1(X)
    test.shrink()
    
