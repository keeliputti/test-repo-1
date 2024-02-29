import os
import unittest
from unittest.mock import patch, MagicMock

import json  # Assuming json is imported in your original code

def read_description_file(source: str):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    descriptions = os.path.join(current_dir, '../catalog/descriptions.json')
    with open(descriptions, "r") as f:
        return json.load(f)


class TestReadDescriptionFile(unittest.TestCase):

    @patch('os.path.dirname')
    def test_correct_path(self, mock_dirname):
        """Tests if the correct path is constructed for the descriptions file."""
        mock_dirname.return_value = '/path/to/current/directory'
        expected_path = '/path/to/current/directory/../catalog/descriptions.json'

        read_description_file('test_source')

        mock_dirname.assert_called_once_with(__file__)

    @patch('os.path.join')
    def test_path_joining(self, mock_join):
        """Tests if the path components are joined correctly."""
        mock_join.return_value = '/joined/path/descriptions.json'
        expected_path = '/joined/path/descriptions.json'

        read_description_file('test_source')

        mock_join.assert_called_once_with('/path/to/current/directory', '../catalog/descriptions.json')

    @patch('builtins.open')
    def test_file_opening(self, mock_open):
        """Tests if the descriptions file is opened in read mode."""
        mock_file = MagicMock()
        mock_open.return_value = mock_file

        read_description_file('test_source')

        mock_open.assert_called_once_with('/joined/path/descriptions.json', 'r')
        mock_file.__enter__.assert_called_once()
        mock_file.close.assert_called_once()

    @patch('json.load')
    def test_json_loading(self, mock_load):
        """Tests if the JSON data is loaded from the file."""
        mock_data = {'key1': 'value1'}
        mock_load.return_value = mock_data

        read_description_file('test_source')

        mock_load.assert_called_once_with(mock_file)

    @patch('read_description_file')
    def test_provider_descriptions(self, mock_read):
        """Tests if `provider_descriptions` calls the function with 'provider' source."""
        mock_data = {'provider_key': 'provider_value'}
        mock_read.return_value = mock_data

        provider_descriptions = read_description_file('provider')

        mock_read.assert_called_once_with('provider')
        self.assertEqual(provider_descriptions, mock_data)

    @patch('read_description_file')
    def test_package_descriptions(self, mock_read):
        """Tests if `package_descriptions` calls the function with 'package' source."""
        mock_data = {'package_key': 'package_value'}
        mock_read.return_value = mock_data

        package_descriptions = read_description_file('package')

        mock_read.assert_called_once_with('package')
        self.assertEqual(package_descriptions, mock_data)

    def test_missing_file(self):
        """Tests if an error is raised when the descriptions file is missing."""
        with self.assertRaises(FileNotFoundError):
            read_description_file('nonexistent_source')


if __name__ == '__main__':
    unittest.main()
