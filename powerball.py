def main():
	fname = input("Enter your first name: ")
	lname = input("Enter your last name: ")
	userNums = []
	try:
		x=int( input("select 1st # (1 thru 69): "))
		if (1 <= x <= 69) and type(x) == type(1):
			userNums.append(x)
		x=int(input("select 2nd # (1 thru 69 excluding " + str(userNums[0])+ "): "))
		if (x not in userNums) and (1 <= x <= 69) and type(x) == type(1):
			userNums.append(x)
		x=int( input("select 3rd # (1 thru 69 excluding " +  str(userNums[0]) +" and "+  str(userNums[1])+ "): "))
		if (x not in userNums) and (1 <= x <= 69) and type(x) == type(1):
			userNums.append(x)
		x=int( input("select 4th # (1 thru 69 excluding " +  str(userNums[0]) + ", " +  str(userNums[1]) +", and "+  str(userNums[2])+ "): "))
		if (x not in userNums) and (1 <= x <= 69) and type(x) == type(1):
			userNums.append(x)
		x=int(input("select 5th # (1 thru 69 excluding " +  str(userNums[0]) + ", " +  str(userNums[1]) +", " +  str(userNums[2]) +", and "+  str(userNums[3])+ "): "))
		if (x not in userNums) and (1 <= x <= 69) and type(x) == type(1):
			userNums.append(x)
		x = int( input("select Power Ball # (1 thru 26): "))
		if  (1 <= x <= 26) and type(x) == type(1):
			pbNum= x

		SaveData(fname,lname,userNums,pbNum)

		#Based on the sample output, I have created seperate list for each number position
		#This can be ranndomised further by creating 1 list for all 5 positions
		selected_numbers_1 = []
		selected_numbers_2 = []
		selected_numbers_3 = []
		selected_numbers_4 = []
		selected_numbers_5 = []
		powerball_numbers=[]

		for row in ReadData():
			selected_numbers_1.append(row[3])
			selected_numbers_2.append(row[4])
			selected_numbers_3.append(row[5])
			selected_numbers_4.append(row[6])
			selected_numbers_5.append(row[7])
			powerball_numbers.append(row[8])
			print(str(row[1]) + " " + str(row[2]) + " " + str(row[3]) + " " + str(row[4]) + " " + str(row[5]) + " " + str(row[6]) + " " + str(row[7]) + " Powerball: " + str(row[8]))

		print ("Powerball winning number:")
		ticket_numbers = []
		ticket_numbers.append(CreateLottoNumber(selected_numbers_1)) 
		ticket_numbers.append(CreateLottoNumber(selected_numbers_2)) 
		ticket_numbers.append(CreateLottoNumber(selected_numbers_3)) 
		ticket_numbers.append(CreateLottoNumber(selected_numbers_4)) 
		ticket_numbers.append(CreateLottoNumber(selected_numbers_5)) 
		print (" ".join(str(x) for x in ticket_numbers) + " Powerball: " + str(CreateLottoNumber(powerball_numbers)))

	except Exception as e:
		print (e)


def CreateLottoNumber (selected_list):
	distinct_list = list(set(selected_list))
	distinct_list_count = {}
	for l in distinct_list:
		distinct_list_count[str(l)] = selected_list.count(l)

	#the list is sorted by number of occurrences descending and the topmost count is chosen
	max_number = int("".join(str(y) for x,y in sorted(distinct_list_count.items(), key=lambda x: (-x[1], x[0]))[:1]))

	#selecting all the numbers that have the topmost occurrence
	max_selected_list=[]
	for key, value in distinct_list_count.items():
	    if value == max_number:
	        max_selected_list.append(key)

	#From the above list a randon number is chosen
	import random
	return random.choice(max_selected_list)

import mysql.connector

def GetConnection():
	return mysql.connector.connect(user='root', password='admin',host='localhost',database='powerball')

def SaveData (fname,lname, userNums, pbNum):
	conn = GetConnection()
	cur = conn.cursor()

	try:
		cur.execute ("INSERT INTO Employee (fName, lName, num1, num2, num3,num4, num5,numPb) VALUES (%s, %s, %s, %s,%s, %s, %s, %s)", 
										(fname, lname,userNums[0],userNums[1],userNums[2],userNums[3],userNums[4] , pbNum))
		conn.commit()
	except Exception as e:
		print(e)
		conn.rollback()
	cur.close()
	conn.close()
	return

def ReadData ():
	conn1 = GetConnection()
	cur1 = conn1.cursor()

	try:
		cur1.execute("SELECT *  FROM Employee")
		data = cur1.fetchall()
	except Exception as e:
		print(e)
	cur1.close()
	conn1.close()
	return data

main()