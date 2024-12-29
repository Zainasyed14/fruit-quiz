import random

class FruitQuiz:

    def __init__(self):
        self.fruits = {"Kiwi" : "green",
                     "Grapes" : "purple",
                     "Banana" : "yellow",
                     "Strawberry" : "red",
                     "Orange" : "orange",
                     "Apple" : "red",
                     "Dragonfruit" : "pink"}
    
    def Quiz(self):
        while (True):

            fruit,color = random.choice(list(self.fruits.items()))
            print("State the color of the fruit", (fruit))
            userAns = input()

            if(userAns.lower()== color):
                print("Correct Answer")

            else:
                print("Incorrect Answer")

            option = input("Enter 1 to play again. Press any other key to exit ")
            if option == "1":
                print("*********************************************************************")
                print("You have chosen to play again. Here is your second chance!!")
                continue
            else:
               print("**********************************************************************")
               print("Quiz Over!!")
               break

quiz =FruitQuiz()
quiz.Quiz() 