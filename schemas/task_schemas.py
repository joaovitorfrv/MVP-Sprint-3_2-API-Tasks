from pydantic import BaseModel, Field
from typing import List

from model.task_model import Task

class TaskSchema(BaseModel):
    id:int = 1
    name:str = 'Finalizar MVP'
    priority:int = 5
    done:bool = True

class TaskViewSchema(BaseModel):
    id:int = 1
    name:str = 'Finalizar MVP'
    priority:int = 5
    done:bool = False

class TaskPostSchema(BaseModel):
    name: str = Field(..., max_length=200,description='Nome da tarefa')
    priority:int = Field(..., description='Prioridade da tarefa medida de 1 a 5.')

class TaskUpdateSchema(BaseModel):
    """Schema para atualização de uma task"""
    name: str = Field(None, max_length=200,description='Nome da tarefas')
    priority:int = Field(None, description='Prioridade da tarefa medida de 1 a 5.')
    done: bool = Field(..., examples=False, description='Tarefa ja foi finalizada? True = Sim, False = Não.')

class TaskSearchForId(BaseModel):
    id:int = '1'

class TasksListSchema(BaseModel):
    tasks:List[TaskViewSchema]

class TaskDelSchema(BaseModel):
    message:str
    id:int

# Representação das tarefas em lista
def show_tasks(tasks: List[Task]):
    result = []
    for task in tasks:
        result.append({
            'id':task.id,
            'name':task.name,
            'priority':task.priority,
            'done':task.done
        })
    return {'tasks':result}, 200


def show_task(task: Task):
    return {
        'id':task.id,
        'name':task.name,
        'priority':task.priority,
        'done':task.done
    }