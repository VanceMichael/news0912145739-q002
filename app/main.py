from fastapi import FastAPI

app = FastAPI(title="赛事成绩归档")

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
