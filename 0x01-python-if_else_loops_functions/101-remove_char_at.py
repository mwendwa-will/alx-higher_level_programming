#!/usr/bin/python3

def remove_char_at(str, n):
    new_string = str * 1
    my_list = list(new_string)
    for i in range(len(my_list)):
        if i < n:
            continue
        elif i <= n and i < len(my_list) - 1:
            my_list[i] = my_list[i+1]
            continue
    my_list = ''.join(my_list)
    return(my_list)
