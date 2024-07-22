from main import *


run_cases = [
    (
        [1, 2, 3, 4, 5],
        [4, 5, 6, 7, 8],
        True,
        [8, 7, 6, 5, 4, 3, 2, 1],
    ),
    (
        ["tent", "sleeping bag", "camp stove", "lantern", "backpack"],
        ["flashlight", "tent", "camp chair", "sleeping bag", "water bottle"],
        False,
        [
            "backpack",
            "camp chair",
            "camp stove",
            "flashlight",
            "lantern",
            "sleeping bag",
            "tent",
            "water bottle",
        ],
    ),
    (
        ["milk", "bread", "eggs", "cheese", "apples"],
        ["milk", "bananas", "bread", "oranges", "cheese"],
        True,
        ["oranges", "milk", "eggs", "cheese", "bread", "bananas", "apples"],
    ),
    (
        ["soccer ball", "tennis racket", "basketball", "baseball glove"],
        ["baseball bat", "soccer ball", "tennis balls", "basketball", "helmet"],
        False,
        [
            "baseball bat",
            "baseball glove",
            "basketball",
            "helmet",
            "soccer ball",
            "tennis balls",
            "tennis racket",
        ],
    ),
]


submit_cases = run_cases + [
    (
        ["notebooks", "pencils", "backpack", "textbooks", "laptop"],
        ["highlighters", "notebooks", "erasers", "backpack", "calculator"],
        False,
        [
            "backpack",
            "calculator",
            "erasers",
            "highlighters",
            "laptop",
            "notebooks",
            "pencils",
            "textbooks",
        ],
    ),
    (
        ["tent", "milk", "soccer ball", "notebooks"],
        ["bread", "tent", "swim goggles", "pencils", "milk"],
        True,
        [
            "tent",
            "swim goggles",
            "soccer ball",
            "pencils",
            "notebooks",
            "milk",
            "bread",
        ],
    ),
]


def test(input1, input2, input3, expected_output):
    print("---------------------------------")
    print(f"List 1: {input1}")
    print(f"List 2: {input2}")
    if input3:
        print(f"Reversed")
    print(f"Expected: {expected_output}")
    result = deduplicate_lists(input1, input2, input3)
    print(f"  Actual: {result}")
    if result != expected_output:
        print("Fail")
        return False
    print("Pass")
    return True


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
