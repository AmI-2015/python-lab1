'''
Created on Mar 16, 2015

Copyright (c) 2015 Luigi De Russis
 
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0
 
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License

@author: derussis
'''

from sys import argv

def find_players(people, instrument):
    players = {} # init a new, empty dictionary
    
    # look for the given instrument
    for person in people.keys():
        if people[person]['instrument'] == instrument:
            players[person] = people[person]
    
    # print the result
    print players


if __name__ == '__main__':
    if len(argv) == 2:
        instrument = argv[1] # take the instrument name from command line
    else:
        # wrong number of arguments: quit!
        print 'Error: please, insert an instrument name when calling the program.'
        exit()
    
    # dictionaries of people
    sam = {'age': 10, 'height': 42, 'weight': 175, 'instrument': 'fiddle' }
    mary = {'age': 41, 'height': 70, 'weight': 160, 'instrument': 'piano' }
    bertha = {'age': 32, 'height': 97, 'weight': 587, 'instrument': 'cello'}
    david = {'age':100, 'height': 4, 'weight': 0.5, 'instrument': 'cello'}
    people = {'Sam': sam, 'Mary': mary, 'Bertha': bertha, 'David': david}
    
    find_players(people, instrument)