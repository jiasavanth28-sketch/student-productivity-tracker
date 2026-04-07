from scheduler import create_schedule

def main():
    print("Welcome to Student Productivity Tracker")

    subjects = []
    n = int(input("Enter number of subjects: "))

    for i in range(n):
        name = input("Subject name: ")
        days = int(input("Days left until exam: "))
        difficulty = int(input("Difficulty (1-5): "))
        subjects.append((name, days, difficulty))

    schedule = create_schedule(subjects)

    print("\nRecommended Study Plan:")
    for item in schedule:
        print(f"{item[0]} → Priority Score: {item[1]}")

if __name__ == "__main__":
    main()
