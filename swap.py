def swap(directory, first_index, second_index, dict_index=False):
    if type(directory) is list:
        swapped_list = list()
        swap_1 = directory[first_index]
        swap_2 = directory[second_index]
        for items in directory:
            if items == swap_1:
                swapped_list.append(swap_2)
            elif items == swap_2:
                swapped_list.append(swap_1)
            else:
                swapped_list.append(items)
        result = swapped_list
    elif type(directory) is dict:
        swapped_dict = dict()
        swap_1 = None
        swap_1_key = None
        swap_2 = None
        swap_2_key = None
        if dict_index:
            for key,index in enumerate(directory.keys()):
                if key == first_index:
                    swap_1 = directory[index]
                    swap_1_key = index
                elif key == second_index:
                    swap_2 = directory[index]
                    swap_2_key = index
                else:
                    continue

            for index in directory:
                if index == swap_1_key:
                    swapped_dict[swap_2_key] = swap_2
                elif index == swap_2_key:
                    swapped_dict[swap_1_key] = swap_1
                else:
                    swapped_dict[index] = directory[index]

        else:
            swap_1 = directory[first_index]
            swap_1_key = first_index
            swap_2 = directory[second_index]
            swap_2_key = second_index
            for index in directory:
                if index == swap_1_key:
                    swapped_dict[swap_2_key] = swap_2
                elif index == swap_2_key:
                    swapped_dict[swap_1_key] = swap_1
                else:
                    swapped_dict[index] = directory[index]

        result = swapped_dict


    return result


'''def reverse():
    pass

def fill():
    #list elements replace and fill input text

def random():
    #list element random sorting

'''