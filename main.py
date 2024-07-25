from fastapi import FastAPI, HTTPException, Depends, status #exception으로 특정 조건에서 클라이언트에게 http오류를 반환할 수 있음. status 로는 https상태 코드를 정의함!
from pydantic import BaseModel
from typing import Annotated # 각 메타데이터를 타입 힌트에 포함할 수 있게 해 줌. 
import models 
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from routers import user_routes, post_routes

app = FastAPI()
models.Base.metadata.create_all(bind = engine)

app.include_router(user_routes.router, prefix="/users", tags=["users"])
app.include_router(post_routes.router, prefix="/posts", tags=["posts"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}

