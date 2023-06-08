import uuid

class Task:
    def __init__(self, title, description, due_date, status, id=None):
        self.id = id or str(uuid.uuid4())  # Generate a unique ID if not provided
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'due_date': self.due_date,
            'status': self.status
        }
