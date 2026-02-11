# List of products on promotion for each weekday
daily_promotions = ["Milk", "Eggs", "Bread", "Apples", "Oranges"]

# List of weekdays corresponding to the promotions
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Loop over the correct range (0 through 4)
for day in range(len(weekdays)):
    weekday = weekdays[day]          # Get the current weekday
    promotion = daily_promotions[day]  # Get the promotion for the current day
    print(f"{weekday}: Promotion on {promotion}")