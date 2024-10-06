"""Test suite for the main module of the calculator application."""
from unittest.mock import patch
from io import StringIO
import pytest
from main import main

@pytest.mark.parametrize("inputs, expected_outputs", [
    (["5", "3", "add", "n"], ["The result of 5.0 add 3.0 is equal to 8.0"]),
    (["10", "2", "subtract", "n"], ["The result of 10.0 subtract 2.0 is equal to 8.0"]),
    (["4", "5", "multiply", "n"], ["The result of 4.0 multiply 5.0 is equal to 20.0"]),
    (["20", "4", "divide", "n"], ["The result of 20.0 divide 4.0 is equal to 5.0"]),
    (["1", "0", "divide", "n"], ["An error occurred: Cannot divide by zero"]),
    (["9", "3", "unknown", "add", "n"], [
        "An error occurred: Unknown operation: unknown",
        "The result of 9.0 add 3.0 is equal to 12.0"
    ]),
    (
        ["a", "3", "5", "3", "add", "n"],
        [
            "Invalid input. Please enter a number.",
            "The result of 3.0 add 5.0 is equal to 8.0"
        ]
    ),
])
def test_main_function(inputs, expected_outputs):
    """Test the main function with various inputs and expected outputs."""
    with patch('builtins.input', side_effect=inputs), \
         patch('sys.stdout', new=StringIO()) as fake_out:
        main()
        output = fake_out.getvalue()
        for expected in expected_outputs:
            assert expected in output
