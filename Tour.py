# Copyright 2013, 2014 Gary Baumgartner, Danny Heap, Dustin Wehr
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 1, CSC148, Fall 2013.
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
from TOAHModel import TOAHModel

import time


def tour_of_four_stools(model: TOAHModel, delay_btw_moves: float=0.5,
                        console_animate: bool=False):
    """Move a tower of cheeses from the first stool in model to the fourth.

       model - a TOAHModel with a tower of cheese on the first stool
                and three other empty stools
       console_animate - whether to animate the tour in the console
       delay_btw_moves - time delay between moves in seconds IF
                         console_animate == True
                         no effect if console_animate == False
    """
    cheeses = model.number_of_cheeses()
    #a reasonable formula to get i, however, not always true
    #eg. for 8 cheeses, it will give 4, however it should be 3
    i = round((2*cheeses)**(1/2))

    #follows the algorithm given in handout
    #move cheeses-i from source to stool 1 using all 4 stools
    min_move_rec(model, cheeses-i, 0, 1, 2, 3,
                 console_animate, delay_btw_moves)
    #do the 3 stool recursion to the last stool
    move_3_stools(model, i, 0, 3, 2, console_animate, delay_btw_moves)
    #move cheeses-i from stool 1 to last stool
    min_move_rec(model, cheeses-i, 1, 3, 0, 2,
                 console_animate, delay_btw_moves)


#4 stool rec
def min_move_rec(model: TOAHModel, cheeses, source, dest, inter1, inter2,
                 console_animate, delay_btw):
        '''
        (obj, int, int, int, int, int) -> none

        moves the cheeses from source to dest using all 4 stools. this should
        be done in minimum moves
        '''

        #first base case where cheeses-i is 0
        if cheeses == 0:
            pass
        elif cheeses == 1:
            model.move(source, dest)
            if (console_animate):
                print(model)
                time.sleep(delay_btw)
        elif cheeses == 2:
            model.move(source, inter1)
            if (console_animate):
                print(model)
                time.sleep(delay_btw)
            model.move(source, dest)
            if (console_animate):
                print(model)
                time.sleep(delay_btw)
            model.move(inter1, dest)
            if (console_animate):
                print(model)
                time.sleep(delay_btw)
        #move cheeses-2 to inter2 using all 4 stools
        else:
            min_move_rec(model, cheeses - 2, source, inter2, inter1, dest,
                         console_animate, delay_btw)
            #extra movements to let this happen
            model.move(source, inter1)
            if (console_animate):
                print(model)
                time.sleep(delay_btw)
            model.move(source, dest)
            if (console_animate):
                print(model)
                time.sleep(delay_btw)
            model.move(inter1, dest)
            if (console_animate):
                print(model)
                time.sleep(delay_btw)
            #extra movements to let this happen
            min_move_rec(model, cheeses - 2,  inter2, dest, source, inter1,
                         console_animate, delay_btw)


#3 stool rec
def move_3_stools(model: TOAHModel, cheeses, source, dest, inter,
                  console_animate, delay_btw):
        '''
        (obj, int, int, int, int) -> none

        moves cheeses from source to dest, using inter as a helper stool.
        this should be done using 3 stools and should be the minimum moves.
        '''
        if cheeses == 1:
            model.move(source, dest)
            if (console_animate):
                print(model)
                time.sleep(delay_btw)
        else:
            #move cheese-1 to inter
            move_3_stools(model, cheeses - 1, source, inter, dest,
                          console_animate, delay_btw)
            model.move(source, dest)
            if (console_animate):
                print(model)
                time.sleep(delay_btw)
            #move cheese -1 from inter to dest
            move_3_stools(model, cheeses - 1, inter, dest, source,
                          console_animate, delay_btw)

if __name__ == '__main__':
    NUM_CHEESES = 8
    DELAY_BETWEEN_MOVES = .5
    CONSOLE_ANIMATE = False

    # DO NOT MODIFY THE CODE BELOW.
    four_stools = TOAHModel(4)
    four_stools.fill_first_stool(number_of_cheese=NUM_CHEESES)

    tour_of_four_stools(four_stools,
                        console_animate=CONSOLE_ANIMATE,
                        delay_btw_moves=DELAY_BETWEEN_MOVES)

    print(four_stools.number_of_moves())