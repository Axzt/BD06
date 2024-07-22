from main import *


run_cases = [
    (
        "00FFFF",
        (0, 255, 255),
    ),
    (
        "FFFF00",
        (255, 255, 0),
    ),
    (
        "Hello!",
        "not a hex color",
    ),
    (
        "42",
        "not a hex color",
    ),
]

submit_cases = run_cases + [
    (
        "",
        "not a hex color",
    ),
    (
        100_000,
        "not a hex color",
    ),
    (
        "FF00FF",
        (255, 0, 255),
    ),
    (
        "000000",
        (0, 0, 0),
    ),
    (
        "FFFFFF",
        (255, 255, 255),
    ),
]


def test(input, expected_output):
    print("---------------------------------")
    print(f"  Inputs: '{input}'")
    print(f"Expected: {expected_output}")
    try:
        result = hex_to_rgb(input)
    except Exception as e:
        result = str(e)
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
