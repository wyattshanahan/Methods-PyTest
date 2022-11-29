import pytest
import math
#this py file contains the pytest functions and the corrected original functions


## opens a file in read mode
## filename received as a parameter
def openFile(filename):
    infile = open(filename, "r")

    print("File opened.")

## takes two numbers and returns
## the result of a division
def numbers(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
    except:
        print("Cannot divide by zero")
    return num1 / num2

## takes in two points
## finds the distance between the points

# tests for a correct division by numbers
def test_numbers():
    assert numbers(10, 2) == 5

#tests for a failed division by numbers
def test_numbers_fail():
    assert numbers(10, 2) == 6

#should throw a zero division error
def test_numbers_zero():
    with pytest.raises(ZeroDivisionError):
        numbers(1,0)
def dist(x1, y1, x2, y2):
    dist = 0
    try:
        dist = (x2 - x1) ** 2 + (y2 - y1) ** 2
        dist = math.sqrt(dist)
        return dist
    except TypeError:
        try:
            x1 = float(x1)
            x2 = float(x2)
            y1 = float(y1)
            y2 = float(y2)
        except ValueError:
            return ("Invalid input.")
            #return False
        dist = (x2 - x1) ** 2 + (y2 - y1) ** 2
        dist = math.sqrt(dist)
        return dist
#testing dist, should pass and return a long decimal using only integers
def test_dist_1():
    assert dist(1,2,3,4) == 2.8284271247461903
#testing dist to ensure it can return a distance of zero
def test_dist_2():
    assert dist(4,2,4,2) == 0.0
#testing dist, should return a float with a decimal of zero
def test_dist_3():
    assert (dist(1, 4, 2, 4)) == 1.0
#testing dist to ensure it can handle a mix of floats and integers
def test_dist_4():
    assert (dist(1,2.0,3,4.0)) == 2.8284271247461903
#testing dist with only floats
def test_dist_5():
    assert (dist(1.0,2.0,3.0,4.0)) == 2.8284271247461903
#testing dist with a number stored as a string, this test should attempt conversion due to a typeError
def test_dist_6():
    assert (dist("1",2,3,4)) == 2.8284271247461903
#testing dist with an input including letters stored in a string
def test_dist_7():
    assert (dist("one",2,3,4)) == "Invalid input."
## takes in a string -- reverses it
## then compares the two
# additions: converts input to string and all upper to avoid case issues
def isPalindrome(temp):
    temp = str(temp)
    temp = temp.upper()
    test = temp[::-1]
    if(test == temp):
        return True
    else:
        return False
#tests a palindrome in all lowercase characters
def test_palin_1():
    assert (isPalindrome("racecar")) == True
#tests a palindrome with one capital letter, should fail without converting letters to the same case
def test_palin_2():
    assert(isPalindrome("Racecar")) == True
#tests a palindrome in all uppercase letters
def test_palin_3():
    assert(isPalindrome("RACECAR")) == True
#tests a multiword string that is a palindrome
def test_palin_4():
    assert(isPalindrome("racecar racecar")) == True
#tests an integer that is a palindrome, should fail as it is not iterable
def test_palin_5():
    assert(isPalindrome(616)) == True
#tests a float that is a palindrome, should fail as it is not iterable
def test_palin_6():
    assert (isPalindrome(616.616)) == True
## has input to receive two numbers
## divides the two, then outputs the result
def divide():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    div = num1 / num2

    print("Your numbers divided is:", div)

## returns the squareroot of a particular number
def sq(num):

    try:
        x = math.sqrt(num)
        print(x)
        return math.sqrt(num)
    except ValueError:
        print("Cannot have a square root of a negative number")
    except TypeError:
        num = float(num)
        x = math.sqrt(num)
        print(x)
        return math.sqrt(num)

## grabs user's name
## greets them by their entire name
## names should be strings
def greetUser(first, middle, last):
    print("Hello!")
    print("Welcome to the program", first, middle, last)
    print("Glad to have you!")

## takes in a Python list
## attempts to display the item at the index provided
def displayItem(numbers, index):
    print("Your item at", index, "index is", numbers[index])

# comment
