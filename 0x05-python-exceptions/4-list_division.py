#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    sum_list = [0] * list_length
    for i in range(0, list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("divison by 0")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            sum_list[i] = result
    return sum_list
