"""We have an existing dictionary that maps US states to their capitals.
1. Print the state capital of Idaho
2. Print all states.
3. Print all capitals.
4. Create a single string 'Alabama -> Montgomery, Alaska -> Juneau, ...'
5. Ensure the string you created in 4. is alphabetically sorted by state
7. Now we want to add the reverse look up, given the name of a capital what state
is it in?
Implement the function def get_state(capital): below so it returns the state.
GOTCHAS: What happens if two states have the same capital name, how do you
handle that?

"""
import sys

import pytest



STATES_CAPITALS = {
    'Alabama' : 'Montgomery',
    'Alaska' : 'Juneau',
    'Arizona' : 'Phoenix',
    'Arkansas': 'Little Rock',
    'California' : 'Sacramento',
    'Colorado' : 'Denver',
    'Connecticut' : 'Hartford',
    'Delaware' : 'Dover',
    'Florida' : 'Tallahassee',
    'Georgia' : 'Atlanta',
    'Hawaii' : 'Honolulu',
    'Idaho' : 'Boise',
    'Illinois' : 'Springfield',
    'Indiana' : 'Indianapolis',
    'Iowa' : 'Des Moines',
    'Kansas' : 'Topeka',
    'Kentucky' : 'Frankfort',
    'Louisiana' : 'Baton Rouge',
    'Maine' : 'Augusta',
    'Maryland' : 'Annapolis',
    'Massachusetts' : 'Boston',
    'Michigan' : 'Lansing',
    'Minnesota' : 'Saint Paul',
    'Mississippi' : 'Jackson',
    'Missouri' : 'Jefferson City',
    'Montana' : 'Helena',
    'Nebraska' : 'Lincoln',
    'Nevada' : 'Carson City',
    'New Hampshire' : 'Concord',
    'New Jersey' : 'Trenton',
    'New Mexico' : 'Santa Fe',
    'New York' : 'Albany',
    'North Carolina' : 'Raleigh',
    'North Dakota' : 'Bismarck',
    'Ohio' : 'Columbus',
    'Oklahoma' : 'Oklahoma City',
    'Oregon' : 'Salem',
    'Pennsylvania' : 'Harrisburg',
    'Rhode Island' : 'Providence',
    'South Carolina' : 'Columbia',
    'South Dakota' : 'Pierre',
    'Tennessee' : 'Nashville',
    'Texas' : 'Austin',
    'Utah' : 'Salt Lake City',
    'Vermont' : 'Montpelier',
    'Virginia' : 'Richmond',
    'Washington' : 'Olympia',
    'West Virginia' : 'Charleston',
    'Wisconsin' : 'Madison',
    'Wyoming' : 'Cheyenne',
}



def capital_of_Idaho():
    # Your code here

    print(STATES_CAPITALS['Idaho'])

    pass

def all_states():
    # Your code here
    #print(STATES_CAPITALS.keys())
    state = ''
    for key in STATES_CAPITALS.keys():
        state+= key + ", "
    print(state[:-2])

    pass

def all_capitals():
    # Your code here
    capital = ''
    for value in STATES_CAPITALS.values():
        capital += value + ", "
    print(capital[:-2])
    pass

def states_capitals_string():
    # Your code here
    mysttr = ''
    my_list = []

    print(len(STATES_CAPITALS))
    for key , value in STATES_CAPITALS.items():
        mysttr += key + ' -> ' + value + ', '
        test = key + ' -> ' + value
        my_list.append(test)

    print(mysttr[:-2])

    my_list.sort()
    print(my_list)

    pass

def get_state(capital):
    for key , value in STATES_CAPITALS.items():
        # print(key+' '+value)
        #test = value
        if ( capital == value ):
            print("For State Name " + key + " Capital is "+ value)
    return
    pass

def test_state_to_capital():

    assert 'Cheyenne' == STATES_CAPITALS['Wyoming']
    get_state(input("import Capital to test:"))


def test_state_to_capital_unknown():
    with pytest.raises(KeyError):
        STATES_CAPITALS['']

def test_capital_to_state():
    assert 'Wyoming' == get_state('Cheyenne')

def test_capital_to_state_unknown():
    with pytest.raises(KeyError):
        get_state('')

test_state_to_capital()
capital_of_Idaho ()
all_states()
all_capitals()
states_capitals_string()


'''
def main():
    return pytest.main(__file__)


if __name__ == '__main__':
    sys.exit(main())
'''