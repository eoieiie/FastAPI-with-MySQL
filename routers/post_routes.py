from fastapi import APIRouter, HTTPException, Depends, status
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import get_db
import models

router = APIRouter()

class PostBase(BaseModel):
    title: str
    content: str
    user_id: int

@router.post("/posts/", status_code=status.HTTP_201_CREATED)
async def create_post(post: PostBase, db: Session = Depends(get_db)):
    db_post = models.Post(**post.dict())
    db.add(db_post)
    db.commit()
    return db_post

@router.get("/posts/{post_id}", status_code=status.HTTP_200_OK)
async def read_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if post is None:
        raise HTTPException(status_code=404, detail='Post not found')
    return post

@router.delete("/posts/{post_id}", status_code=status.HTTP_200_OK)
async def delete_post(post_id: int, db: Session = Depends(get_db)):
    db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if db_post is None:
        raise HTTPException(status_code=404, detail='Post not found')
    db.delete(db_post)
    db.commit()


# @app.post("/posts/", status_code=status.HTTP_201_CREATED)
# async def create_post(post: PostBase, db: db_dependency): # PostBase 모델의 데이터를 받아온다. 
#     db_post = models.Post(**post.dict()) # 딕셔너리의 키-값 쌍을 인자로 넘겨 models.Post 클래스의 인스턴스 생성
#     db.add(db_post) # 생성된 db_post 객체를 데이터베이스 세션에 추가
#     db.commit() # 변경 사항 커밋하여 실제 데이터베이스에 반영


# @app.get("/posts/{post_id}", status_code=status.HTTP_200_OK)
# async def read_post(post_id: int, db: db_dependency): # 게시물 ID로 데이터베이스에서 게시물 조회
#     post = db.query(models.Post).filter(models.Post.id == post_id).first() # 쿼리 시작, 필터링, 조건에 맞는 첫 번째 레코드 반환
#     if post is None:
#         raise HTTPException(status_code=404, detail='Post was not found') # 예외 처리
#     return post


# @app.delete("/posts/{post_id}", status_code=status.HTTP_200_OK)
# async def delete_post(post_id: int, db: db_dependency): # 전달된 post_id에 해당하는 게시물 삭제
#     db_post = db.query(models.Post).filter(models.Post.id == post_id).first() # 쿼리 시작, 필터링, 첫 번째 레코드 반환
#     if db_post is None:
#         raise HTTPException(status_code=404, detail='Post was not found') # 예외 처리
#     db.delete(db_post) # 조회된 게시물 객체를 데이터베이스 세션에서 삭제
#     db.commit() # 변경사항 커밋