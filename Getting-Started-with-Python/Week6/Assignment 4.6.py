def computepay(h,r):
    if h > 40:
        return (40*r+(h-40)*1.5*r)
    elif 0<h<40:
        return h*r
    else:
        return False

try:
    hrs = input("Enter Hours:")
    hours = float(hrs)
    r = input("Enter your rate:")
    rate = float(r)
    p = computepay(hours,rate)
    print(p)
except:
    print("Enter your number")