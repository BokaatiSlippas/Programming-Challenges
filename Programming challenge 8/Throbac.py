def romantonumber(roman):
  dict={"C":100,"L":50,"X":10,"V":5,"I":1}
  arr=[]
  for char in roman:
    arr.append(dict[char])
  arr.append(0)
  total=0
  i=0
  while i<len(arr):
    if arr[i]==0:
      break
    else:
      if arr[i]<arr[i+1]:
        total+=(arr[i+1]-arr[i])
        i+=2
      else:
        total+=arr[i]
        i+=1
  print(total)
def numbertoroman(number):
  number=onumber
  text=""
  while number>=100:
    text+="C"
    number-=100
  while number>=90:
    text+="XC"
    number-=90
  while number>=50:
    text+="L"
    number-=50
  while number>=40:
    text+="XL"
    number-=40
  while number>=10:
    text+="X"
    number-=10
  while number>=9:
    text+="IX"
    number-=9
  while number>=5:
    text+="V"
    number-=5
  while number>=4:
    text+="C"
    number-=4
  while number>=1:
    text+="I"
    number-=1
  return text

def main():
  n1=input("Enter first roman number no spaces:")
  print(romantonumber(n1))
  n2=input("Enter second roman number no spaces:")
  print(romantonumber(n2))
  print(f"Digital sum is {(romantonumber(n1))+(romantonumber(n2))}")
  print(f"Roman sum is {numbertoroman((romantonumber(n1))+(romantonumber(n2)))}")

if __name__=="__main__":
  main()
