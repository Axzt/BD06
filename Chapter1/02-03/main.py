def add_prefix(document, documents):
    prefixed_document = f"{len(documents)}. {document}"
    return documents + (prefixed_document,)