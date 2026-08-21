def main() -> None:
    
    while True:
        
        name = input("What is your name? ")
        age = int(input("How old are you? "))


        hours_per_week = int(input("How many hours/week can you commit? "))
        
        if hours_per_week <= 0:
            print("Hours should be greater than zero!")
            continue

        try:
            weeks_to_150 = 150 // hours_per_week
        except ZeroDivisionError:
            print(f"Hours should be greater than zero!")


        print(f"Hey {name}, age {age},")

        if hours_per_week >= 10:
            print(f"Aggressive pace - {weeks_to_150} weeks to 150 hours. You'll move fast.")

        elif hours_per_week >= 5:
            print(f"Steady pace - {weeks_to_150} weeks to 150 hours. Solid and sustainable.")
        else:
            print(f"Light pace - {weeks_to_150} weeks to 150 hours. Slower but consistency wins long-term.")
            
        again = input("Run again? (y/n)")
        if again.lower() != "y":
            print(f'Thanks! Come back soon')
            break

   
