def meters(rods):
    return rods*5.0292

def feet(rods):
    return (meters(rods)/0.3048)

def miles(rods):
    return (meters(rods)/1609.34)

def furlong(rods):
    return (rods/40)

def walktime(rods):
    distance=miles(rods)
    return ((distance/3.1)*60)

def enter_rods():
    return float(input("Input rods:"))

def pritt():
    rods=enter_rods()
    print(f"You input {rods} rods")
    print("Conversions")
    print(f"Metres: {meters(rods)}")
    print(f"Feet: {feet(rods)}")
    print(f"Miles: {miles(rods)}")
    print(f"Furlongs: {furlong(rods)}")
    print(f"Minutes to walk {rods} rods {walktime(rods)}")

if __name__ == "__main__":
    pritt()
