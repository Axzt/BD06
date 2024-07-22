def format_line(line):
    # broken up function, to debug
    """ 
    print(f"Original Line: {line}")
    stripped_line = line.strip()
    print(f"Stripped Line: |{stripped_line}|")
    capitalized_line = stripped_line.upper()
    print(f"Capitalized Line: {capitalized_line}")
    remove_punctuation = capitalized_line.replace('.', '')
    print(f"No Punctuation Line: {remove_punctuation}")
    formatted = remove_punctuation +"..."
    return formatted
    """
    # Fixed return statement
    return f"{line.strip().upper().replace('.', '')}..."

