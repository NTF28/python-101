# magic8.py
# another way
import random

ans = [
  "Yes - definitely.",
  "It is decidedly so.",
  "Without a doubt.",
  "Reply hazy, try again.",
  "Ask again later.",
  "Better not tell you now.",
  "My sources say no.",
  "Outlook not so good.",
  "Very doubtful."
]

random = random.choice(ans) # '.choice' when using non numeric data

input("Question:      ")
print("Magic 8 Ball: ",random)
