def add_time(start, duration, day_of_week=None):
    # Split the start time into hours, minutes, and seconds
    time_part, period = start.split()
    start_hour, start_minute = map(int, time_part.split(':'))
    duration_hour, duration_minute = map(int, duration.split(':'))
    period = period.upper()

    # Convert start time to 24-hour format for easier calculation
    if period == "PM" and start_hour != 12:
        start_hour += 12
    elif period == "AM" and start_hour == 12:
        start_hour = 0
    
    # Add the duration to the start time
    end_hour = start_hour + duration_hour
    end_minute = start_minute + duration_minute

    # Handle minute overflow
    if end_minute >= 60:
        end_minute -= 60
        end_hour += 1

    # Calculate the number of days passed
    days_passed = end_hour // 24
    end_hour = end_hour % 24

    # Convert back to 12-hour format
    if end_hour >= 12:
        period = "PM"
        if end_hour > 12:
            end_hour -= 12
    else:
        period = "AM"
        if end_hour == 0:
            end_hour = 12

    # Calculate the day of the week if provided
    if day_of_week:
        days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        day_of_week = day_of_week.capitalize()
        start_day_index = days_of_week.index(day_of_week)
        end_day_index = (start_day_index + days_passed) % 7
        end_day = days_of_week[end_day_index]

    # Format the final time
    new_time = f"{end_hour}:{end_minute:02d} {period}"

    if day_of_week:
        new_time += f", {end_day}"
    
    if days_passed == 1:
        new_time += " (next day)"
    elif days_passed > 1:
        new_time += f" ({days_passed} days later)"
    
    return new_time


def main():
    start_time = input("Enter the start time (e.g., '3:30 PM'): ")
    duration_time = input("Enter the duration time (e.g., '2:12'): ")
    day_of_week = input("Enter the starting day of the week (optional, e.g., 'Monday'): ")
    result = add_time(start_time, duration_time, day_of_week if day_of_week else None)
    print("Result:", result)

main()
