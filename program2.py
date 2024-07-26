def decode_message( s: str, p: str) -> bool:

# write your code here
        if len(s) != len(p):
                return False
        for i in range(len(s)):
                