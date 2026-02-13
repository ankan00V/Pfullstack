from fastapi import FastAPI,status

app = FastAPI(title='Abir')

@app.post('/',tags=['main'],status_code=status.HTTP_404_NOT_FOUND)
def indexPostView(data:str):
    return {
        "msg" : data
    }

@app.get('/',tags=['main'],status_code=status.HTTP_404_NOT_FOUND)
def indexRecieve(data:str):
    return {
        "msg" : data
    }

# @app.get('/update',tags=['main'])
# def updateView():
#     return {
#         "msg" : 'Hello Bharat'
#     }
