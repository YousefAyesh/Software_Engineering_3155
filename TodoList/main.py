from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated, Optional
import models
from database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session

# Initialize FastAPI application
app = FastAPI()

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Database dependency
db_dependency = Annotated[Session, Depends(get_db)]


# Pydantic model for creating todos (without id)
class TodoCreate(BaseModel):
    task_body: str
    due_day: int
    due_month: str
    due_year: int


# Pydantic model for todo responses (with id)
class TodoBase(BaseModel):
    id: int
    task_body: str
    due_day: int
    due_month: str
    due_year: int


# Pydantic model for updating todos
class TodoUpdate(BaseModel):
    task_body: Optional[str] = None
    due_day: Optional[int] = None
    due_month: Optional[str] = None
    due_year: Optional[int] = None


# CREATE - Post a new todo
@app.post("/todos/", status_code=status.HTTP_201_CREATED)
async def create_todo(todo: TodoCreate, db: db_dependency):
    db_todo = models.Todo(
        task_body=todo.task_body,
        due_day=todo.due_day,
        due_month=todo.due_month,
        due_year=todo.due_year
    )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return {"detail": "Todo added successfully", "id": db_todo.id}


# READ - Get all todos
@app.get("/todos/", status_code=status.HTTP_200_OK)
async def get_todos(db: db_dependency):
    return db.query(models.Todo).all()


# READ - Get a single todo by ID
@app.get("/todos/{todo_id}", response_model=TodoBase, status_code=status.HTTP_200_OK)
async def get_todo(todo_id: int, db: db_dependency):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    return db_todo


# UPDATE - Update a todo
@app.put("/todos/{todo_id}", response_model=TodoBase, status_code=status.HTTP_200_OK)
async def update_todo(todo_id: int, todo_request: TodoBase, db: db_dependency):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")

    update_data = todo_request.model_dump(exclude_unset=True)

    # Update the database record with the new data
    for key, value in update_data.items():
        setattr(db_todo, key, value)

    db.commit()
    return db_todo


# DELETE - Delete a todo
@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(todo_id: int, db: db_dependency):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")

    db.delete(db_todo)
    db.commit()
    return None


# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Todo API is running"}