def get_median_font_size(font_sizes):
    if not font_sizes:
        return None
    sorted_list = sorted(font_sizes)
    n = len(sorted_list)
    if n % 2 == 0:
        return ((sorted_list[(n//2)-1]) + (sorted_list[(n//2-1)]+1)) // 2
    else:
        return sorted_list[(n//2)]
    