from moyenne import calculate_average

def test_calculate_average():
    assert calculate_average([1, 2, 3, 4, 5]) == 3
    assert calculate_average([10, 20, 30, 40, 50]) == 30
    assert calculate_average([]) == 0
