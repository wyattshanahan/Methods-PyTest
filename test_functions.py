import pytest
import math
from functions import *
#this py file contains the pytest functions and the uncorrected original functions

# TESTS FOR OPENFILE

# TESTS FOR NUMBERS
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

# tests the function using an integer and a float, should return an integer
def test_numbers_1flt():
    assert numbers(5,5.0) == 1.0

# TESTS FOR DIST
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

# TESTS FOR ISPALINDROME

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

# TESTS FOR DIVIDE


# TESTS FOR SQ

## returns the squareroot of a particular number

def test_sq_negative():
    with pytest.raises(ValueError):
        sq(-1)
def test_sq():
    assert sq(4) == 2
def test_sq_is_float():
    assert sq(4) == 2
def test_sq_string():
    assert sq("4") == 2
def test_sq_str2():
    assert sq(float("4")) == 2
## grabs user's name
## greets them by their entire name
## names should be strings

# TESTS FOR GREETUSER
def test_greetUser(capsys):
    greetUser("John", "Robert", "Doe")

    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout == "Hello!\nWelcome to the program John Robert Doe\nGlad to have you!\n"

## takes in a Python list
## attempts to display the item at the index provided

# TESTS FOR DISPLAYITEM

#tests for correct output
def test_displayItem(capsys):
    displayItem([0, 1, 2, 3], 3)
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout == "Your item at 3 index is 3\n"
# should raise an index error, because tried to get an index that is out of reach of the list
def test_displayItem_indexErr():
    assert displayItem([0, 1, 2], 5) == "index error"
# should raise a type error, because the index variable must be an integer
def test_displayItem_PLACEHOLDER():
    assert displayItem([0, 1, 2, 3], "five") == "type error"
