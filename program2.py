def decode_message( s: str, p: str) -> bool:

# write your code here
         if len(s) != len(pattern):
        return False
    
    for i in range(len(input_string)):
        if pattern[i] == '?':
            if not input_string[i].isalpha():
                return False
        elif pattern[i] == '*':
            continue
        elif input_string[i] != pattern[i]:
            return False
    
    return True

# Example usage:
print(decode_message("aa", "a"))    # Output: False
print(decode_message("aa", "*"))    # Output: True
print(decode_message("cb", "?a"))   # Output: False
print(decode_message("abc", "?b?"))