def extract_tasks(user_input):
    """
    Extract basic tasks and deadlines from a user's request.
    This is an initial rule-based implementation.
    """

    text = user_input.lower()

    tasks = []
    deadline = None

    # Detect exam-related task
    if "exam" in text:
        tasks.append({
            "task": "Prepare for exam",
            "priority": "High"
        })

    # Detect assignments
    if "assignment" in text:
        if "two" in text or "2" in text:
            tasks.append({
                "task": "Complete assignment 1",
                "priority": "Medium"
            })

            tasks.append({
                "task": "Complete assignment 2",
                "priority": "Medium"
            })

        else:
            tasks.append({
                "task": "Complete assignment",
                "priority": "Medium"
            })

    # Detect deadline
    if "tomorrow" in text:
        deadline = "Tomorrow"

    elif "today" in text:
        deadline = "Today"

    return {
        "tasks": tasks,
        "deadline": deadline
    }