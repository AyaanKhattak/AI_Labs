month_names = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
calendar = {}

for month_name in month_names:
    calendar[month_name] = {}
    for week_num in range(1, 5):  # Weeks numbered 1 to 4
        calendar[month_name][f"Week {week_num}"] = []

calendar["July"]["Week 2"].append("Family picnic at the park")

print("Calendar with month names and numbered weeks:")
for month, weeks in calendar.items():
    print(f"{month}:")
    for week, events in weeks.items():
        print(f"  {week}: {events}")

print("\nSpecific access:")
print("July Week 2 events:", calendar["July"]["Week 2"])