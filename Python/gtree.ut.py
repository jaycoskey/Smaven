#!/usr/bin/env python

import unittest
import yaml


from board import Board
from gtree import GTree


class TestGTree(unittest.TestCase):
    def test_word_1x1(self):
        gtree = GTree()
        # print(gtree)
        assert(not gtree.has_word('a'))

    def test_word_1x3(self):
        gtree = GTree()
        gtree.add_word('bet')
        # print(gtree)
        assert(gtree.has_word('bet'))

    def test_word_4x3(self):
        gtree = GTree()
        words = ['net', 'not', 'pet', 'pot']
        gtree.add_wordlist(words)
        # print(gtree)
        for word in words:
            assert(gtree.has_word(word))


class TestGTree_FindMoves(unittest.TestCase):
    def test_board_edge(self):
        run_config_test('test_board_edge')

    def test_empty_board(self):
        run_config_test('test_empty_board')

    def test_fill_gap(self):
        run_config_test('test_fill_gap')

    def test_fill_gap_with_blank(self):
        run_config_test('test_fill_gap_with_blank')

    def test_fill_noncontiguous_gaps(self):
        run_config_test('test_fill_noncontiguous_gaps')

    def test_parallel_word(self):
        run_config_test('test_parallel_word')

    def test_secondary_words(self):
        run_config_test('test_secondary_words')


def run_config_test(test_name):
    with open('test_config.yml', 'r') as stream:
        config = yaml.load(stream)

    config_test = config[test_name]
    config_board = config_test['board']
    config_dictionary = config_test['dictionary']
    config_rack = config_test['rack']

    board = Board(layout=None, rows=config_board)
    gtree = GTree()
    gtree.add_wordlist(config_dictionary)
    moves_found = gtree.find_moves(board, config_rack)

    words_found = []
    for move in moves_found:
        words_found.append(move.primary_word)
        words_found.extend(move.secondary_words)
    num_words_found = len(words_found)

    config_words_found = config_test['words_found']
    assert(all([ word in config_words_found
                    for word in words_found
                    ]))

    if 'words_not_found' in config_test:
        config_words_not_found = config_test['words_not_found']
        assert(all([word not in config_words_not_found
                    for word in words_found]))


def show_config():
    with open('test_config.yml', 'r') as stream:
        config = yaml.load(stream)

    for k in config:
        print(f'Test name: {k}')
        for test_prop in config[k]:
            if test_prop == 'board':
                print(f'\t{test_prop}: ...')
            else:
                print(f'\t{test_prop}: {config[k][test_prop]}')

if __name__ == '__main__':
    # show_config()
    runner = unittest.main()

