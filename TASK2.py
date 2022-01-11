from statistics import mean
km,miles=[],[]
print("Swallow Speed Analysis: Version 1.0")
while True:
    s=input("Enter the Next Reading:")
    if s=="":break
    speed=float(s[1:]) 
    (miles.append(speed), km.append(speed*0.621371)) if s[0].lower()=="u" else  (km.append(speed),miles.append(speed*1.60934))
    print("Reading saved.")
if len(km)!=0: 
    print("{} Readings Analysed.\nmax speed:{:.2f}KPH,{:.2f}MPH\nmin speed:{:.2f}KPH,{:.2f}MPH\naverage speed:{:.2f}KPH,{:.2f}MPH".format(len(km),max(km),max(miles),min(km),min(miles),mean(km),mean(miles)))    
else:
    print("no values entered") 