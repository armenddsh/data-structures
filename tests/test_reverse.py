from exercises.reverse import reverse, reverse_integer

def test_reverse():

    test_cases = [
        ([1,2,3,4,5,6], [6,5,4,3,2,1]),
        ([1,2,3,4,5], [5,4,3,2,1]),
        ([1,2,3,4], [4,3,2,1]),
        ([1,2,3], [3,2,1]),
        ([1,2], [2,1]),
        ([1], [1]),
        ([], []),
        ([-1,-2,-3,-4,-5,-6], [-6,-5,-4,-3,-2,-1]),
        ([-1,-2,-3,-4,-5], [-5,-4,-3,-2,-1]),
        ([-1,-2,-3,-4], [-4,-3,-2,-1]),
        ([-1,-2,-3], [-3,-2,-1]),
        ([-1,-2], [-2,-1]),
        ([-1], [-1]),
        ([5,-3,6,2,1,100,-500,20,3,4,5,6], [6,5,4,3,20,-500,100,1,2,6,-3,5])
    ]

    for (test_input, expected_result) in test_cases:
        assert all([a == b for a, b in zip(reverse(test_input), expected_result)])

def test_reverse_integer():

    test_cases = [
        (12345, 54321),
        (1234, 4321),
        (123, 321),
        (12, 21),
        (1, 1),
        (0, 0),
        (-12345, -54321),
        (-1234, -4321),
        (-123, -321),
        (-12, -21),
        (-1, -1)
    ]

    for (test_input, expected_result) in test_cases:
        assert reverse_integer(test_input) == expected_result   