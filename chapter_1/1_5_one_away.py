def one_away(str1, str2):
    if len(str1) == len(str2):
        return check_replacements(str1, str2)
    elif len(str1) == len(str2) + 1:
        return check_add_remove(str2, str1)
    elif len(str1) +1 == len(str2):
        return check_add_remove(str1, str2)
    else:
        return False

def check_replacements(str1, str2):
    num_diff = 0
    for c1, c2 in zip(str1, str2):
        if num_diff > 1:
            return False
        if c1 != c2:
            num_diff += 1

    return True

def check_add_remove(str1, str2):
    index1 = 0
    index2 = 0

    while (index1 < len(str1) and index2 < len(str2)):
        if str1[index1] != str2[index2]:
            if index1 != index2:
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1

    return True

if __name__ == "__main__":
    print(one_away("pale", "plf"))