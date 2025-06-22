class Task:
    def __init__(self, id, title, priority, status="pending"):
        self.id = id
        self.title = title
        self.priority = priority
        self.status = status

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, id, title, priority):
        task = Task(id, title, priority)
        if any(t.id == id for t in self.tasks):
            return False
        self.tasks.append(task)
        return task

    def update_status(self, id, new_status):
        for task in self.tasks:
            if task.id == id:
                task.status = new_status
                return True
        for task in self.tasks:
            task.status = new_status
        return False

    def get_high_priority_tasks(self):
        high_priority = []
        for task in self.tasks:
            if task.priority == "high":
                high_priority.append(task)
            elif task.priority == 1:
                high_priority.append(task)
        return high_priority
