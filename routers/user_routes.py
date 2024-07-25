from fastapi import APIRouter, HTTPException, Depends, status
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import get_db
import models

router = APIRouter()

class UserBase(BaseModel):
    username: str

@router.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserBase, db: Session = Depends(get_db)):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    return db_user

@router.get("/users/{user_id}", status_code=status.HTTP_200_OK)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail='User not found')
    return user


# @app.post("/users/", status_code=status.HTTP_201_CREATED) # 성공적으로 사용자 생성 시, HTTP 상태 코드 201(생성됨)을 반환
# async def create_user(user: UserBase, db: db_dependency): # 비동기 함수, 새로운 사용자를 데이터베이스에 생성, UserBase, db_dependency 설정 
    
#     # models.User(**user.dict()): 딕셔너리의 키-값 쌍을 models.User 클래스의 인스턴스 생성에 사용. 생성하면서 데이터베이스 테이블에 삽입할 준비를 함.
#     db_user = models.User(**user.dict()) # user.dict()는 UserBase 모델의 데이터를 딕셔너리 형태로 변환
#     db.add(db_user) # 새로 생성된 db_user 객체를 데이터베이스 세션에 추가
#     db.commit() # 데이터베이스 세션의 변경 사항을 커밋하여 실제로 데이터베이스에 반영
    

# @app.get("/users/{user_id}", status_code=status.HTTP_200_OK) 
# async def read_user(user_id:int, db: db_dependency): # 비동기 함수, 사용자 조회 함수
#     user = db.query(models.User).filter(models.User.id == user_id).first() # 모든 레코드를 선택하는 쿼리 시작, user 모델의 id가 user_id와 일치하는지 필터링, 첫번째 레코드 반환
#     if user is None:
#         raise HTTPException(status_code=404, detail='User not found') # 조회된 사용자가 없을 경우 예외 발생
#     return user # 조회된 사용자 객체 반환
