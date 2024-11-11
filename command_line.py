#TASK 3
import sys
import convert

def arg_convert_total(input: sys.argv):
    total = 0
    floats = []
    for i in input:
        num = convert.str_to_float(i)
        floats.append(i)
    for i in floats:
        if i is not None:
            total = total + i
    return total

if __name__ == '__main__':
    print(arg_convert_total(sys.argv[1:]))
