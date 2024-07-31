def find_common_elements(list_1, list_2):
    set_1 = set(list_1)
    set_2 = set(list_2)
    common = set_1.intersection(set_2)
    return list(common)
