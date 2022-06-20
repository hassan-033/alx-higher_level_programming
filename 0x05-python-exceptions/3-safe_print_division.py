/usr/bin/python3
def safe_print_division(a, b):
    try:
        num = a / b
        return num
    except ZeroDivisionError:
        num = None
        return num
    finally:
        print("Inside result: {}".format(num))
