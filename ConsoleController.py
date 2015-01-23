# Copyright 2014 Dustin Wehr
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 1, CSC148, Winter 2014.
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
"""
ConsoleController: User interface for manually solving Anne Hoy's problems
from the console.

move: Apply one move to the given model, and print any error message
to the console.
"""

from TOAHModel import TOAHModel, Cheese, IllegalMoveError


def move(model: TOAHModel, origin: int, dest: int):
    '''
    Module method to apply one move to the given model, and print any
    error message to the console.

    model - the TOAHModel that you want to modify
    origin - the stool number (indexing from 0!) of the cheese you want
             to move
    dest - the stool number that you want to move the top cheese
            on stool origin onto.
    '''
    try:
        #get the cheeses and move them if they are valid
        _from = model.top_cheese(origin)
        _to = model.top_cheese(dest)
        if _to is None:
            model.move(origin, dest)
        elif _from.size > _to.size:
            print('Illegal Move')
        else:
            model.move(origin, dest)
    except:
        print('Invalid Stool')
        print()
    #prints model after the moves are done
    print(model)


class ConsoleController:

    def __init__(self: 'ConsoleController',
                 number_of_cheeses: int, number_of_stools: int):
        """
        Initialize a new 'ConsoleController'.

        number_of_cheeses - number of cheese to tower on the first stool
        number_of_stools - number of stools
        """
        #get cheeses and stools
        self.number_of_cheeses = number_of_cheeses
        self.num_of_stools = number_of_stools

        #create a model using cheeses and stools
        self.model = TOAHModel(number_of_stools)
        self.model.fill_first_stool(number_of_cheeses)

    def play_loop(self: 'ConsoleController'):
        '''
        Console-based game.
        TODO:
        -Start by giving instructions about how to enter moves (which is up to
        you). Be sure to provide some way of exiting the game, and indicate
        that in the instructions.
        -Use python's built-in function input() to read a potential move from
        the user/player. You should print an error message if the input does
        not meet the specifications given in your instruction or if it denotes
        an invalid move (e.g. moving a cheese onto a smaller cheese).
        You can print error messages from this method and/or from
        ConsoleController.move; it's up to you.
        -After each valid move, use the method TOAHModel.__str__ that we've
        provided to print a representation of the current state of the game.
        '''

        exit = False
        while not exit:
            #commands for user
            print('List of commands:')
            print('move - moves cheese')
            print('exit - exits the game')
            print()

            #get input
            user_input = input()
            user_input = user_input.upper()
            user_input = user_input.strip()

            #do the commands given from user
            if user_input == 'MOVE':
                origin = input('from stool: ')
                dest = input('new stool: ')
                try:
                    origin = origin.strip()
                    dest = dest.strip()

                    origin = int(origin)
                    dest = int(dest)
                except:
                    print('Those are not numbers')
                    print()
                if type(origin) == int and type(dest) == int:
                    move(self.model, origin, dest)
            elif user_input == 'EXIT':
                exit = True
            else:
                print('Unknown Command, please try again')
                print()


if __name__ == '__main__':
    # TODO:
    # You should initiate game play here. Your game should be playable by
    # running this file.
    con = ConsoleController(8, 4)
    con.play_loop()