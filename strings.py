# noinspection PyInterpreter
"""With this string:
'monty pythons flying circus'
Create a function that returns a sorted string with no duplicate characters
(keep any whitespace):
Example: ' cfghilmnoprstuy'
Create a function that returns the words in reverse order:
Example: ['circus', 'flying', 'pythons', 'monty']
Create a function that returns a list of 4 character strings:
Example: ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus']

"""
print ()


import pytest

new_list = []

def no_duplicates(a_string):
    my_list = []
    for leter in a_string :
        my_list.append(leter)
        #print(leter)
    a = len(my_list)
    new_word = ""
    prev_word  = ""
    #print(a)
    while a>0:
        #print(min(my_list))
        if min(my_list) != " ":
            if prev_word != min(my_list):
                new_word += min(my_list)


            prev_word = min(my_list)
            #print(min(my_list))
            my_list.remove(min(my_list))

            #print(my_list)
            #print(new_word)
            a= a-1

        else:
            my_list.remove(min(my_list))
            a=a-1
            #print("new space")

    print(new_word)
    return

    pass


def reversed_words(a_string):

    new_rev_list = []
    new_recive_list = a_string.split(" ")
    print(new_recive_list)
    print(len(new_recive_list))
    a = len(new_recive_list)
    while a>0 :

        new_rev_list.append(new_recive_list[a-1])
        a = a-1

    print(new_rev_list)

    pass


def four_char_strings(a_string):

    new_list.clear()
    while len(a_string)>0 :
        new_list.append(a_string[:4])
        a_string = a_string[4:]
        print(a_string)
    print(new_list)

    return

    pass


def test_no_duplicates():
    s = 'monty pythons flying circus'
    assert no_duplicates(s) == ' cfghilmnoprstuy'


def test_reversed_words():
    s = 'monty pythons flying circus'
    assert reversed_words(s) == ['circus', 'flying', 'pythons', 'monty']


def test_four_char_strings():

    s = 'monty pythons flying circus'
    assert four_char_strings(s) == ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus']


no_duplicates("monty pythons flying circus")
#reversed_words('monty pythons flying circus')

'''
def main():
    return pytest.main(__file__)


if __name__ == '__main__':
    main()
    
'''