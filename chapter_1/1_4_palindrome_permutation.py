def is_palindrome_permutation(str1):
    """
    O(N) solution using a dictionary to count totals of each character and checking that only one
    character has an odd count (middle characters)
    """
    # remove white-space and make all lower case
    str1 = str1.lower()
    str1 = "".join(str1.split())
    

    str_dict = {}
    for c in str1:
        if c in str_dict:
            str_dict[c] += 1
        else:
            str_dict[c] = 1

    num_even = 0
    num_odd = 0
    for c in str_dict:
        if str_dict[c] % 2 == 0:
            num_even += 1
        else:
            num_odd += 1

    return num_odd <= 1


if __name__ == "__main__":
    print(is_palindrome_permutation("tact vcoa"))