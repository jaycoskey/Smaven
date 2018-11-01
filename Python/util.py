#!/usr/bin/env python

from collections import namedtuple


Square = namedtuple('Square', ['x', 'y'])


class Util:
    @staticmethod
    def do_rows_form_square(rows):
        row_count = len(rows)
        are_rows_same_length = all(map(lambda row: len(row) == row_count, rows))
        if not are_rows_same_length:
            return False
        is_board_square = row_count = len(rows[0])
        return is_board_square

    @staticmethod
    def reversed_dict(d):
        return { d[k]: k for k in d }