
# Determine if string is a number using recursion
def isNum(s:str):

    if "." in s:
        if s.index(".") != s.rindex("."):
            return False
        return isNum(s[:s.index(".")]) and isNum(s[s.index(".")+1:])
    
    else:
        if s == "":
            return True
        return s.isnumeric()
    
def get_course_title(name:str) -> str:
    name = name.split()

    newName = ""

    for word in name:
        if len(word) > 5:
            newName += word[:5] + ". "
        else:
            newName += word + " "
    
    return newName.strip()

def get_course_title2 (name):
    new_name = ""
    word = ""
    count = 0

    for char in name:
        if char == " ":
            count = 0
            new_name += word + " "

            word = ""
        else:
            if count < 5:
                word += char

            elif count == 5:
                word += ". "
            count += 1
    
    return new_name + word