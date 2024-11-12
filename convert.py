from typing import Optional

#TASK 1
def str_to_float(input: str) -> Optional[float]:
    try:
        floaty = float(input)
        return floaty
    except ValueError:
        return None

#TASK 2:
def gather_numbers() -> list[float]:
    nums1= []
    nums2 = []
    num = 0
    while num != "done":
        num = input("enter a number, or if you are finished, type 'done': ")
        checknum = str_to_float(num)
        nums1.append(checknum)
    for i in nums1:
        if i != None:
            nums2.append(i)
    return nums2

if __name__ == '__main__':
    numss = gather_numbers()
    print(numss)

#TASK 3 in command_line.py