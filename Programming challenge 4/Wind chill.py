def calculation(air_temp,air_speed):
  return(35.74+(0.6215*air_temp)-(35.75*(air_speed**0.16))+(0.4275*air_temp*(air_speed**0.16)))
def windchill():
  print(f"Temperature of 10 and a speed of 15 gives windchill of:  {calculation(10,15)}")
  print(f"Temperature of 0 and a speed of 25 gives windchill of:  {calculation(0,25)}")
  print(f"Temperature of -10 and a speed of 35 gives windchill of:  {calculation(-10,35)}")
  airtemp=float(input("Temperature: "))
  airspeed=float(input("Speed: "))
  print(f"Windchill: {calculation(airtemp,airspeed)}")
if __name__=="__main__":
  windchill()