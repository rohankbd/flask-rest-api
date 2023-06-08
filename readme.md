# Flask REST API
This is a RESTful API for managing tasks using Python and Flask.

## Prerequisites

- Python 3.9 or higher
- pip package manager

## Getting Started

Follow the steps below to set up and run the Flask application locally.

### 1. Clone the repository

git clone [https://github.com/your-username/flask-task-manager.git]

### 2. Set up a virtual environment (optional)

It's recommended to create a virtual environment for the project to keep the dependencies isolated. To create a virtual environment, run the following command:

python3 -m venv venv

Activate the virtual environment:

- On macOS and Linux:
source venv/bin/activate

- On Windows:
venv\Scripts\activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Run the application

flask run --debug

The Flask application should now be running locally at `http://localhost:5000`.

## API Documentation

The following endpoints are available:

- **Create a new task:** `POST /tasks`
- **Retrieve a single task by ID:** `GET /tasks/<task_id>`
- **Update an existing task:** `PUT /tasks/<task_id>`
- **Delete a task:** `DELETE /tasks/<task_id>`
- **List all tasks:** `GET /tasks`

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
