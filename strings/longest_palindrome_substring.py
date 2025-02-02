"""
Python solution for finding longest palindrome substring
"""

"""
This method prints a substring

>>> print_sub_str("abcaaaaabc", 3, 7)
None
"""


def print_sub_str(string: str, low: int, high: int) -> None:
    """
    Inputs:
    string: String value representing input string
    low: Integer value representing starting index of substring
    high: Integer value representing ending index of substring

    Outputs:
    return Value: None
    """
    for i in range(low, high + 1):
        print(string[i], end="")


"""
This method finds the starting and ending index of the longest palindrome substring.
It also returns the length.

>>> longest_pal_substr("abcaaaaabc")
5
"""


def longest_pal_substr(string: str) -> int:
    """
    Inputs:
    string: String value representing the input string

    Outputs:
    return Value: maxLen (storing the length of longest palindrome substring)
    """
    n = len(string)
    max_len = 1
    start = 0

    for i in range(n):
        for j in range(i, n):
            flag = 1
            for k in range(0, ((j - i) // 2) + 1):
                if string[i + k] != string[j - k]:
                    flag = 0
            if flag != 0 and (j - i + 1) > max_len:
                start = i
                max_len = j - i + 1

    print("Longest Palindrome Substring:", end="")
    print_sub_str(string, start, start + max_len - 1)
    return max_len


"""
Driver Code
"""

if __name__ == "__main__":
    string = input()
    print("\nLength =", longest_pal_substr(string))
