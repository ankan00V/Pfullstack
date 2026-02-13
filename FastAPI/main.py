from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def LPU():
    return("Hello LPU")

@app.get("/about")
def about():
    return("LPU is Good")

@app.get("/links")
def links():
    return("Links are working")
