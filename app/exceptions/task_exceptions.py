class TaskNotFoundException(Exception):
    def __init__(self):

        self.message = "Task not found"

        super().__init__(self.message)

