#!/usr/bin/env python3
"""Defines a test class"""
from parameterized import parameterized
import utils
import unittest
from typing import Mapping, Sequence, Any


class TestAccessNestedMap(unittest.TestCase):
    """Test utils methods"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: Any) -> None:
        """Test accesss_nested_map function"""
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)
