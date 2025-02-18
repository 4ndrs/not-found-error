from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello from Python!"}


@app.get("/api/test")
def test_endpoint():
    return {"message": "This is a test endpoint from FastAPI"}


@app.get("/api/404-test")
def test_404():
    return {"error": "This is a test for 404 handling"}
