# GuessNumber
import random
print("********GuessNumber********")
temp = input("GuessNumber:")
Guess = int(temp)
secret = random.randint(1,100)

while Guess != secret:
    print("wrong!")
    if Guess<secret:
        print("bigger next time!")
    else:
        print("smaller next time!")
    Guess = int(input())

print("you smart ass!")
print("GameOver")
