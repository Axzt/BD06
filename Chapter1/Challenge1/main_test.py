from main import *

run_cases = [
    (
        "live long and prosper",
        "Live Long And Prosper",
    ),
    (
        "...Khan",
        "...KHAN!!!",
    ),
    ("BEAM ME UP, BOOTS!", "Beam me up, boots"),
]

submit_cases = run_cases + [
    (
        "",
        "",
    ),
    (
        "I aM a DoCtOr, nOt A fUnCtIoNaL pRoGrAmMeR!!",
        "I aM a DoCtOr, nOt A fUnCtIoNaL pRoGrAmMeR!!",
    ),
    (
        "TO BOLDLY GO WHERE NO BEAR HAS GONE BEFORE!!!!",
        "To boldly go where no bear has gone before",
    ),
    (
        "Illogical",
        "ILLOGICAL!!!",
    ),
]


def test(input, expected_output):
    print("---------------------------------")
    print(f"   Input: {input}")
    print(f"Expected: {expected_output}")
    result = toggle_case(input)
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
