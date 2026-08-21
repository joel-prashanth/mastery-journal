from datetime import date

def log_study_session(sessions_logged: list) -> None:
    
    hours_per_week = int(input("How many hours have you studied this week? "))
    
    sessions_logged.append(hours_per_week)
    
    total = sum(sessions_logged)
    print(f"Logged {hours_per_week}h. Total across {len(sessions_logged)} sessions: {total}h.")
    

def pace_check() -> None:
    name = input("What is your name? ")
    age = int(input("How old are you? "))
    hours_per_week = int(input("How many hours per week can you commit? "))
    
    if hours_per_week <= 0:
        print(f"Hours should be greater than 0!")
        return
    
    weeks_to_150 = 150 // hours_per_week
    
    print(f"Hey {name}, age {age},")
    
    if hours_per_week >= 10:
        print(f"Aggressive pace - {weeks_to_150} weeks to 150 hours. You'll move fast.")
    elif(hours_per_week >= 5):
        print(f"Steady pace - {weeks_to_150} weels to 150 hours. Solid and sustainable.")
    else:
        print(f"Light pace - {weeks_to_150} weeks to 150 hours. Slower but consistency matters in the long run.")
    
def main() -> None:
    
    sessions_logged = []
    
    while True:
        log_study_session(sessions_logged)
        pace_check()
        
        again = input("Run again? ")
        if(again.lower() != "y"):
            print("Thanks! Come back soon.")
            break
    print(f"\nAll sesisons this run: {sessions_logged}")