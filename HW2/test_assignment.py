import pytest
import assignment

@pytest.mark.parametrize("format_str, expected", [
    ("dd", 90),
    ("cc", 650),
    ("dcdd", 23400),
])
def test_solve(format_str, expected):
    assert assignment.solve(format_str) == expected
