from main import *


def to_string(file):
    return (
        f"File: {file['filename']}\n"
        f"Author: {file['author_first_name']} {file['author_last_name']}\n"
        f"Content: {file['content']}"
    )


run_cases = [
    (
        {
            "filename": "essay.txt",
            "content": "Dear Mr. Vernon, we accept the fact that we had to sacrifice a whole Saturday in detention for whatever it was we did wrong...",
            "author_first_name": "Brian",
            "author_last_name": "Johnson",
        },
        "```\nFile: essay.txt\nAuthor: Brian Johnson\nContent: Dear Mr. Vernon, we accept the fact that we had to sacrifice a whole Saturday in detention for whatever it was we did wrong...\n```",
    ),
    (
        {
            "filename": "letter.txt",
            "content": "But we think you're crazy to make us write an essay telling you who we think we are.",
            "author_first_name": "Brian",
            "author_last_name": "Johnson",
        },
        "```\nFile: letter.txt\nAuthor: Brian Johnson\nContent: But we think you're crazy to make us write an essay telling you who we think we are.\n```",
    ),
]

submit_cases = run_cases + [
    (
        {
            "filename": "note.txt",
            "content": "Does Barry Manilow know that you raid his wardrobe?",
            "author_first_name": "John",
            "author_last_name": "Bender",
        },
        "```\nFile: note.txt\nAuthor: John Bender\nContent: Does Barry Manilow know that you raid his wardrobe?\n```",
    ),
]


def test(input1, expected_output):
    print("---------------------------------")
    print("Inputs:")
    print(f"  filename: {input1['filename']}")
    print(f"  content: {input1['content'][:30]}...")  # Truncate for display
    print(f"  author_first_name: {input1['author_first_name']}")
    print(f"  author_last_name: {input1['author_last_name']}")
    print(f"Expecting:\n{expected_output}")
    result = file_to_prompt(input1, to_string)
    print(f"Actual:\n{result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


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
