from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()
@app.get("/")
def read_root():
    return {'data': {'name':'nitin'}}

# @app.get('/blog')
# def about(limit , publised:bool):
#     if publised:
#         return {'data': f'{limit} publised blog' }
#     else :
#         return {'data': f'{limit} not publised blog'}

# you can pass default value 
@app.get('/blog')
def about(limit  = 10, publised:bool = True , sort : Optional[str] =None ):
    if publised:
        return {'data': f'{limit} publised blog' }
    else :
        return {'data': f'{limit} not publised blog'}


@app.get('/blog/unpublished')
def unpublished():
    return{'data':'all unpublished blogs'}

# @app.get('/blog/{id}')
# def show(id:int):
#     return {'data':id}

class Blog(BaseModel):
    title : str
    body : str
    publised : Optional[bool]

@app.post('/blog')
def create_blog(blog : Blog):
    # return blog
    return {'data': f'Blog is created with title as {blog.title} and in blog the value is {blog.body}'}