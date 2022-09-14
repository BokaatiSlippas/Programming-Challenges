def main():
  palindromes=0
  nonlychrel=0
  lychrel=0
  lower=int(input("Integer 1: "))
  higher=int(input("Integer 2: "))
  while lower<=higher:
    i=0
    done=False
    newlower=lower
    while done==False and i<=60:
      if ((len(str(newlower)))%2)==0:
        if ((str(newlower))[0:((len(str(newlower)))//2)])==(((str(newlower))[((len(str(newlower)))//2):])[::-1]):
          if i==0:
            palindromes+=1
            done=True
          else:
            nonlychrel+=1
            done=True
        else:
          newlower=newlower+(int(str(newlower)[::-1]))#Might have to separate int and str into separate lines REMEMBER!!!
          i+=1
      else:
        if str(newlower)[0:(((len(str(newlower)))+1)//2)]==((str(newlower)[(((len(str(newlower)))-1)//2):])[::-1]):
          if i==0:
            palindromes+=1
            done=True
          else:
            nonlychrel+=1
            done=True
        else:
          newlower=newlower+(int(str(newlower)[::-1]))#Might have to separate int and str into separate lines REMEMBER!!!
          i+=1
    if i==61:
      lychrel+=1
      print(f"{lower} is probably lychrel")
    i=0
    lower+=1
  print(f"Palindrome numbers = {palindromes}")
  print(f"Not lychrel numbers = {nonlychrel}")
  print(f"Lychrel = {lychrel}")
if __name__=="__main__":
  main()