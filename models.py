# 데이터베이스 테이블에 매핑되는 ORM 모델을 정의
'''
ORM 모델이란?
ORM(Object-Relational Mapping, 객체-관계 매핑)은 객체 지향 프로그래밍 언어를 사용하여 관계형 데이터베이스를 다루기 위한 기술. ORM은 데이터베이스의 테이블을 클래스 형태로 매핑하여, 데이터베이스와 상호작용할 때 SQL 쿼리 대신 객체 지향 프로그래밍 언어의 객체를 사용할 수 있게 해 줌. (CREATE ALTER 이런 게 sql 쿼리) 이를 통해 개발자는 데이터베이스와의 상호작용을 더욱 직관적이고 쉽게 할 수 있게 됨!
SQLAlchemy는 Python에서 널리 사용되는 ORM 라이브러리로, 관계형 데이터베이스와 상호작용하기 위해 사용된다.
'''

from sqlalchemy import Boolean, Column, Integer, String
from database import Base

# User 테이블을 정의하는 클래스
class User(Base):
    __tablename__ = 'users'  #매핑될 데이터베이스 테이블 이름을 지정하고 

    id = Column(Integer, primary_key=True, index=True)  # 사용자 ID(정수형 ID)로 기본 키를 생성하고, 인덱스 기능을 true 로 하여 더 빠르게 작업하도록 함. 
    username = Column(String(50), unique=True)  # 최대 50자 길이의 문자열로 사용자 이름을 저장하며, 중복 불가하다. 

# Post 테이블을 정의하는 클래스입니다.
class Post(Base):
    __tablename__ = 'posts'  # 테이블 이름을 지정. 항상 이런 식으로 테이블을 만들고 테이블 이름을 지정함. 

    id = Column(Integer, primary_key=True, index=True)  # 게시물 ID, 기본 키 속성
    title = Column(String(50))  # 최대 50자 길이의 문자열로 게시물 제목을 저장
    content = Column(String(100))  # 최대 100자 길이의 문자열로 게시물 내용을 저장
    user_id = Column(Integer)  # 게시물을 작성한 사용자 ID 저장



'''시각화:

User
+---------+--------------+-------------+
| 컬럼 이름 | 데이터 타입    | 속성          |
+---------+--------------+-------------+
| id      | Integer      | Primary Key, Index |
| username| String(50)   | Unique       |
+---------+--------------+-------------+

Post
+---------+--------------+-------------+
| 컬럼 이름 | 데이터 타입    | 속성          |
+---------+--------------+-------------+
| id      | Integer      | Primary Key, Index |
| title   | String(50)   |               |
| content | String(100)  |               |
| user_id | Integer      | Foreign Key  |
+---------+--------------+-------------+

'''