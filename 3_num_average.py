#!/usr/bin/env python3
# Created By: Tony Tran
# Date: Oct. 25, 2023
# This is program will give you the average using 3 given numbers.


def main():
    num_1 = str(input("Enter First Number:\n"))
    num_2 = str(input("Enter Second Number:\n"))
    num_3 = str(input("Enter Third Number:\n"))
    try:
        num_1 = int(num_1)
        num_2 = int(num_2)
        num_3 = int(num_3)
    except ValueError:
        print("The numbers given were invalid")
    else:
        if (num_1 and num_2 and num_3 <= 100) and (num_1 and num_2 and num_3 >= 0):
            average = round((num_1 + num_2 + num_3) / 3, 2)
            print(f"Your average is {average}")
        else:
            print(
                "Your numbers weren't within equal or lower 100 OR equal or higher than 0"
            )
    finally:
        print("Code Ended")


if __name__ == "__main__":
    main()
