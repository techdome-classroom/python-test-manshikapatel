def decode_message(s: str, p: str) -> bool:
    def match(si: int, pi: int) -> bool:
        if pi == len(p):
            return si == len(s)
        
        if si == len(s):
            
            return all(p[k] == '*' for k in range(pi, len(p)))
        
        if p[pi] == s[si] or p[pi] == '?':
            return match(si + 1, pi + 1)
        elif p[pi] == '*':
            
            while si <= len(s):
                if match(si, pi + 1):
                    return True
                si += 1
        return False
    
    return match(0, 0)


