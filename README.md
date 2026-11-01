# Todo List

A task management web application built with Python and Flask. Users can create, edit, complete, and delete tasks, with options to filter tasks by status and track their progress through a simple dashboard.

## Screenshots

<img width="1470" height="831" alt="Screenshot 2026-11-01 at 1 37 18 PM" src="https://github.com/user-attachments/assets/3baab4e0-d1e8-4c75-88c0-86fcbe658489" />

<img width="1469" height="833" alt="Screenshot 2026-11-01 at 1 37 34 PM" src="https://github.com/user-attachments/assets/e9b7841a-af4f-4be2-b44e-c4146bf88928" />

<img width="1469" height="844" alt="Screenshot 2026-11-01 at 1 38 00 PM" src="https://github.com/user-attachments/assets/035adb32-3da1-4f7a-b186-68352be7375f" />


## Features

- **Add Tasks:** Create new tasks.
- **Edit Tasks:** Update existing task descriptions.
- **Complete Tasks:** Mark tasks as completed or undo completion.
- **Delete Tasks:** Remove tasks with a confirmation prompt.
- **Filter Tasks:** View all, pending, or completed tasks.
- **Task Dashboard:** Track total, pending, and completed tasks.
- **Database Storage:** Store tasks using SQLite.

## Technologies

- Python
- Flask
- Flask-SQLAlchemy
- SQLAlchemy
- SQLite
- HTML
- Bootstrap 5
- Jinja2

## Installation and Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/gustavodev6331/todo-list.git
   ```

2. Navigate to the project directory:

   ```bash
   cd todo-list
   ```

3. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

4. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Run the application:

   ```bash
   python main.py
   ```

6. Open your browser and visit:

   ```text
   http://127.0.0.1:5000
   ```

## Project Structure

```text
todo-list/
│
├── main.py
├── requirements.txt
├── templates/
│   ├── index.html
│   └── edit.html
├── static/
└── .gitignore
```

## Database

The application uses SQLite with Flask-SQLAlchemy to manage task records. The database is automatically created when the application starts.
