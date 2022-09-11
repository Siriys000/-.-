import string
import random
# Для Цезаря
str_a =list(string.ascii_lowercase)
shift = 6
# Для подстановочного
str_wildcard=list(string.ascii_lowercase)
random.shuffle(str_wildcard)

def crypt(text):
    str_result=""
    for c in text:
        if(c>='a' and c<='z'):
            str_result+= str_a[((ord(c) + shift)-ord('a'))%(len(str_a))]
        else:
            str_result+= c
    return str_result

def decrypt(text):
    str_result=""
    for c in text:
        if(c>='a' and c<='z'):
            str_result+= str_a[((ord(c) - shift)-ord('a'))%(len(str_a))]
        else:
            str_result+= c
    return str_result

# Подстановочный шифр
def crypt_wildcard(text):
    str_result=""
    for c in text:
        if(c>='a' and c<='z'):
            str_result+= str_wildcard[(ord(c)-ord('a'))]
        else:
            str_result+= c
    return str_result

def decrypt_wildcard(text):
    str_result=""
    for c in text:
        if(c>='a' and c<='z'):
            str_result+= str_a[str_wildcard.index(c)]
        else:
            str_result+= c
    return str_result

x="hello world!"

# Цезаря
y=crypt(x)
print(y)
print(decrypt(y))

#Подстановочный шифр
y=crypt_wildcard(x)
print(y)
print(decrypt_wildcard(y))
