import sys
w=float(sys.argv[1])
h=float(sys.argv[2])
bmi = w/(h**2)
print "%.2f" %bmi
if bmi < 15: status = "Very severely underweight"; print status; exit(1)
if bmi >= 15 and bmi <= 16: status = "Severely underweight"; print status; exit(1)
if bmi > 16 and bmi <= 18.5: status = "Underweight"; print status; exit(1)
if bmi > 18.5 and bmi <= 25: status = "Normal"; print status; exit(1)
if bmi > 25 and bmi <= 30: status = "Overweight"; print status; exit(1)
if bmi > 30 and bmi <= 35: status = "Moderately obese"; print status; exit(1)
if bmi > 35 and bmi <= 40: status = "Severely obese"; print status; exit(1)
if bmi > 40: status = "Very severely obese"; print status; exit(1)