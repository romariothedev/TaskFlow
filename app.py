from flask import Flask, render_template, request, redirect, url_for, flash
from database import get_db, init_db

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.update(
        SECRET_KEY="taskflow-dev-key",
        DATABASE="taskflow.db",
    )
    if test_config:
        app.config.update(test_config)

    os_path = app.config["DATABASE"]
    init_db(os_path)

    @app.route("/")
    def index():
        db = get_db(app.config["DATABASE"])
        tasks = db.execute("SELECT * FROM tasks ORDER BY id DESC").fetchall()
        return render_template("index.html", tasks=tasks)

    @app.route("/tasks", methods=["POST"])
    def create_task():
        title = request.form.get("title", "").strip()
        description = request.form.get("description", "").strip()
        if not title:
            flash("O título da tarefa é obrigatório.", "error")
            return redirect(url_for("index"))
        db = get_db(app.config["DATABASE"])
        db.execute(
            "INSERT INTO tasks (title, description, status) VALUES (?, ?, ?)",
            (title, description, "A Fazer"),
        )
        db.commit()
        flash("Tarefa criada com sucesso!", "success")
        return redirect(url_for("index"))

    @app.route("/tasks/<int:task_id>/status", methods=["POST"])
    def update_status(task_id):
        status = request.form.get("status")
        if status not in {"A Fazer", "Em Progresso", "Concluído"}:
            flash("Status inválido.", "error")
            return redirect(url_for("index"))
        db = get_db(app.config["DATABASE"])
        db.execute("UPDATE tasks SET status = ? WHERE id = ?", (status, task_id))
        db.commit()
        return redirect(url_for("index"))

    @app.route("/tasks/<int:task_id>/delete", methods=["POST"])
    def delete_task(task_id):
        db = get_db(app.config["DATABASE"])
        db.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        db.commit()
        flash("Tarefa excluída.", "success")
        return redirect(url_for("index"))

    return app

if __name__ == "__main__":
    import os
    app = create_app()
    app.run(debug=True)
