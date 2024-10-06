"""Calculator Test Suite"""
# pylint: disable=redefined-outer-name
import pytest
from faker import Faker
from calculator.calculator import Calculator
from calculator.calculation import Calculation, Calculations

fake = Faker()

@pytest.fixture
def setup_calculations():
    """Fixture to set up test calculations"""
    Calculations.clear_history()
    calc1 = Calculation(5, 3, Calculator.add)
    calc2 = Calculation(10, 2, Calculator.multiply)
    Calculations.add_to_history(calc1)
    Calculations.add_to_history(calc2)
    return calc1, calc2

@pytest.mark.parametrize("a, b, expected", [
    (2, 2, 4),
    (2.5, 3.5, 6.0),
    (-1, 1, 0),
    (0, 0, 0)
])
def test_addition(a, b, expected):
    """Test that addition method works"""
    assert Calculator.add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (10.5, 5.5, 5.0),
    (-1, 1, -2),
    (0, 0, 0)
])
def test_subtraction(a, b, expected):
    """Test that subtraction method works"""
    assert Calculator.subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (3, 4, 12),
    (2.5, 4, 10.0),
    (-2, 3, -6),
    (0, 5, 0)
])
def test_multiplication(a, b, expected):
    """Test that multiplication method works"""
    assert Calculator.multiply(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5.0),
    (7, 2, 3.5),
    (-6, 3, -2.0),
    (0, 5, 0.0)
])
def test_division(a, b, expected):
    """Test that division method works"""
    assert Calculator.divide(a, b) == expected

def test_division_by_zero():
    """Test that division by zero raises an error"""
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(5, 0)

@pytest.mark.parametrize("a, b, operation, expected", [
    (5, 3, Calculator.add, 8),
    (10, 4, Calculator.subtract, 6),
    (3, 7, Calculator.multiply, 21),
    (15, 3, Calculator.divide, 5.0)
])
def test_calculation(a, b, operation, expected):
    """Test Calculation class operations"""
    calc = Calculation(a, b, operation)
    assert calc.perform_operation() == expected

def test_calculation_methods():
    """Test individual Calculation class methods"""
    calc = Calculation(10, 5, Calculator.add)
    assert calc.add() == 15
    assert calc.subtract() == 5
    assert calc.multiply() == 50
    assert calc.divide() == 2.0

def test_calculation_divide_by_zero():
    """Test Calculation class division by zero"""
    calc = Calculation(5, 0, Calculator.divide)
    with pytest.raises(ZeroDivisionError):
        calc.perform_operation()

def test_calculations_add_to_history(setup_calculations):
    """Test adding calculations to history"""
    # Explicitly use the setup_calculations fixture
    Calculations.clear_history()
    calc1, calc2 = setup_calculations
    Calculations.add_to_history(calc1)
    Calculations.add_to_history(calc2)
    assert len(Calculations.get_history()) == 2
    assert Calculations.get_history()[0] == calc1
    assert Calculations.get_history()[1] == calc2

def test_calculations_get_last_calculation(setup_calculations):
    """Test retrieving the last calculation from history"""
    _, calc2 = setup_calculations
    last_calc = Calculations.get_last_calculation()
    assert last_calc == calc2

def test_calculations_clear_history():
    """Test clearing the calculation history"""
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0

def test_random_calculations(random_calculations):
    """Test random calculations"""
    for calc in random_calculations:
        try:
            result = calc.perform_operation()
            assert isinstance(result, (int, float))
        except ZeroDivisionError:
            # Skip this calculation if it's a division by zero
            continue

def test_calculations_empty_history():
    """Test behavior with empty history"""
    Calculations.clear_history()
    assert Calculations.get_last_calculation() is None
    assert len(Calculations.get_history()) == 0
