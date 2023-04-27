def remove_and_strip(string, word):
    newStr=string.replace(word,"")
    return newStr.strip()

this = "    this is a drag     "

n =remove_and_strip(this,"this")

print(n)
