from exercises.anagram import is_anagram

def test_is_anagram():

    test_cases = [
        ("test", "tset", True),
        ("restful", "fluster", True),
    ]

    for (test_input1, test_input2, expected_result) in test_cases:
        assert is_anagram(test_input1, test_input2) == expected_result