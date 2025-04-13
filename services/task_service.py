from sqlalchemy.exc import IntegrityError
from model import Session, Task
from schemas import show_task, show_tasks

def add_task_service(form):
    """
    Adicionar uma nova tarefa à lista.
    """
    task = Task(
        name=form.name,
        priority=form.priority,
        done=False
    )

    try:
        session = Session()
        session.add(task)
        session.commit()
        return show_task(task), 200
    except IntegrityError:
        error_msg = 'Já existe uma tarefa com este nome'
        return {'message': error_msg}, 409
    except Exception:
        error_msg = 'Não foi possível adicionar a tarefa.'
        return {'message': error_msg}, 400

def get_tasks_service():
    """
    Retornar lista com TODAS as tarefas.
    """
    session = Session()
    tasks = session.query(Task).all()

    return show_tasks(tasks)

def get_task_service(query):
    """
    Retornar informações de UMA tarefa a partir do seu ID.
    """
    session = Session()
    task = session.query(Task).filter(Task.id == query.id).first()
    return show_task(task) if task else {'message': 'Task inexistente'}, 404

def delete_task_service(query):
    """
    Deletar uma tarefa a partir do ID.
    """
    session = Session()
    count = session.query(Task).filter(Task.id == query.id).delete()
    session.commit()
    return {'message': 'Task removida', 'id': query.id} if count else {'message': 'Task não encontrada'}, 404

def update_task_service(query, form):
    """
    Atualizar informações de uma tarefa a partir do ID.
    """
    session = Session()
    task = session.query(Task).filter(Task.id == query.id).first()
    
    if not task:
        return {'message': 'Task não encontrada'}, 404

    if form.name is not None:
        task.name = form.name
    if form.priority is not None:
        task.priority = form.priority

    task.done = form.done

    try:
        session.commit()
        return show_task(task), 200
    except Exception:
        error_msg = 'Não foi possível atualizar esta tarefa'
        return {'message': error_msg}, 400
