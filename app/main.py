from fastapi import FastAPI
import routes

app = FastAPI(title="Employee App")

@app.get("/")
def root():
    return {"status": "ok", "message": "FastAPI is running"}

app.include_router(routes.router)
