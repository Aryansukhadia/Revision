def replaceChar(s,a,b):
    if len(s)==0:
        return s
    smallOutput = replaceChar(s[1:],a,b)
    if s[0]==a:
        return b+smallOutput
    else:
        return s[0] + smallOutput
    
replaceChar("dacdxcd","c","x")
print(replaceChar("dacdxcd","c","x"))