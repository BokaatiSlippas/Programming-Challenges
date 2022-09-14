def main():
  print("We are going to play a game. I want you to pick a number then do a series of calculations. I bet I know what the result of those calculations will be!")
  answer=int(input("*You* This is will be the answer. Select a number between 10-49: "))
  factor=99-answer
  select=int(input("*Player* Pick any number 50-99: "))
  newselect=select+factor
  hundreds=str(newselect)
  newselect+=(int(hundreds[0])-100)
  print(f"I said the answer was {answer} and the calculation result is {select-newselect}")
if __name__=="__main__":
  main()