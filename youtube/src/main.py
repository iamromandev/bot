from fastapi import FastAPI

app = FastAPI(
    title="Youtube Bot Service",
    version='0.0.1',
)


@app.get("/")
def read_root():
    return {"Hello": "World"}
