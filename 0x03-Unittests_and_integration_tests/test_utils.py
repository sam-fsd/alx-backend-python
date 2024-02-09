#!/usr/bin/env python3
"""Defines a test class"""
from parameterized import parameterized
import utils
import unittest
from unittest.mock import patch, Mock
from typing import Mapping, Sequence, Any, Dict


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

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> None:
        """
        Test case to verify that accessing a nested map with an invalid
        path raises a KeyError.

        Args:
            nested_map (Mapping): The nested map to access.
            path (Sequence): The path to the desired value in the nested map.

        Raises:
            AssertionError: If accessing the nested map with the given
            path does not raise a KeyError.
        """
        with self.assertRaises(KeyError):
            utils.access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("requests.get")
    def test_get_json(self, test_url: str, test_payload: Dict, mock_get):
        mock_get.return_value.json.return_value = test_payload
        result = utils.get_json(test_url)
        self.assertEqual(result, test_payload)
        mock_get.assert_called_once_with(test_url)
