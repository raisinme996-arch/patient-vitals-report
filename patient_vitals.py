patient_name = "Patient A"
age = 45
weight_kg = 70.0
height_m = 1.65
temperature_c = 38.5
heart_rate = 110
systolic_bp = 135
bmi = weight_kg / (height_m ** 2)
bmi = round(bmi, 1)
has_fever = temperature_c > 37.5
fast_heart_rate = heart_rate > 100
high_bp = systolic_bp >= 130
print("PATIENT VITALS REPORT")
print("Name:", patient_name)
print("Age:", age)
print("BMI:", bmi)
print("Fever:", has_fever)
print("Fast heart rate:", fast_heart_rate)
print("High blood pressure:", high_bp)
temperature_c = 37.1
has_fever = temperature_c > 37.5
print("Temperature after treatment:", temperature_c)
print("Fever now:", has_fever)
