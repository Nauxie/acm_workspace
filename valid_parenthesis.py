def isValid(s) -> bool:
        validity = True
        for i in range(len(s)-1):
            if (s[i] == "[" and(s[i+1] != "]"):
                validity = False
            elif (s[i] == "{" and(s[i+1] != "}"):
                validity = False
            elif (s[i] == "(" and(s[i+1] != ")"):
                validity = False
            if (len(s)% 2 !=0):
                validity = False
        return validity


print(isValid('[]{[]'))