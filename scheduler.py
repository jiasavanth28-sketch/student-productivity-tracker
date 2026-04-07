def create_schedule(subjects):
    schedule = []

    for subject in subjects:
        name, days, difficulty = subject

        # Simple priority logic
        priority = (6 - days) * difficulty

        schedule.append((name, priority))

    # Sort by priority (highest first)
    schedule.sort(key=lambda x: x[1], reverse=True)

    return schedule
