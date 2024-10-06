from unittest.mock import patch
from io import StringIO
import pytest
from plugins.sample_plugin import SamplePlugin

def test_execute_plugin_command():
    with patch('sys.stdout', new=StringIO()) as fake_out:
        plugin = SamplePlugin()
        commands = plugin.get_commands()
        cmd = commands[0](3, 2)
        cmd.execute()
        assert fake_out.getvalue() == "The result of 3.0 power 2.0 is equal to 9.0\n"

def test_invalid_plugin():
    with pytest.raises(FileNotFoundError):
        plugin_dir = 'invalid_plugin_dir'
        load_plugins(plugin_dir)
