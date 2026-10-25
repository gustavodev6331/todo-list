from flask import Flask, render_template
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
    db.session.execute(db.select(Task).order_by(Task.id)).scalars().all()
    return render_template('home.html', tasks=all_tasks)

if __name__ == '__main__':
    app.run(debug=True)
