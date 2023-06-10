#!/usr/bin/python3

def new_in_list(my_list, idx, element):
     new_list = my_list
     for i in range(len(new_list)):
        if idx < 0:
            return new_list
        elif idx > len(new_list):
            return new_list
        elif i == idx:
            my_list[i] = element
            return new_list
