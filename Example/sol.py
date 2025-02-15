import numpy as np

def hello_world() -> str:
    """
    Hello World! 를 리턴해 주세요.
    """
    return("Hello World!")
    raise NotImplementedError()


def add_two(number: int) -> int:
    """
    number에 숫자 2를 더해주세요.
    """
    return number+2
    raise NotImplementedError()


def zero_array(N: int) -> np.ndarray:
    """
    N개의 0으로 채워진 넘파이 배열을 리턴해 주세요. 자료는 더블형이어야 합니다.
    """
    arr = np.zeros(N, dtype=np.double)
    return arr
    raise NotImplementedError()
