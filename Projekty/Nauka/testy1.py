def is_adult(age: int) -> bool:
    return age >= 18

def test_is_adult():
    age = 18
    result = is_adult(age)
    assert result
    assert is_adult(55)


def test_is_not_adult():
    assert not is_adult(17)
    assert not is_adult(10)

