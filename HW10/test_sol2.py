import pytest
import sol2

@pytest.mark.parametrize("s, bomb, expected", [
    ("mirkovC4nizCC44", "C4", "mirkovniz"),
    ("12ab112ab2ab", "12ab", "FRULA"),
    ("abcdababcda", "abc", "dabda"),
    ("123456789", "123", "456789"),
    ("aaaaabbbbb", "ab", "FRULA"), # 같은 문자가 두 번 이상 포함된 폭발 문자열
    ("a", "a", "FRULA"),
    ("", "a", "FRULA"),
    ("abcabcabc", "abc", "FRULA"),  # 폭발 문자열이 여러 번 나타나는 경우
    ("abcdefghij", "z", "abcdefghij") # 폭발 문자열이 없는 경우
])
def test_solve(s, bomb, expected):
    assert sol2.solve(s, bomb) == expected
