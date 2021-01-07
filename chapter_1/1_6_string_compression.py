def string_compression(str1):
    compress_string = ""
    current_count = 1

    for i in range (1, len(str1)):
        if str1[i] == str1[i-1]:
            current_count += 1
        else:
            compress_string = compress_string + str1[i-1] + str(current_count)
            current_count = 1

        if i == len(str1) - 1:
            compress_string = compress_string + str1[i] + str(current_count)

    if len(compress_string) < len(str1):
        return compress_string
    else:
        return str1

if __name__ == "__main__":
    print(string_compression("aabcccccaaa"))