def replace_pi(s):
    if len(s)==0 or len(s)==1:
        return s
    if s[0]=='p' and s[1]=='i':
        smalloutput = replace_pi(s[2:])
        return "3.14" + smalloutput
    else:
        smalloutput = replace_pi(s[1:])
        return s[0]+smalloutput
replace_pi("abcpi")
print(replace_pi("abcpi"))