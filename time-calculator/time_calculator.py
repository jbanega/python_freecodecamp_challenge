def add_time(start, duration, starting_Day=None):

    days_of_Week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Extracting data
    start_Time, initial_system_hour = start.split()
    hours, minutes = start_Time.split(":")
    add_hours, add_minutes = duration.split(":")

    if starting_Day != None:
        starting_Day = starting_Day.strip().capitalize()
        index_Day_in_list = days_of_Week.index(starting_Day)

    ending_hour = int(hours) + int(add_hours)
    ending_minutes = int(minutes) + int(add_minutes)

    # Formatting the hour
    if initial_system_hour == "PM":
        ending_hour += 12

    if ending_minutes >= 60:
        ending_minutes -= 60
        ending_hour += 1
    
    number_of_Days = round(ending_hour / 24)

    if ending_hour < 24:
        number_of_Days = 0
    elif ending_hour >= 24:
        ending_hour -= number_of_Days * 24

    if ending_hour == 0:
        system_hour = "AM"
        ending_hour += 12
    elif ending_hour > 0 and ending_hour < 12:
        system_hour = "AM"
    else:
        system_hour = "PM"
        ending_hour -= 12
        if ending_hour == 0:
            ending_hour = 12

    if starting_Day != None:
        days_of_Week += round(number_of_Days / len(days_of_Week)) * days_of_Week
        final_Day = days_of_Week[index_Day_in_list + number_of_Days]

    result = f"{ending_hour:1d}:{ending_minutes:02d} {system_hour}"

    # Displaying result
    if (number_of_Days == 0) and (starting_Day == None):
        new_time = result
    elif (number_of_Days == 0) and (starting_Day != None):
        new_time = result + f", {final_Day}"
    elif (number_of_Days == 1) and (starting_Day == None):
        new_time = result + " (next day)"
    elif (number_of_Days >= 1) and (starting_Day != None):
        if number_of_Days == 1:
            new_time = result + f", {final_Day} (next day)"
        else:
            new_time = result + f", {final_Day} ({number_of_Days} days later)"
    else:
        new_time = result + f" ({number_of_Days} days later)"
    
    return new_time


if __name__ == "__main__":
    print(add_time("2:59 AM", "24:00", "saturDay"))