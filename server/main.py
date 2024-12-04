import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:4000",
]
hosts = ["localhost", "127.0.0.1"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=hosts
)


@app.get("/")
async def root():
    return {"message": "hi"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=4000, reload=True)
