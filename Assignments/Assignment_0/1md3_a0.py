
'''

Name: Luca Mawyin
MACID: mawyinl
Date: September 10, 2024

Write a program that implements functions in finding area of recangle
given user inputted length + width

'''

def area(length, width):
    return length*width

def main():
    length = -1
    width = -1

    while length < 0 or width < 0:
        length = int(input("Enter rectangle length: "))
        width = int(input("Enter rectangle width: "))

    print("Area is", area(length,width))

if __name__ == "__main__":
    main()