y=input()
if y>="a" and y<="z" or y>="A" and y<="Z":
    x=y.lower()
    if y=="a" or y=="e" or y=="i" or y=="o" or y=="u":
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid")
