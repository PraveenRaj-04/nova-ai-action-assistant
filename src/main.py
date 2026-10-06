from agent.intent import understand_intent
from agent.task_extractor import extract_tasks
from agent.planner import create_plan
from agent.memory import NovaMemory


def process_request(user_input, memory):
    """
    Process one user request using NOVA's
    intent, task extraction, planning, and memory systems.
    """

    text = user_input.lower()

    # ==========================================
    # MEMORY: CHECK DEADLINE
    # ==========================================

    if "deadline" in text:

        deadline = memory.get_deadline()

        if deadline:
            print(f"\nNOVA: Your current deadline is {deadline}.")
        else:
            print("\nNOVA: I don't have a deadline stored yet.")

        return

    # ==========================================
    # MEMORY: CHECK TASKS
    # ==========================================

    if "what tasks" in text or "my tasks" in text:

        tasks = memory.get_tasks()

        if tasks:

            print("\nNOVA: Your current tasks are:")

            for index, task in enumerate(tasks, start=1):

                print(
                    f"{index}. {task['task']} "
                    f"(Priority: {task['priority']})"
                )

        else:

            print("\nNOVA: I don't have any tasks stored yet.")

        return

    # ==========================================
    # STEP 1: UNDERSTAND INTENT
    # ==========================================

    intent_result = understand_intent(user_input)

    # ==========================================
    # STEP 2: EXTRACT TASKS
    # ==========================================

    task_result = extract_tasks(user_input)

    # ==========================================
    # STEP 3: STORE INFORMATION IN MEMORY
    # ==========================================

    memory.remember_intent(
        intent_result["intent"]
    )

    if task_result["tasks"]:

        memory.remember_tasks(
            task_result["tasks"]
        )

    if task_result["deadline"]:

        memory.remember_deadline(
            task_result["deadline"]
        )

    # ==========================================
    # STEP 4: DISPLAY INTENT
    # ==========================================

    print("\nNOVA:")
    print(f"Intent: {intent_result['intent']}")

    # ==========================================
    # STEP 5: DISPLAY TASKS
    # ==========================================

    if task_result["tasks"]:

        print("\nTasks:")

        for index, task in enumerate(
            task_result["tasks"],
            start=1
        ):

            print(
                f"{index}. {task['task']} "
                f"(Priority: {task['priority']})"
            )

    else:

        print("\nNo specific tasks identified.")

    # ==========================================
    # STEP 6: DISPLAY DEADLINE
    # ==========================================

    if task_result["deadline"]:

        print(
            f"\nDeadline: "
            f"{task_result['deadline']}"
        )

    # ==========================================
    # STEP 7: CREATE PLAN
    # ==========================================

    plan = create_plan(
        task_result["tasks"]
    )

    if plan:

        print("\nNOVA PLAN")
        print("-----------------------------------")

        total_time = 0

        for index, item in enumerate(
            plan,
            start=1
        ):

            print(
                f"{index}. {item['task']}"
                f" | Priority: {item['priority']}"
                f" | Time: {item['duration']} minutes"
            )

            total_time += item["duration"]

        print("-----------------------------------")

        print(
            f"Total planned time: "
            f"{total_time} minutes"
        )


def main():
    """
    Main NOVA application.
    """

    print("===================================")
    print("       NOVA AI ACTION ASSISTANT")
    print("===================================")

    print("\nNOVA is ready.")
    print("Type 'exit' to stop.\n")

    # ==========================================
    # CREATE MEMORY
    # ==========================================

    memory = NovaMemory()

    # ==========================================
    # CONVERSATION LOOP
    # ==========================================

    while True:

        user_input = input("You: ").strip()

        # Ignore empty input
        if not user_input:
            continue

        # ======================================
        # EXIT COMMAND
        # ======================================

        if user_input.lower() in [
            "exit",
            "quit",
            "bye"
        ]:

            print("\nNOVA: Goodbye! 👋")
            break

        # ======================================
        # PROCESS USER REQUEST
        # ======================================

        process_request(
            user_input,
            memory
        )


# ==============================================
# PROGRAM ENTRY POINT
# ==============================================

if __name__ == "__main__":
    main()