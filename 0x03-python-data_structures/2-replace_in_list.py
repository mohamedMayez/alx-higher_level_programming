#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    for i in range(len(my_list)):
        if idx < 0:
            return my_list
        elif idx > len(my_list):
            return my_list
        elif i == idx:
            my_list[i] = element
            return my_list
