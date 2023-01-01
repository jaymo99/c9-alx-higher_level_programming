#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nb_print = 0

    while (nb_print < x):
        try:
            print("{}".format(my_list[nb_print]), end='')
            nb_print = nb_print + 1
        except IndexError:
            break

    print()
    return (nb_print)
