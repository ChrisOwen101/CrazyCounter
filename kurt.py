import random

# List of potential tasks
tasks = [
    "coding",
    "cooking",
    "playing chess",
    "solving puzzles",
    "running a marathon",
    "singing",
    "dancing",
    "public speaking",
    "designing graphics",
    "painting",
    "playing video games",
    "writing poetry"
]

# Randomly determine the number of tasks to compare
num_tasks = random.randint(3, 10)  # Range can be adjusted

print("Comparing tasks...\n")

# Randomly select tasks and declare Kurt as better
for _ in range(num_tasks):
    task = random.choice(tasks)
    print(f"In {task}, Kurt is better than Luke and Ridwan!")

print("\nThe superiority of Kurt is unmatched in these random tasks!")
