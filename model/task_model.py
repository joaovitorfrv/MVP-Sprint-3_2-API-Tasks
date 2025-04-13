from sqlalchemy import Column, Integer, String, Boolean, DateTime, UniqueConstraint
from typing import Union
from datetime import datetime

from model import Base



# Cria classe da task
class Task(Base):
    # Define o nome da table
    __tablename__ = 'task_list'

    # Cria colunas: id, task, done, prioriy
    id = Column('task_id', Integer, primary_key=True)
    name = Column('task_name', String(100))
    priority = Column('task_priority', Integer)
    done = Column('task_status', Boolean)
    date = Column('insert_date', DateTime, default=datetime.now)

    #
    __table_args__ = (UniqueConstraint('task_name', name='task_unique_name'),)

    def __init__(self, name:str, priority:int, done:Boolean, data_insercao:Union[DateTime, None] = None):
        self.name = name
        self.priority = priority
        self.done = done

        if data_insercao:
            self.data_insercao = data_insercao

    def to_dict(self):

        return {
            'id':self.id,
            'name':self.name,
            'priority': self.priority,
            'done': self.done,
            'data_insercao': self.data_insercao
        }

    def __repr__(self):
        return f'Task (id={self.id}), name={self.name}, priority={self.priority}, done={self.done}'