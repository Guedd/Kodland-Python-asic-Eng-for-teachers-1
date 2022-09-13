def shrink(int_list) -> list:
    if str in map(type, int_list):
        raise TypeError('The list contains only strings')

    if 0 not in int_list:
        # check if the list don't cantain zeros
        print(
        "\nthe final list is: {}\n".format(int_list))
        return int_list

    else:
        int_list = zero_drop(int_list)
        print("\nthe final list: {}\n".format(int_list))
        return int_list

def zero_drop(int_list):
    # drop all the zeros from the list
    orignal_length = len(int_list)
    int_list = [i for i in int_list if i != 0]
    length = orignal_length - len(int_list)
    return zero_append(int_list, length)
    
def zero_append(int_list, l):
    # add the exact number of zeros we drop at the end
    for i in range(l):
        int_list.append(0)
    return int_list
            

if __name__ == '__main__':

    A = [1, 0, 0, 5]
    B = [0, 0, 5]
    C = [1, 4, 0, 5]
    D = [1, 5, '3', 5]
    E = [1, 0, 5]
    F = [1, 4, 0, 5]

    shrink(A)
    shrink(B)
    shrink(C)
    shrink(D)
    shrink(E)
    shrink(F)
