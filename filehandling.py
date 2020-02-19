# read
fopen = open("readme.txt")
print(fopen.read())
fopen.close()

#write
fopen = open("readme1.txt", 'w')
userinput = input("plz enter your name: ")
name = fopen.write(userinput)
print(name)
if len(userinput) == name:
    print("sucessfully saved data")
fopen.close()

#append
fopen = open("readme2.txt", 'a')
userinput = input("plz enter your name: ")
name = fopen.write(userinput)
print(name)
if len(userinput) == name:
    print("sucessfully saved data")
fopen.close()

#write a program to make a expense wallet on console base
# where user can add the daily expenses and can view expenses in 3 ways
#user se lo gey kisliye kharcha kiya aur kitna kharcha kiya
#daily
#weekly
#monthly
#(use functions modules and file handling)
#use date and time module help
