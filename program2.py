def decode_message( s: str, p: str) -> bool:

# write your code here
         if len(s) != len(p):
                return False
    
        for i in range(len(s)):
            if p[i] == '?':
               if not s[i].isalpha():
                  return False
            elif p[i] == '*':
               continue
            elif s[i] != p[i]:
                return False
    
    return True

