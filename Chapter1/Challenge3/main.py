def deduplicate_lists(lst1, lst2, reverse=False):
    lst = []
    for item in lst1:
        lst.append(item)
    for item in lst2:
        if item not in lst:
            lst.append(item)
    
    if reverse:
        return sorted(lst, reverse=True)
    return sorted(lst)