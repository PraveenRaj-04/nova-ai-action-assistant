class NovaMemory:
    """Stores relevant information during a NOVA session."""

    def __init__(self):
        self.tasks = []
        self.last_intent = None
        self.last_deadline = None

    def remember_tasks(self, tasks):
        self.tasks = tasks

    def remember_intent(self, intent):
        self.last_intent = intent

    def remember_deadline(self, deadline):
        self.last_deadline = deadline

    def get_tasks(self):
        return self.tasks

    def get_intent(self):
        return self.last_intent

    def get_deadline(self):
        return self.last_deadline

    def clear(self):
        self.tasks = []
        self.last_intent = None
        self.last_deadline = None