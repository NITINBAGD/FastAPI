from fastapi import FastAPI

app = FastAPI()

@app.get('/users')
def read_users():
    return ['Rick' , 'Morty']

@app.get('/users')
def read_users2():
    return ['nitin' , 'bagde']