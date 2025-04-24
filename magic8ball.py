import random
print("Magic 8 Ball")
name = input("Please enter your name: ")
question = input("Please ask your question that has a 'Yes' or 'No' answer: ")
answer = ""
random_number = random.randint(1,9)
print("Hello " + name + "\nYou asked: " + question + "\n")
if random_number == 1: 
  answer = "Yes - definitely"
elif random_number == 2: 
  answer = "It is decidely so"
elif random_number == 3: 
  answer = "Without a doubt"
elif random_number == 4: 
  answer = "If it's meant to be, it will happen" 
elif random_number == 5: 
  answer = "High chances" 
elif random_number == 6: 
  answer = "Better not tell you now"
elif random_number == 7: 
  answer = "My sources say no"
elif random_number == 8: 
  answer = "Outlook not so good"
elif random_number == 9: 
  answer = "Very doubtful"
else:  
  print("Error")     
print("Magic 8-Ball's answer: " + answer)        