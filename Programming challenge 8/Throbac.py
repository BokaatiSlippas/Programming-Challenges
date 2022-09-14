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
  