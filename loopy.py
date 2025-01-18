#Write a loop that prints the numbers 1 to 5
for number in range(1,6):
    print(number)

#Pretend to fill a bucket of water until it is full
water_level = 0
full_level = 5
while water_level < full_level:
    print("Filling bucket... Water level is", water_level)
    water_level +=1 #add more water
print("Bucket is full")

#Exercise 1 : Print Even Numbers
for i in range(1,21):
    if i % 2 == 0:
     print(i)

#Exercise 2: Count Down to Zero
number = 10
while number >= 0:
   print(number)

#Exercise 3:Sum of Numbers
total = 0
for i in range(1, 11):
   total += i
print(total)

#Exercise 4:Guess the Secret Number
secret_number = 7
number = -1
while number != secret_number:
    number = int(input("Guess the secret number"))
    if number != secret_number:
        print("Keep guessing!")
print("You guessed it!")

#Exercise 5: Count characters in a string
sentence = "Python is awesome!"
count = 0
for char in sentence:
   count += 1
print("The number of characters is:", count)

#Exercise 6: Multiplication Table
number = 1
while number <= 10:
    print(number * 5)
    number+=1
    
#Exercise 7: Stop at Negative
numbers = [4, 7, 2, -1, 5, 8]
for number in numbers:
     if number < 0:
         break
     print(number)

#Exercise 8:Factorial of 5
factorial = 1
for number in range(1,6):
    factorial *= number
print("the factorial of 5 is:", factorial)


    



        



    


