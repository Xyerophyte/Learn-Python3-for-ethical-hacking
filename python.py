#!/bin/python3
#import sys #imports the module system function and parameters
#from datetime import datetime as dt #imports module for date and time but specifically only date and time with alias
#import socket


#Print
#print("Hello World") #prints the text Hello World
#print('\n') #prints a new line
#print("This string runs multiple lines")


#Math
#print(50+50)#add
#print(50-50)#subtract
#print(50*50)#multiply
#print(50/50)#divide
#print(50+50-50*50/50)#Dmas
#print(50**50)#to the power of
#print(50%4)#modulo
#print(50//4)#only decimals
#print('\n')#prints a new line


#Variables and Methods
#quote = "All is fair in war."#string
#print(quote.upper()) #makes the quote uppercase
#print(quote.lower()) #makes the quote lowercase
#print(quote.title()) #title cases
#print(len(quote)) #prints the length of quote
#name = "Harsh" #string
#age = 15 #integer
#gpa = 3.7 #float is a integer with decimals
#print("My name is "+ name + " and I am " + str(age) + " years old.") #My name is Harsh and I am 15 years old.
#print("My name is " + name + " and I was " + str(age) + " years old.") #My name is Harsh and I was 15 years old.
#age += 1 #adds 1 to my age; can use any number not just 1
#print("But now I am " + str(age) + " years old.") #But now i am 16 years old.


#Functions
#def who_am_i(): #this is a function
	#name = "Xyero"
	#age = 15
	#print("My name is "+ name + " and I am " + str(age) + " years old.")
#who_am_i() #this is done to call the who_am_i function
#def add_one_hundred(num): #this is a single parameter function
	#print(num + 100)
#add_one_hundred (100) #this will be 100+100


#Multiple Parameters
#def add(x,y): #this is a multiple parameter
	#print(x+y)
#add(7,7)
#def multiply(x,y):
	#return x*y #This is usually used for storing a value but not printiing it out. we can print it out anytime we want but the return just stores the value.
#multiply(7,7) #This wont do anything unless we tell it to do anything it just stores the value 7*7
#print(multiply(7,7)) #This is going to print the value
#def square_root(x):
	#print(x ** .5)
#square_root(4)
#def nl(): #nl = new line
	#print('\n') #prints new line
#nl() #makes a new line


#Boolian Expressions
#Boolian Expressions are basically just True or False
#print("Boolian Expressions: ")
#bool1 = True
#bool2 = 3*3 == 9 #3*3 is equal to 9 is stated here which is true
#bool3 = False
#bool4 = 3*3 != 9 #3*3 is not equal to 9 is false
#print(bool1, bool2, bool3, bool4)
#print(type(bool1)) #it will show <class = 'bool'>


#Relational and Boolian Operators
#greater_than = 7>5 #7 is greater than 5 so this is true
#less_than = 5<7 #5 is less than 7 so this is also true
#greater_than_equal_to = 7>=7 #7 is more than or equal to 7 which is true as well
#less_than_equal_to = 7<=7 #7 is less than or equal to 7 true again
#test_and = (7>5) and (5<7) #this is true
#test_and2 = (7>5) and (5>7) #this is false because 5 is not more than 7 so whole is false
#test_or = (7>5) or (5>7) #this is true because at least one is true
#test_or2 = (7<5) or (5>7) #this is false because both are false
#test_not = not True #test_not is not true so false


#Conditional Statements
#def drink(money): #usage = drink(*amount of money in $*)
	#if money >= 2: #IF you put a larger number than 2 or put 2 then return this below statement
		#return "You have a drink for yourself!" #prints this 
	#else: #IF you put a number less than 2 or anything else you print the below statement.
		#return "You don't have enough money!"
#print(drink(3)) #it will print the 1st statement
#print(drink(1)) #it will print the 2nd statement
#def alcohol(age,money): #need to requirement age and money
	#if age >= 21 and money >= 5: #if age is more than or equal to 21 AND money is more than or equal to 5 return below statement.
		#return "You bought a bottle of alcohol."
	#elif age >= 21 and money < 5: #if age is more than or equal to 21 AND money is less than 5 return below statement.
		#return "You are poor and have no money."
	#elif age < 21 and money >= 5: #if age is less than 21 AND money is more than or equal to 5 return below statement.
		#return "Nice try, kid."
	#else: #if age less than 21 AND money less than 5 return below statement.
		#return "Sorry no alcohol for you because you are too young and too poor."
#print(alcohol(21,5))
#print(alcohol(20,5))
#print(alcohol(21,4))
#print(alcohol(20,4))


#List (have brackets [])
#movies = ["The Terminator","The Avengers","The Guardians of the Galaxy","X-MAN"] #List of movies so 4 movies in this list
#print(movies[0]) #remember- Lists start from 0 not 1 so if you want to print out first movie out of our list we have to use print(movies[0[) not print(movies[1]
#print(movies[1:3]) #this prints out the movies from 1 to 3 but this won't include the 3rd one so to print out the 3rd one as well we have to do print(movies[1:4])
#print(movies[0:]) #this prints out everything starting from 0 and till the end of the list
#print(movies[:3]) #this is going to print every movie before the 3rd one excluding the 3rd one
#print(movies[-1]) #this will print the last item of the list
#print(len(movies)) #prints the number of items in the list
#movies.append("Batman") #adds Batman to the list to the end of list
#movies.pop() #this will remove the last item in the list but if you add the number inside the bracket it will remove the particular item in the list


#Tuples (can't change () )
#grades = ("a","b","c","d","f") #you cannot change this tuple
#print(grade[1])


#Looping

# -For loops = start to finish of a iterate
#fruits = ["Apple","Banana","Grapes"] #This is a list of fruits
#for x in fruits: #this means that for the value x in fruits do the below statement
	#print(x) #prints the value x which is now fruits so will print the list of fruits

# -While loops = runs as long as its true
#i = 1 #this variable i is equal to 1
#while i < 10: #while i is less than 10 this while loop will run until its equal to 10 
	#print(i) #prints i
	#i += 1 #keep printing i while adding 1 to each until i will be less than 10


#Advanced Basic python
#print(sys.version) #prints the version of python
#print(dt.now()) #prints the date and time currently


#Advanced strings
#my_name = "Xyero"
#print(my_name[0]) #prints the first alphabet from my name
#print(my_name[-1]) #pritns the last alphabet of my name
#sentence = "This is a sentence."
#print(sentence[0:4]) #prints the first 4 letters
#print(sentence.split()) #splits the sentence without spaces because default is space
#sentence_split = sentence.split() #variable which splits the sentence
#sentence_join = ' '.join(sentence_split) #variable fro joining the split sentence 
#print(sentence_join) #prints the joined statement/sentence
#quote = "He said, \"Give me all your money.\"" #this \"...\" will help you use a " inside of quotes which normally you can't OR you can use single quotes instead of double quotes and vice versa and this is called a character escape.
#print(quote)
#too_much_space = "          hello          " #this has a lot of spaces
#print(too_much_space.strip()) #this will strip away the spaces
#print("A" in "Apple") #this is asking is there is A in Apple so its gonna show true
#letter = "A"
#word = "Apple"
#print(letter.lower() in word.lower()) #Improved version of above code. This is turning the letter and the word to lowercase and then finding the letter a in apple.
#movie = "Avengers"
#print("My favourite movie is {}.".format(movie)) #this is going to print My favourite movie is avengers by using the {} and then the .format(movie) after the print. This is done for a better alternative to this down below
#print("My favourite movie is " + movie + ".") #this works as well but the better version to write this is the upper one


#Dictionaries (key/value pairs {} )
#drinks = {"White Russian": 7, "Old Fashioned": 10, "Lemon Drop": 13} #drink is key and price is value
#employees = {"Finance Department": ["Bob", "Lynda", "Tine"], "IT Department": ["Gene", "Louis", "Teedy"], "Human Resource Department": ["Jimmy", "Wiz", "Mort"]}
#employees["Legal Department"] = ["Mr.John"] #this adds a new key:value pair
#employees.update({"Sales Department": ["Andie", "Ollie"]}) #this adds a new key:value pair as well
#drinks["White Russian"] = 8 #updates the price of drinks
#print(employees)
#print(drinks)
#print(drinks.get("White Russian")) #prints the value for "White Russian"


#Sockets
#HOST = '127.0.0.1'
#PORT = 7777
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # for now AF_INEt is ipv4 and SOCK_STREAM is a port
#s.connect((HOST, PORT)) #makes a connection

#use netcat to establish a listening port. syntax = nc -nvlp 7777


#Scanner

#Define our target
#if len(sys.argv) == 2:
	#target = socket.gethostbyname(sys.argv[1]) #Translating host name to IPv4
#else:
	#print("Invalid amount of arguments.")
	#print("Syntax- python3 scanner.py <ip>")

#Add a banner
#print("=" * 50)
#print("\n")
#print("Scanning target " + target)
#print("Time started " + str(dt.now()))
#print("\n")
#print("=" * 50)

#try:
	#for port in range(1, 255): #For loop in range of 50-85.
		#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Making a connection.
		#socket.setdefaulttimeout(1) #Sets default timeout for server.
		#result = s.connect_ex((target, port)) #Returns a error indicator.
		#print("Checking port {}".format(port))
		#if result == 0:
			#print("Port {} is open.".format(port))
		#s.close() #Closes the connection.

#except KeyboardInterrupt: #If an keyboard interuption is made it will trigger this.
	#print("\nExiting Program...")
	#sys.exit()
#except socket.gaierror: #If there isn't a hostname resolution this will be triggered.
	#print("\nHostname could not be resolved.")
	#sys.exit()
#except socket.error: #If there is a connection error.
	#print("\nCouldn't connext to the server")
	#sys.exit()

#You have completed the basic python needed for hacking!