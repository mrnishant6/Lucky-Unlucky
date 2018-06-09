num = input("What Is The Range Of Your Numbers?")
num = int(num)
for i in range(num):
	if i ==4 or i==13:
		print(f"{i} is unlucky")
	elif i % 2 == 0:
		print(f"{i} is even")
	else :
		print(f"{i} is odd")
