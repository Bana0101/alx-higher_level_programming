#!/usr/bin/python3
def weight_average(my_list=[]):
    total_w= 0
    total_s = 0
    if my_list is None:
        return 0
    for x in my_list:
        score, weight = x
        total_s += score * weight
        total_w += weight
    return total_s / total_w
