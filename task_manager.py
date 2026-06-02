from datetime import datetime, timedelta
from models import Task, Status, Priority


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    # ---------- CRUD ----------
    def create_task(self, title, description, priority, due_date):
        task = Task(
            id=self.next_id,
            title=title,
            description=description,
            status=Status.TODO,
            priority=Priority(priority),
            due_date=due_date,
            created_at=datetime.now().isoformat()
        )
        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_tasks(self):
        return self.tasks

    def update_status(self, task_id, status):
        task = self._find(task_id)
        if task:
            task.status = Status(status)

    def delete_task(self, task_id):
        self.tasks = [t for t in self.tasks if t.id != task_id]

    # ---------- BUSINESS RULE ----------
    def update_overdue_tasks(self):
        now = datetime.now()

        for task in self.tasks:
            if task.status == Status.DONE:
                continue

            due = datetime.fromisoformat(task.due_date)
            overdue_days = (now - due).days

            if overdue_days > 7 and task.priority != Priority.HIGH:
                task.status = Status.ABANDONED

    # ---------- HELPERS ----------
    def _find(self, task_id):
        return next((t for t in self.tasks if t.id == task_id), None)