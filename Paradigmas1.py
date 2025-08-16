# 1KG de grasa = 7700 calorias 
# 10 KG de grasa = 77000 calorias

def calories_to_lose_weight(weight_to_lose_kg, days=30):
    calories_per_kg = 7700
    total_calories = weight_to_lose_kg * calories_per_kg
    daily_calories = total_calories / 90  # Assuming a 90-day period
    return total_calories, daily_calories

print("calculator to lose weight")
weight_to_lose = float(input("Please enter the weight you want to lose in KG: "))
days_to_lose = int(input("Please enter the number of days you want to lose that weight in: "))  

total_calories, daily_calories = calories_to_lose_weight(weight_to_lose, days=30)

print(f"\nTo lose {weight_to_lose} kg you need to burn aproximately {total_calories:.0f} calories")
print(f"That is equal to {daily_calories:,.0f} calories per day for {days_to_lose} days")


