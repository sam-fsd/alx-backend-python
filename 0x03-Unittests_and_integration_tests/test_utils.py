#!/usr/bin/env python3
"""Defines a test class"""
from parameterized import parameterized
import utils
from utils import memoize
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
    """
    Test case for the get_json function.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("requests.get")
    def test_get_json(self, test_url: str, test_payload: Dict, mock_get):
        """
        Test the get_json function.

        Args:
            test_url (str): The URL to test.
            test_payload (Dict): The expected payload.
            mock_get: The mock object for the get method.

        Returns:
            None
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response
        result = utils.get_json(test_url)
        self.assertEqual(result, test_payload)
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    Test the memoization decorator, memoize
    """

    def test_memoize(self):
        """
        Test that utils.memoize decorator works as intended
        """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, 'a_method') as mock_object:
            test = TestClass()
            test.a_property()
            test.a_property()
            mock_object.assert_called_once()
