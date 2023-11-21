#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = list()
    for idx in range(list_length):
        try:
            new_list.append(my_list_1[idx] / my_list_2[idx])
        except TypeError:
            print("wrong type")
            new_list.append(0)
            continue
        except ZeroDivisionError:
            print("division by zero")
            new_list.append(0)
            continue
        except IndexError:
            print("out of range")
            new_list.append(0)
            continue
        finally:
            pass
    return new_list
