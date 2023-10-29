from exercises.reverse import reverse

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