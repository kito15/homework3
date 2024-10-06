"""
Test suite for the command pattern module.
"""
from unittest.mock import patch
from io import StringIO
import pytest
from command_pattern import (
    CommandInvoker, AddCommand, SubtractCommand, MultiplyCommand, DivideCommand
)

@pytest.mark.parametrize("command, inputs, expected_output", [
    (AddCommand, [5, 3], "The result of 5.0 add 3.0 is equal to 8.0\n"),
    (SubtractCommand, [10, 2], "The result of 10.0 subtract 2.0 is equal to 8.0\n"),
    (MultiplyCommand, [4, 5], "The result of 4.0 multiply 5.0 is equal to 20.0\n"),
    (DivideCommand, [20, 4], "The result of 20.0 divide 4.0 is equal to 5.0\n"),
])
def test_command(command, inputs, expected_output):
    """
    Test individual commands with various inputs and expected outputs.
    """
    with patch('sys.stdout', new=StringIO()) as fake_out:
        cmd = command(*inputs)
        cmd.execute()
        assert fake_out.getvalue() == expected_output

def test_divide_command_zero_denominator():
    """
    Test the divide command with a zero denominator.
    """
    with patch('sys.stdout', new=StringIO()) as fake_out:
        cmd = DivideCommand(1, 0)
        cmd.execute()
        assert fake_out.getvalue() == "An error occurred: Cannot divide by zero\n"

def test_command_invoker():
    """
    Test the command invoker with multiple commands.
    """
    with patch('sys.stdout', new=StringIO()) as fake_out:
        invoker = CommandInvoker()
        invoker.add_command(AddCommand(5, 3))
        invoker.add_command(SubtractCommand(10, 2))
        invoker.execute_commands()
        assert fake_out.getvalue() == (
            "The result of 5.0 add 3.0 is equal to 8.0\n"
            "The result of 10.0 subtract 2.0 is equal to 8.0\n"
        )
