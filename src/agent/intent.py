def understand_intent(user_input):
    """
    Basic intent understanding for NOVA.
    """

    text = user_input.lower()

    if "exam" in text or "study" in text:
        return {
            "intent": "study_planning",
            "message": "The user needs help with studying or exam preparation."
        }

    if "task" in text or "assignment" in text:
        return {
            "intent": "task_management",
            "message": "The user needs help managing tasks."
        }

    if "schedule" in text or "plan" in text:
        return {
            "intent": "planning",
            "message": "The user wants help creating a plan."
        }

    return {
        "intent": "general",
        "message": "The user's intent could not be identified yet."
    }