import pytest
from main import load_plugins
from plugins.sample_plugin import SamplePlugin
from command_pattern import CommandInvoker, CommandHistory
from io import StringIO
import sys

def test_load_plugins():
    plugins = load_plugins('plugins')
    assert len(plugins) == 1
    assert isinstance(plugins[0], SamplePlugin)

def test_execute_plugin_command(capsys):
    plugins = load_plugins('plugins')
    plugin = plugins[0]
    command = plugin.get_commands()[0](3, 2)
    command.execute()
    captured = capsys.readouterr()
    assert "The result of 3.0 power 2.0 is equal to 9.0" in captured.out

def test_invalid_plugin():
    with pytest.raises(ImportError):
        load_plugins('invalid_plugin_dir')
