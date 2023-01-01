#!/usr/bin/python3
try:
    file = open("mydata3.txt")
except FileNotFoundError as ex:
    print("Sorry the file is NOT availabe!")

    print(ex.args)
else:
    print("-----------FILE CONTENTS---------")
    print(file.read())
    print("---------------------------------")
finally:
    print("\n\n[Finished working with the file]")
