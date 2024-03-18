
import pytest
from unittest.mock import patch
from frog import frog_cli

@pytest.mark.parametrize("test_args,expected_call", [
    (['prog', 'frogmode'], 'frogmode'),
    (['prog', 'feed', 'flies'], ('feed', 'flies')),
   
])
def test_frog_cli_commands(test_args, expected_call):
    with patch('sys.argv', test_args), patch(f'frog.frog.{expected_call[0] if isinstance(expected_call, tuple) else expected_call}', return_value=None) as mock_func:
        frog_cli.main()
        if isinstance(expected_call, tuple):
            mock_func.assert_called_once_with(*expected_call[1:])
        else:
            mock_func.assert_called_once()
