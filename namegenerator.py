#10/18/24
#Period 5
#Name Generator

print("Which Gilmore Girls character are you???")
print("Answer the following questions to find out!")
ans = input ("winter (win) or summer (sum)?")
if ans == "win":
	ans = input("blue (b) or purple (p)")
	if ans == "b":
		ans = input("dinner (d) or breakfast (b)?")
		if ans == "d":
			print("You are Rory Gilmore!")
		else:
			print("You are Lorelai Gilmore!")
	if ans == "p":
		ans = input("books (b) or movies (m)?")
		if ans == "b":
			print("You are Jess!")
		else:
			print("You are Lane!")
if ans == "sum":
	ans = input("sweet (sw) or salty (sal)?")
	if ans == "sw":
		ans = input("coffee (c) or tea (t)?")
		if ans == "c":
			print("You are Sookie!")
		if ans == "t":
			print("You are Kirk!")
	if ans == "sal":
		ans = input("night owl (n) or early bird (e)?")
		if ans == "n":
			print("You are Logan!")
		if ans == "e":
			print("You are Paris!")
