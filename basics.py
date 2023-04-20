from decimal import Decimal, getcontext

def factorial(num):
    ''' Performs factorial
    example 5!= 5*4*3*2*1
                =120
    '''
    j=1
    if type(num)!= int and num <=1:
        print("num is not a positive integer")
    else:
        for n in range(num+1):
            if n>=1:
                j=n*j
        return j


def hextodec(hex_string):
    """Converts a string hexa decimal number into a
#     interger decimal without using 'int' eg.
#      hextodec('3c0')   == 960
#     """
 
    hex_values = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
        '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
    }

    #Checking throuh the dictionary if every char of hex_string is in the dictionary
    for char in hex_string:
        if char not in hex_values:
            return None

    decimal_value = 0
    power = len(hex_string) - 1
    for char in hex_string:
        decimal_value += hex_values[char.upper()] * (16 ** power)
        power -= 1
    return decimal_value


# write a function encoding that will encode a string 'AAAAABBBBCCCCCCC' 
# to become a list of tuple [('A',5),('B',4),('C',7)]
# Also write a function that will decode the list of tuple back to string.

def encodeString(stringVal):
    """This is a function encoding that will encode a string like 'AAAAABBBBCCCCCCC' 
     to become a list of tuple [('A',5),('B',4),('C',7)]
    """
    encodedList=[]
    prevChar=stringVal[0]
    count=0
    for char in stringVal:
        count+=1
        if prevChar!=char:         
            encodedList.append((prevChar,count))
            prevChar=char
            count=0
    encodedList.append((prevChar,count))
    return encodedList


def decodeTuple(encodedList):
    """  this is a function that will decode the list of tuple produced
    by the encoding function above back to string.
    """
    decodedString=""
    for item in encodedList:
        decodedString= decodedString + item[0] * item[1]
        
    return decodedString


# if values=[[1,'i','a'],[2,'we','be','it'],[3,'are','few', 'two']]
# write a function to create a dictionary structure like below 
"""{
    1:['i','a']
    2:['we','be','it']
    3:['are','few', 'two']
}"""

def createDict(values):
    """creating new dictionary structure from a list using comprehension"""
    return {item[0]:item[1:] for item in values}