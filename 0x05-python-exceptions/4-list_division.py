#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = list()
    for idx in range(list_length):
        try:
            new_list.append(my_list_1[idx] / my_list_2[idx])
        except TypeError:
            print("wrong type")
            new_list.append(0)
        except ZeroDivisionError:
            print("division by zero")
            new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.append(0)
        finally:
            pass
    return new_list
