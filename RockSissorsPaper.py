
# coding: utf-8

# In[11]:

p1=raw_input("Rock Sissors Paper player 1 input R or S or P: ")
p2=raw_input("Rock Sissors Paper player 2 input R or S or P: ")

if (p1 == p2):
	print("Draw!");
elif (p1 == "R"):
	if (p2 == "P"):
		print("p2 wins!");
	else:
		print("p1 win!");
elif (p1 == "P"):
	if (p2 == "R"):
		print("p1 win!");
	else:
		print("p2 win!")
elif (p1 == "S"):
	if (p2 == "R"):
		print("p2 win!");
	else:
		print("p1 win!");

