BB = 51
TB = 1.7
BMI = BB/(TB**2)
print ("BMI")

if BMI < 18.5:
    print("Kekuranagn Berat Badan")
    
elif BMI >= 18.5-24.9:
    print ("ideal")
        
elif BMI > 25.0-29.9:
    print("Kelebihan Berat Badan")
    
elif BMI > 30.0:
    print ("Obesitas co")

else: 
    print("Di luar nalar")