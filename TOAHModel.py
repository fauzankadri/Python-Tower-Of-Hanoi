# Copyright 2013, 2014 Gary Baumgartner, Danny Heap, Dustin Wehr
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
TOAHModel:  Model a game of Towers of Anne Hoy
Cheese:   Model a cheese with a given (relative) size
IllegalMoveError: Type of exceptions thrown when an illegal move is attempted
MoveSequence: Record of a sequence of (not necessarily legal) moves. You will
need to return MoveSequence object after solving an instance of the 4-stool
Towers of Anne Hoy game, and we will use that to check the correctness of your
algorithm.
"""


class TOAHModel:
    """Model a game of Towers Of Anne Hoy.

    Model stools holding stacks of cheese, enforcing the constraint
    that a larger cheese may not be placed on a smaller one.

    fill_first_stool - put an existing model in the standard starting config
    move - move cheese from one stool to another
    add - add a cheese to a stool
    top_cheese - top cheese on a non-empty stool
    cheese_location - index of the stool that the given cheese is on
    number_of_cheeses - number of cheeses in this game
    number_of_moves - number of moves so far
    number_of_stools - number of stools in this game
    get_move_seq - MoveSequence object that records the moves used so far

    """
    def __init__(self, number_of_stools):
        '''
        (obj, int) -> None

        Creates a model of TOAH with the number_of_stools given.
        model will be a list, with each stool having its own list.
        '''
        self.stool_is_filled = False
        self.number_of_move = 0
        self.number_of_cheese = 0
        #creating stools
        self.stools = []
        self.num_of_stools = number_of_stools
        for i in range(self.num_of_stools):
            self.stools.append([])
        self._move_seq = MoveSequence([])

    def fill_first_stool(self: 'TOAHModel', number_of_cheese: int):
        """
        (obj, int) -> None

        Put number_of_cheeses cheeses on the first (i.e. 0-th) stool, in order
        of size, with a cheese of size == number_of_cheeses on bottom and
        a cheese of size == 1 on top.

        >>> mod = TOAHModel(3)
        >>> mod.fill_first_stool(4)
        >>> mod.stools
        [[Cheese(4), Cheese(3), Cheese(2), Cheese(1)], [], []]

        """
        if (not self.stool_is_filled):
            self.number_of_cheese = number_of_cheese
            self._cheese_size = []
            #Make the sizes of cheese
            for i in range(1, self.number_of_cheese + 1):
                self._cheese_size.append(i)
            self._cheese_size.reverse()

            #Add the cheeses to first stool
            for size in self._cheese_size:
                self.stools[0].append(Cheese(size))
            self.stool_is_filled = True
        else:
            raise IllegalMoveError

    def move(self: 'TOAHModel', point_1: int, point_2: int):
        '''
        (int, int) -> none

        >>> mod = TOAHModel(3)
        >>> mod.fill_first_stool(3)
        >>> mod.move(0,1)
        >>> mod.stools
        [[Cheese(3), Cheese(2)], [Cheese(1)], []]

        Mutates self.stools so a cheese is taken from point_1 to point_2
        '''
        self._move_seq.add_move(point_1, point_2)
        try:
            if len(self.stools[point_1]) == 0:
                return None
            #get cheese at top
            to_move = self.top_cheese(point_1)
            dest = self.top_cheese(point_2)
            if len(self.stools[point_2]) == 0 or to_move.size < dest.size:
                #remove the cheese from its original location
                self.stools[point_1].remove(to_move)
                #add cheese to the new location
                self.add(point_2, to_move)
                #record the number of moves and history
                self.number_of_move += 1
            else:
                return None
        except:
            pass

    #adds a created cheese to a stool
    def add(self: 'TOAHModel', stool_index: int, cheese: 'Cheese'):
        '''
        (int, obj) -> none

        >>> cheese = Cheese(2)
        >>> mod = TOAHModel(3)
        >>> mod.add(1, cheese)
        >>> mod.stools
        [[], [Cheese(2)], []]

        Adds a created cheese to the stool_index, that too on top
        '''
        self.stools[stool_index].append(cheese)

    def top_cheese(self: 'TOAHModel', index: int):
        '''
        (int) -> None or obj

        >>> mod = TOAHModel(3)
        >>> mod.fill_first_stool(3)
        >>> mod.top_cheese(0)
        Cheese(1)

        >>> mod = TOAHModel(3)
        >>> mod.fill_first_stool(3)
        >>> mod.top_cheese(1)

        Returns the top cheese of the cheese that is at the index of stool
        '''
        #empty stool returning nothing
        if len(self.stools[index]) > 0:
            return self.stools[index][-1]
        #stool with cheese returning top cheese
        else:
            return None

    #get the stool index of the input cheese
    def cheese_location(self: 'TOAHModel', cheese: 'Cheese'):
        '''
        (obj, obj) -> int

        >>> mod = TOAHModel(3)
        >>> mod.fill_first_stool(3)
        >>> cheese = Cheese(3)
        >>> mod.cheese_location(cheese)
        0

        Return the index of the stool that the given cheese is at
        '''
        #checks every stool
        for i in range(self.num_of_stools):
            #checks every Cheese
            for j in range(len(self.stools[i])):
                if cheese == self.stools[i][j]:
                    return i  # returns stool index if cheese is found

    #return the number of cheeses being played in game
    def number_of_cheeses(self: 'TOAHModel'):
        '''
        (obj) -> int

        >>> mod = TOAHModel(3)
        >>> mod.fill_first_stool(3)
        >>> mod.number_of_cheeses()
        3

        Return the number of cheeses being played in TOAHModel
        '''
        return self.number_of_cheese

    def number_of_moves(self: 'TOAHModel'):
        '''
        () -> int

        >>> mod = TOAHModel(3)
        >>> mod.fill_first_stool(3)
        >>> mod.move(0,1)
        >>> mod.number_of_moves()
        1

        Returns the number_of_moves done in the game
        '''
        return self.number_of_move

    def number_of_stools(self: 'TOAHModel'):
        '''
        (obj) -> int

        >>> mod = TOAHModel(3)
        >>> mod.number_of_stools()
        3

        Returns num_of_stools, the number of stools being used in game
        '''
        return self.num_of_stools

    def _cheese_at(self: 'TOAHModel', stool_index,
                   stool_height: int) -> 'Cheese':
        """
        If there are at least stool_height+1 cheeses
        on stool stool_index then return the (stool_height)-th one.
        Otherwise return None.

        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(5)
        >>> M._cheese_at(0,3).size
        2
        >>> M._cheese_at(0,0).size
        5
        """
        try:
            return self.stools[stool_index][stool_height]
        except:
            return None

    def get_move_seq(self: 'TOAHModel') -> 'MoveSequence':
        '''
        () -> list of set

        >>> mod = TOAHModel(3)
        >>> mod.fill_first_stool(3)
        >>> mod.move(0, 1)
        >>> mod.get_move_seq()
        MoveSequence([(0, 1)])

        Returns a list of sets of the move sequences done
        '''
        print(self._move_seq)

    def __eq__(self: 'TOAHModel', other: 'TOAHModel') -> bool:
        """
        We're saying two TOAHModels are equivalent if their current
        configurations of cheeses on stools look the same.
        More precisely, for all h,s, the h-th cheese on the s-th
        stool of self should be equivalent the h-th cheese on the s-th
        stool of other

        >>> m1 = TOAHModel(4)
        >>> m1.fill_first_stool(7)
        >>> m1.move(0,1)
        >>> m1.move(0,2)
        >>> m1.move(1,2)
        >>> m2 = TOAHModel(4)
        >>> m2.fill_first_stool(7)
        >>> m2.move(0,3)
        >>> m2.move(0,2)
        >>> m2.move(3,2)
        >>> m1 == m2
        True
        """
        return self.stools == other.stools

    def __str__(self: 'TOAHModel') -> str:
        """
        Depicts only the current state of the stools and cheese.
        """
        stool_str = "=" * (2 * (self.number_of_cheeses()) + 1)
        stool_spacing = "  "
        stools_str = (stool_str + stool_spacing) * self.number_of_stools()

        def cheese_str(size: int):
            if size == 0:
                return " " * len(stool_str)
            cheese_part = "-" + "--" * (size - 1)
            space_filler = " " * int((len(stool_str) - len(cheese_part)) / 2)
            return space_filler + cheese_part + space_filler

        lines = ""
        for height in range(self.number_of_cheeses() - 1, -1, -1):
            line = ""
            for stool in range(self.number_of_stools()):
                c = self._cheese_at(stool, height)
                if isinstance(c, Cheese):
                    s = cheese_str(int(c.size))
                else:
                    s = cheese_str(0)
                line += s + stool_spacing
            lines += line + "\n"
        lines += stools_str

        return lines


class Cheese:
    def __init__(self: 'Cheese', size: int):
        """
        Initialize a Cheese to diameter size.

        >>> c = Cheese(3)
        >>> isinstance(c, Cheese)
        True
        >>> c.size
        3
        """
        self.size = size

    def __repr__(self: 'Cheese') -> str:
        """
        Representation of this Cheese
        """
        return "Cheese(" + str(self.size) + ")"

    def __eq__(self: 'Cheese', other: 'Cheese') -> bool:
        """Is self equivalent to other? We say they are if they're the same
        size."""
        return isinstance(other, Cheese) and self.size == other.size


class IllegalMoveError(Exception):
    pass


class MoveSequence:
    def __init__(self: 'MoveSequence', moves: list):
        # moves - a list of integer pairs, e.g. [(0,1),(0,2),(1,2)]
        self._moves = moves

    def get_move(self: 'MoveSequence', i: int):
        # Exception if not (0 <= i < self.length)
        return self._moves[i]

    def add_move(self: 'MoveSequence', src_stool: int, dest_stool: int):
        self._moves.append((src_stool, dest_stool))

    def length(self: 'MoveSequence') -> int:
        return len(self._moves)

    def generate_TOAHModel(self: 'MoveSequence', number_of_stools: int,
                           number_of_cheeses: int) -> 'TOAHModel':
        """
        An alternate constructor for a TOAHModel. Takes the two parameters for
        the game (number_of_cheeses, number_of_stools), initializes the game
        in the standard way with TOAHModel.fill_first_stool(number_of_cheeses),
        and then applies each of the moves in this move sequence.
        """
        model = TOAHModel(number_of_stools)
        model.fill_first_stool(number_of_cheeses)
        for move in self._moves:
            model.move(move[0], move[1])
        return model

    def __repr__(self: 'MoveSequence') -> str:
        return "MoveSequence(" + repr(self._moves) + ")"


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)