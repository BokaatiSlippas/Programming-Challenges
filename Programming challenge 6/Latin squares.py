def main():
  order=int(input("Please input the order of square: "))
  topleft=int(input("Please input the top left number: "))
  final=""
  string=""
  for i in range(order):
    newtopleft=topleft
    for j in range(order):
      if newtopleft<=order:
        string+=(str(newtopleft)+" ")
      else:
        newtopleft=1
        string+=(str(newtopleft)+" ")
      newtopleft+=1
    final+=(string[:-1]+"\n")
    string=""
    if topleft==order:
      topleft=0
    topleft+=1
  print(final[:-1])
if __name__=="__main__":
  main()