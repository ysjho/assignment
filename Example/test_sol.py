import pytest
import numpy as np
import sol

def test_hello():
    assert sol.hello_world() == "Hello World!"


@pytest.mark.parametrize("input, expected", [(1, 3), (10, 12), (-4, -2)])
def test_add_two(input, expected):
    assert sol.add_two(input) == expected


def test_zero_array():
    return np.testing.assert_allclose(sol.zero_array(100), np.zeros(shape=(100,)))
