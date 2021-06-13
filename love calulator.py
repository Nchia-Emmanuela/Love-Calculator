print("Welcome to the python love calculator!")


name1 = input("Enter your name:\n")

name2 = input("Enter their name:\n")

names = (name1 + name2).lower()

t_occurs = names.count("t")
r_occurs = names.count("r")
u_occurs = names.count("u")
e_occurs = names.count("e")
total1 = t_occurs + r_occurs + u_occurs + e_occurs
print(f"true = {total1}")

l_occurs = names.count("l")
o_occurs = names.count("o")
v_occurs= names.count("v")
e_occurs = names.count("e")
total2 = l_occurs + o_occurs + v_occurs + e_occurs
print(f"love = {total2}")

score = str(total1) + str(total2)
love_score = int(score)

if love_score <= 10 or love_score >= 90:
    print(f"your love score is {love_score}: you go like coke and mentos")
elif love_score >= 40 and love_score <= 50:
    print(f"your love score is {love_score}: you are okay")
else:
    print(f"your love score is {love_score}")

