import re

print('This is the final lesson 1 from regular expression')

all_apes = re.findall("ape", "The ape was in the apex")

for i in all_apes:
    print(i)

the_str = "The ape was in the apex"
for i in re.finditer("ape.", the_str):
    loc_tuple = i.span()
    print(loc_tuple)
    print(the_str[loc_tuple[0]:loc_tuple[1]])

print("=========================")
print("Lesson 2 ")

rand_str = "F.B.I. I.R.S. CIA"
print("Matches :", len(re.findall(".\..\..", rand_str)))

rand_str2 = """This is a 
long string
that goes
on
many lines"""
print(rand_str2)
regex = re.compile("\n")
rand_str2 = regex.sub(" ", rand_str2)
print(rand_str2)

numb_str = "123456"
print("Matches :", len(re.findall("\d", numb_str)))

ph_numb = "412-555-76232"
if re.search("\w{3}-\w{3}-\w{4}", ph_numb):
    print("It is a phone number")
else:
    print("It's a code")

email_list = "db@aol.com m@.com @apple.com db@.com"

print("Email Matches :", len(re.findall("[\w. %+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}", email_list)))