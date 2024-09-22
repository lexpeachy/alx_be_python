# Ask the user to input a task description and save it into a task variable
# Prompt for the task’s priority (high, medium, low) and save it into a priority variable
# In a time_bound variable, Ask if the task is time-bound (yes or no)
task = (input(f"enter your task: "))
priority = (input(f"enter your task priority (high/medium/low): "))
time_bound = (input(f"Is it time-bound? (yes/no) : "))
# Use a Match Case statement to react differently based on the task’s priority.
# Within the Match Case or after, use an if statement to modify the reminder if the task is time-bound.
match priority:
    case "high":
        reminder = f"{task} is a high priority task "
        if time_bound == "yes":
            reminder += "and it requires immediate attention."
        else:
            reminder += "."
    case "medium":
        reminder = f"{task} is a medium priority task "
        if time_bound == "yes":
            reminder += "you should consinder addressing it soon."
        else:
            reminder += "."
    case "low":
        reminder = f"{task} is a low priority task"
        if time_bound == "yes":
            reminder = "and you should consinder doing it when free."
        else:
            reminder += "."
    case _:
        reminder = "you have entered an invalid priority"
print(reminder)