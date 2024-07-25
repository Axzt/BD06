def file_to_prompt(file, to_string):
    to_string_result = to_string(file)
    format_string = (f"```\n{to_string_result}\n```")
    return  format_string