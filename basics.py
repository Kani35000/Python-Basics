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

# write a function that produces all prime numbers of any given range
# findPrimeNumbers(toprange, downrange)
# example findPrimeNumbers(2, 100)
# factors that make a prime number 
# a. it divides only itself and 1
# b. it doesnot divide by factors(2, 3, 5 nor 7) without a remender

def findPrimeNumbers(downrange, toprange):
    """this returns a list of prime numbers between the top rage and down range"""
    listRange= list(range(downrange, toprange+1))
    for number in listRange:
        for factor in range(downrange, int(number ** 0.5)+1): 
            if number%factor==0:
                primeList=listRange.remove(number)
    return primeList
       
            
# static and instance Methods in classes
class Wordset:
    def __init__(self):
        self.words=set()
    def addText(self,text):
        # instance method here
        text=Wordset.cleanText(text)
        for word in text.split():
            self.words.add(word)

    def cleanText(text):
        # cleaning function
        text.replace('!','').replace('.','').replace('\'','')
        return text.lower()

wordset= Wordset()

wordset.addText('Hi, I\'m Kani! Here\'s a sentence I want to add')
wordset.addText('Heres another sentence I want to aff again')

print(wordset.words)

class Wordset2:
    # Another way but making replacepuncs itsown variable and having a chaining function
    replacePuncs= ('!','.',',','\'')
    def __init__(self):
        self.words=set()

    def addText(self,text):
            # instance method here
            text= Wordset2.cleanText(text)
            for word in text.split():
                self.words.add(word)

    # using decorators
    
    def cleanText(text):
        # chaining function
        for punc in Wordset2.replacePuncs:
            text= text.replace(punc,'')

        return text.lower()
wordset2=Wordset2()

wordset2.addText('Hi, I\'m Kani! Here\'s a sentence I want to add')
wordset2.addText('Heres another sentence I want to aff again')

print(wordset2.words)

class Wordset3:
    
    def __init__(self):
        self.words=set()

    def addText(self,text):
        # instance method here
        text= self.cleanText(text)
        for word in text.split():
            self.words.add(word)

    @staticmethod
    def cleanText(text):
        # chaining functions
        text= text.replace('!','').replace(',','').replace('\'', '').replace('\'','')

        return text.lower()
wordset3 = Wordset3()

wordset3.addText('Hi, I\'m Kani! Here\'s a sentence I want to add')
wordset3.addText('Heres another sentence I want to aff again')

print(wordset3.words)


#class Inheritance
class Dog:
    _legs = 4
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + 'says: Bark!')

    def getLegs(self):
        return self._legs

class Chihuahua(Dog):
    def speak(self):
        print(f'{self.name} says: yap yap yap!')

dog = Chihuahua('Roxy')
# dog.speak()


#  using python built-in class 
myList = list()
class UniqueList(list):
    def append(self, item):
        if item in self: 
            # calling append in the parent class we use "super"
            return 
        super().append(item)
uniqueList = UniqueList()
uniqueList.append(1)
uniqueList.append(2)
uniqueList.append(3)

print(uniqueList)
