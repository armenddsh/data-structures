from exercises.palindrome import is_palindrome

def test_is_palindrome():

    # generate test cases

    test_cases = [
        ("", False),
        ("a", False),
        ("aa", True),
        ("aba", True),
        ("abba", True),
        ("abca", False),
        ("abcba", True),
        ("abcdcba", True),
        ("abcd", False),
        ("abcddcba", True)
    ]

    # run test cases

    for (test_input, expected_result) in test_cases:
        assert is_palindrome(test_input) == expected_result