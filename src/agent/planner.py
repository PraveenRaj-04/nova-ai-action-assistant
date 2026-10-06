def create_plan(tasks):
    """
    Create a simple priority-based plan.
    """

    priority_order = {
        "High": 1,
        "Medium": 2,
        "Low": 3
    }

    # Sort tasks by priority
    sorted_tasks = sorted(
        tasks,
        key=lambda task: priority_order.get(task["priority"], 4)
    )

    plan = []

    for task in sorted_tasks:

        if task["priority"] == "High":
            duration = 90
        elif task["priority"] == "Medium":
            duration = 30
        else:
            duration = 20

        plan.append({
            "task": task["task"],
            "priority": task["priority"],
            "duration": duration
        })

    return plan