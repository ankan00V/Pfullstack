from fastapi import FastAPI

app = FastAPI(title='Abir')

@app.get('/',tags=['main'])
def indexView():
    return {
        "msg" : 'Hello India'
    }

@app.get('/update',tags=['main'])
def updateView():
    return {
        "msg" : 'Hello Bharat'
    }
