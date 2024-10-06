"""Pytest configuration and fixtures for calculator tests."""
import pytest
from faker import Faker
from calculator import Calculator, Calculation

fake = Faker()

def generate_calculation():
    """Generate a random calculation."""
    a = fake.random_number(digits=2)
    b = fake.random_number(digits=2)
    operation = fake.random_element(elements=(
        Calculator.add, Calculator.subtract, Calculator.multiply, Calculator.divide
    ))
    return Calculation(a, b, operation)

def pytest_addoption(parser):
    """Add command line option for number of records to generate."""
    parser.addoption("--num_records", action="store", default=10, type=int,
                     help="Number of records to generate")

@pytest.fixture
def num_records(request):
    """Fixture to get the number of records from command line option."""
    return request.config.getoption("--num_records")

@pytest.fixture
def random_calculations(num_records):  # pylint: disable=redefined-outer-name
    """Fixture to generate random calculations."""
    return [generate_calculation() for _ in range(num_records)]
