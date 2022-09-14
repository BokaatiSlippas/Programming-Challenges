def calculation(slayer):
  newslayer=str(slayer)
  newslayer=int(newslayer[1:]+newslayer[0])
  if (3*slayer)==newslayer:
    return True
  else:
    return False
def main():
  print("Guess a six_digit number SLAYER so that following equation is true, where each 1 letter stands for the digit in the position shown: SLAYER + SLAYER + SLAYER = LAYERS")
  slayer=int(input("Enter your guess for SLAYER: "))
  if calculation(slayer):
    print("Your guess is correct")
  else:
    print("Your guess is wrong")
  print(f"SLAYER + SLAYER + SLAYER = {3*slayer}")
  print(f"LAYERS = {((str(slayer))[1:])+((str(slayer))[0])}")
  print("Thanks for playing")
if __name__=="__main__":
  main()