# -*- coding: utf-8 -*-
"""Unit tests for pynlpir.nlpir."""
from __future__ import unicode_literals
import ctypes
import unittest

from pynlpir import nlpir


class TestNLPIR(unittest.TestCase):
    """Unit tests for the pynlpir.nlpir module."""

    def test_load_library(self):
        """Tests that the load_library() function works as expected."""
        self.assertTrue(isinstance(nlpir.libNLPIR, ctypes.CDLL))

    def test_segment(self):
        """Tests that the segment() function works as expected."""
        s = '我们都是美国人。'
        seg_s = nlpir.segment(s, False)
        pos_seg_s = nlpir.segment(s, True)
        expected_seg_s = ['我们', '都', '是', '美国', '人', '。']
        expected_pos_seg_s = [('我们', 'rr'), ('都', 'd'), ('是', 'vshi'),
                              ('美国', 'nsf'), ('人', 'n'), ('。', 'wj')]
        self.assertEqual(expected_seg_s, seg_s)
        self.assertEqual(expected_pos_seg_s, pos_seg_s)

    def test_get_key_words(self):
        """Tests that the get_key_words() function works as expected."""
        s = '我们都是美国人。'
        key_words = nlpir.get_key_words(s)
        weighted_key_words = nlpir.get_key_words(weighted=True)
        expected_key_words = ['美国']
        expected_weighted_key_words = [('美国', 0.01)]
        self.assertEqual(expected_key_words, key_words)
        self.assertEqual(expected_weighted_key_words, weighted_key_words)
