#!/usr/bin/python3
"""
0_main
"""
rain = __import__('0-rain').rain

if __name__ == "__main__":
    walls = [0, 1, 0, 2, 0, 3, 0, 4]
    print(rain(walls))
    walls = [2, 0, 0, 4, 0, 0, 1, 0]
<<<<<<< HEAD
    print(rain(walls))
=======
    print(rain(walls))
>>>>>>> 5183e1d395d233f636521de863fe69ab94e10ab5
