import sys
import numpy
import struct
import binascii
from PIL import Image

def reverseDigits(digit, lst):
    digit = digit[2:]                               #Deletes the 0b at the beginning
    if(len(digit) == 1):                            #Since python removes 0's in the left side, and we need them there...
        digit = "0" + digit                         #... We put it there
    digit = digit[1] + digit[0]                     #Change the first element with the second, and vice-versa
    lst.append(digit)                               #And finally put these two bits in the list
    return lst
        
def embed(imgFile):
    img = Image.open(imgFile)
    width, height = img.size
    conv = img.convert('RGBA').getdata()
    lst = []
    for h in range(height):
        for w in range(width):
            r, g, b, a = conv.getpixel((w, h))
            reverseDigits(bin(r & 3), lst)
            reverseDigits(bin(g & 3), lst)
            reverseDigits(bin(b & 3), lst)
    return lst

def getSize(vec):
    i = 0
    size = []
    while (i < len(vec) - 1):
        aux = vec[i:i+8]
        size.insert(0, aux)
        i += 8
    return int("".join(size), 2)

if __name__ == '__main__':
    lst = ''.join(embed(sys.argv[1]))               #Joins all elements of the list into a string without spaces
    size = getSize(lst[:33])                        #Gets the size of the object hidden in the image
    lst = lst[32:]                                  #Removes the size info from the list
    lst = lst[:(size * 8)]                          #Removes the trash from the list that is after the size
    lst = hex(int(lst, 2))[2:-1]                    #Converts into hexadecimal, deleting the 0x at the beginning, and the final L
    print(binascii.a2b_hex(lst))                    #Prints the hexadecimal in a way that the computer can interpret it