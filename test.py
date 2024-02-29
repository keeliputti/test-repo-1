import unittest
from unittest.mock import patch, MagicMock

from test import read_description_file  # Assuming the function is in a separate file

class TestReadDescriptionFile(unittest.TestCase):

    @patch('read_description_file.os.path.dirname')
    @patch('read_description_file.os.path.join')
    @patch('read_description_file.builtins.open')
    @patch('read_description_file.json.load')
    def test_read_description_file(self, mock_json_load, mock_open, mock_join, mock_dirname):
        """Tests the read_description_file function with mocking."""

        # Mock return values
        mock_dirname.return_value = '/path/to/current/directory'
        mock_join.return_value = '/path/to/descriptions.json'
        mock_file = MagicMock()
        mock_open.return_value = mock_file
        mock_file.__enter__.return_value = mock_file  # Simulate file object
        mock_data = {'key': 'value'}
        mock_json_load.return_value = mock_data

        # Call the function
        source = 'test_source'
        descriptions = read_description_file(source)

        # Assertions
        mock_dirname.assert_called_once_with(__file__)
        mock_join.assert_called_once_with('/path/to/current/directory', '../catalog/descriptions.json')
        mock_open.assert_called_once_with('/path/to/descriptions.json', 'r')
        mock_file.__enter__.assert_called_once()
        mock_file.close.assert_called_once()
        mock_json_load.assert_called_once_with(mock_file)
        self.assertEqual(descriptions, mock_data)

if __name__ == '__main__':
    unittest.main()
