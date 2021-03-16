import hashlib  # module used to Use MD5 hash function using

PWname = '1MillionPassword_hashed.txt'  # file to crack

# After opening and reading the file,
# all elements divided by lines of PWname is appended in to a list.
# The list is then used to be crack each elements.
PWlist = open(PWname, 'r').readlines()
PWlist = list(map(str.strip, PWlist))

count = 0  # number of elements cracked
totalcount = 0  # number of elements checked

# Hashing the elements.
for PWlist in PWlist:
    with open('wordlist.txt', 'r') as wordlist:
        for line in wordlist:
            line = line.strip()
            if hashlib.md5(line.encode('utf-8')).hexdigest() == PWlist:
                # 'utf-8' is used to prevent encoding problems
                # the cracked results are converted to string using the function 'hexdigest()'

                # prints out like the format of the assignment
                print(count, ' / 1000000 password has been cracked', end='')
                print(', hashed: ', PWlist, end='')
                print(", cracked: " + line)
                count += 1
        totalcount += 1

# Indication methods to know if cracking is over and done to all elements
print("\n----------------------------------------------")
print("Cracking has been completed.")
print(totalcount, "passwords have been checked.")
print(count, "passwords have been cracked.")
print("----------------------------------------------")
