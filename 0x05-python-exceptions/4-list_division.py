#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = list()
    div = 0
    idx = 0
    while idx != list_length:
        try:
            div = my_list_1[idx] / my_list_2[idx]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            idx += 1
            new_list.append(div)
    return new_list
