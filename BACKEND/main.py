from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
# from model import Todo

# from database import (
#     fetch_one_todo,
#     fetch_all_todos,
#     create_todo,
#     update_todo,
#     remove_todo,
# )

# an HTTP-specific exception class  to generate exception information


app = FastAPI()

origins = [
    "http://localhost:3000",
]

# what is a middleware? 
# software that acts as a bridge between an operating system or database and applications, especially on a network.

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True, 
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():        
    return {"ping":"pomg"}

@app.get("/api/todo")
async def get_todo():
    return 1

@app.get("/api/todo{id}")
async def get_todo_by_id(id):
    return 1

@app.post("/api/todo")
async def post_todo(todo):
    return 1

@app.put("/api/todo{id}")
async def put_todo(id, data):
    return 1

@app.delete("/api/todo{id}")
async def delete_todo(id, data):
    return 1