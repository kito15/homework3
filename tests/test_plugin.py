"""
Test suite for the plugin module.
"""
from unittest.mock import patch
from io import StringIO
import pytest
from plugins.plugin import SamplePlugin
from main import load_plugins  # Import the load_plugins function

def test_execute_plugin_command():
    """
    Test executing a command from a plugin.
    """
    with patch('sys.stdout', new=StringIO()) as fake_out:
        plugin = SamplePlugin()
        commands = plugin.get_commands()
        cmd = commands[0](3, 2)
        cmd.execute()
        assert fake_out.getvalue() == "The result of 3.0 power 2.0 is equal to 9.0\n"

def test_invalid_plugin():
    """
    Test loading an invalid plugin directory.
    """
    operations = {}  # Initialize the operations dictionary
    with pytest.raises(FileNotFoundError):
        plugin_dir = 'invalid_plugin_dir'
        load_plugins(plugin_dir, operations)  # Pass the operations dictionary
