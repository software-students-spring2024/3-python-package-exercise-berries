
import pytest
from unittest.mock import patch
from frog import frog_cli

@pytest.mark.parametrize("test_args,expected_call", [
    (['prog', 'frogmode'], 'frogmode'),
    (['prog', 'feed', 'flies'], ('feed', 'flies')),
    (['prog', 'hello', 'Alice'], ('hello', 'Alice')),
])

def test_frog_cli_commands(test_args, expected_call):
    with patch('sys.argv', test_args), patch(f'frog.frog.{expected_call[0] if isinstance(expected_call, tuple) else expected_call}', return_value=None) as mock_func:
        frog_cli.main()
        if isinstance(expected_call, tuple):
            mock_func.assert_called_once_with(*expected_call[1:])
        else:
            mock_func.assert_called_once()

def test_frogmode_no_arguments():
    test_args = ['prog', 'frogmode']
    with patch('sys.argv', test_args), patch('frog.frog.frogmode', return_value=None) as mock_func:
        frog_cli.main()
        mock_func.assert_called_once_with()

def test_hello_with_numbers():
    test_args = ['prog', 'hello', '123']
    with patch('sys.argv', test_args), patch('frog.frog.hello', return_value=None) as mock_func:
        frog_cli.main()
        mock_func.assert_called_once_with('123')

def test_hello_with_special_characters():
    test_args = ['prog', 'hello', '!@#$%']
    with patch('sys.argv', test_args), patch('frog.frog.hello', return_value=None) as mock_func:
        frog_cli.main()
        mock_func.assert_called_once_with('!@#$%')

def test_unrecognized_command():
    test_args = ['prog', 'unknown_command']
    with patch('sys.argv', test_args), patch('sys.exit') as mock_exit:
        frog_cli.main()
        mock_exit.assert_called_once_with(2)
