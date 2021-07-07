# tank overflow

r = float(input("Enter the radius of the tank (m) "))# radius of the tank
h = float(input("Enter the height of the tank (m) "))# height of the tank
f = float(input("Enter the rate of liquid entering the tank m^3/min "))# the rate of liquid going into the tank in m^3 per minute
t = float(input("Enter the duration of time the liquid will be entering the tank in minutes ")) # time
pi = 3.14159
vTank = float(pi*pow(r,2)*h)# tank volume
vLiq = float(f*t) # volume of liquid
vOverflow = float(vLiq-vTank) # amount overflown by
if vLiq > vTank:
    print("The tank has overflowed by " + str(vOverflow))
else:
    print("Tank not over filled")
    