import pytest
from command_pattern import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand, CommandInvoker, CommandHistory
from calculator.calculator import Calculator
from io import StringIO
import sys

def test_add_command(capsys):
    command = AddCommand(5, 3)
    command.execute()
    captured = capsys.readouterr()
    assert "The result of 5.0 add 3.0 is equal to 8.0" in captured.out

def test_subtract_command(capsys):
    command = SubtractCommand(10, 2)
    command.execute()
    captured = capsys.readouterr()
    assert "The result of 10.0 subtract 2.0 is equal to 8.0" in captured.out

def test_multiply_command(capsys):
    command = MultiplyCommand(4, 5)
    command.execute()
    captured = capsys.readouterr()
    assert "The result of 4.0 multiply 5.0 is equal to 20.0" in captured.out

def test_divide_command(capsys):
    command = DivideCommand(20, 4)
    command.execute()
    captured = capsys.readouterr()
    assert "The result of 20.0 divide 4.0 is equal to 5.0" in captured.out

def test_command_invoker(capsys):
    invoker = CommandInvoker()
    invoker.add_command(AddCommand(5, 3))
    invoker.add_command(SubtractCommand(10, 2))
    invoker.execute_commands()
    captured = capsys.readouterr()
    assert "The result of 5.0 add 3.0 is equal to 8.0" in captured.out
    assert "The result of 10.0 subtract 2.0 is equal to 8.0" in captured.out

def test_command_history():
    history = CommandHistory()
    command1 = AddCommand(5, 3)
    command2 = SubtractCommand(10, 2)
    history.add_command(command1)
    history.add_command(command2)
    assert len(history.get_history()) == 2
    assert history.get_history()[0] == command1
    assert history.get_history()[1] == command2
    history.clear_history()
    assert len(history.get_history()) == 0

def test_divide_command_zero_denominator(capsys):
    command = DivideCommand(5, 0)
    with pytest.raises(ZeroDivisionError):
        command.execute()
    captured = capsys.readouterr()
    assert "An error occurred: Cannot divide by zero" in captured.out
