def file_type_getter(file_extension_tuples):
    file_extensions_dict = {}
    for tuples in file_extension_tuples:
        for extension in tuples[1]:
            file_extensions_dict[extension] = tuples[0]
    return lambda extensions: file_extensions_dict.get(extensions, "Unknown")
