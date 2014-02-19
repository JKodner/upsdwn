my_dict = {
    "a" : "ɐ", "b" : "q", "c" : "ɔ", "d" : "p", "e" : 
    "ǝ", "f" : "ɟ", "g" : "ƃ", "h" : "ɥ", "i" : "ı", "j" 
    : "ɾ", "k" : "ʞ", "l" : "l", "m" : "ɯ", "n" : "u", 
    "o" : "o", "p" : "b", "r" : "ɹ", "s" : "s", "t" : 
    "ʇ", "u" : "n", "v" : "ʌ", "w" : "ʍ", "x" : "x", "y" 
    : "ʎ", "z" : "z"
    }
print "Welcome to the sentence to upside-down translator!"
v = raw_input("What sentence do you want upside-down?")
def reverse(v):
    x = " "
    for i in v:
        if i.isalpha():
            i = i.lower()
            i = my_dict[i]
            x = x + i
        else:
            x = x + i
    print "\'%s\' upside-down is:" % v
    print x
reverse(v)