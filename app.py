from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

# Data storage: in-memory list
tasks = []

# Function to save a task
def save_task(task):
    tasks.append(task)

# Function to retrieve a task by ID
def get_task(task_id):
    for task in tasks:
        if task.id == task_id:
            return task
    return None

# Function to update a task
def update_task(task_id, updated_task):
    for i, task in enumerate(tasks):
        if task['id'] == task_id:
            tasks[i] = updated_task
            return True
    return False

# Function to delete a task
def delete_task(task_id):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            del tasks[i]
            return True
    return False

# Function to list all tasks
def list_tasks():
    return tasks


# Routes

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    due_date = data.get('due_date')
    status = data.get('status')

    new_task = Task(title, description, due_date, status)
    tasks.append(new_task)

    return jsonify({'message': 'Task created successfully', 'task': new_task.to_dict()}), 201

@app.route('/tasks/<task_id>', methods=['GET'])
def get_task_by_id(task_id):
    task = get_task(task_id)
    if task:
        return jsonify(task.to_dict())
    else:
        return jsonify({'error': 'Task not found'}), 404

@app.route('/tasks/<task_id>', methods=['PUT'])
def update_task_by_id(task_id):
    task = get_task(task_id)
    if task:
        data = request.json
        task.title = data['title']
        task.description = data['description']
        task.due_date = data['due_date']
        task.status = data['status']
        # Optionally, you can save the updated task to a database or storage
        # task.save() or db.session.commit() depending on your setup
        return jsonify({'message': 'Task updated successfully'})
    else:
        return jsonify({'error': 'Task not found'})

@app.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task_by_id(task_id):
    if delete_task(task_id):
        return jsonify({'message': 'Task deleted successfully'})
    else:
        return jsonify({'error': 'Task not found'}), 404

@app.route('/tasks', methods=['GET'])
def list_all_tasks():
    return jsonify([task.to_dict() for task in list_tasks()])
