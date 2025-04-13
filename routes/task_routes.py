from flask_openapi3 import Tag
from flask import jsonify
from schemas import *
from services.task_service import (
    add_task_service,
    get_tasks_service,
    get_task_service,
    delete_task_service,
    update_task_service
)

task_tag = Tag(name="Task", description="Adiciona, Visualiza e Remove uma task.")

def init_task_routes(app):
    @app.post('/api/task', tags=[task_tag],
              responses={'200': TaskViewSchema, '409': ErrorSchema, '400': ErrorSchema})
    def add_task(form: TaskPostSchema):
        """
        POST: Adicionar uma nova tarefa à lista.
        """
        return add_task_service(form)

    @app.get('/api/tasks', tags=[task_tag],
              responses={'200': TasksListSchema, '409': ErrorSchema, '404': ErrorSchema})
    def get_tasks():
        """
        GET: Retornar lista com TODAS as tarefas.
        """
        return get_tasks_service()

    @app.get('/api/task', tags=[task_tag],
              responses={'200': TaskViewSchema, '404': ErrorSchema})
    def get_task(query: TaskSearchForId):
        """
        GET: Retornar informações de UMA tarefa.
        """
        return get_task_service(query)

    @app.delete('/api/task', tags=[task_tag],
               responses={'200': TaskDelSchema, '404': ErrorSchema})
    def del_task(query: TaskSearchForId):
        """
        DELETE: Remover uma tarefa.
        """
        return delete_task_service(query)

    @app.put('/api/task', tags=[task_tag],
              responses={'200': TaskSchema, '404': ErrorSchema, '422': ErrorSchema})
    def update_task(query: TaskSearchForId, form: TaskUpdateSchema):
        """
        PUT: Atualizar informações de uma tarefa.
        """
        return update_task_service(query, form)