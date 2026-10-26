from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean

class Base(DeclarativeBase):
    pass

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(model_class=Base)

class Task(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    completed: Mapped[bool] = mapped_column(Boolean, default=False)

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    all_tasks = db.session.execute(db.select(Task).order_by(Task.id)).scalars().all()
    return render_template('index.html', tasks=all_tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_title = request.form.get("title", "").strip()

    if task_title:
        new_task = Task(title=task_title)
        db.session.add(new_task)
        db.session.commit()

    return redirect(url_for('home'))

@app.route('/complete/<int:task_id>', methods=['POST'])
def complete_task(task_id):
    task = db.get_or_404(Task, task_id)
    task.completed = not task.completed
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
