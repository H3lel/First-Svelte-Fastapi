from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select

class TasksDb(SQLModel,table=True):
    id : int | None = Field(default=None,primary_key=True , index=True)
    taskName : str = Field(index=True)
    taskContent : str = Field(index=True)