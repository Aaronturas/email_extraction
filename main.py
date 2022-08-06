import re

pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
str = "My email is aaron4gonzalez@gmail.com for assistance"

match = re.search(pattern, str)
if match:
    print('Email:',match.group())

#Testcases
new_str = "Contact this email for assistance Aaronturas@protonmail.com"

match = re.search(pattern, new_str)
if match:
    print('Email:',match.group())