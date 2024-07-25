# 데이터베이스 연결, 세션 설정
'''
데이터베이스 세션이란?
애플리케이션과 데이터베이스 간의 일시적인 연결. 세션을 통해 데이터베이스에 쿼리를 보내고 데이터를 삽입, 업데이트, 삭제할 수 있으며 작업이 완료되면 세션을 종료하여 리소스를 해제한다. 

세션의 역할

상태 관리:
데이터베이스와의 연결이 열려 있는 동안 상태를 유지하고, 작업이 완료되면 연결을 닫는다.

트랜잭션 관리:
데이터베이스의 일련의 작업을 하나의 단위로 묶어 처리함. 세션은 트랜잭션을 시작하고, 필요한 경우 커밋(commit)하거나 롤백(rollback)함. 

쿼리 실행:
데이터베이스에 쿼리를 실행하고 결과를 반환받음. 이를 통해 데이터베이스의 데이터를 읽고 쓸 수 있음.
'''


from sqlalchemy import create_engine #create_engine 은 sqlalchemy의 엔진을 생성. orm과 데이터베이스 간의 연결을 관리하며 sql 쿼리를 데이터베이스로 전달하는 역할을 함. 
from sqlalchemy.orm import sessionmaker #객체를 데이터베이스에 추가 수정 삭제하는 역할을 함. 
from sqlalchemy.ext.declarative import declarative_base #orm 의 기본 클래스인 base를 생성함. 이 base를 상속받아서 각 데이터베이스에 해당하는 orm 모델 클래스를 정의함. 
from dotenv import load_dotenv
import os

# 환경 변수 로드
load_dotenv()

URL_DATABASE = os.getenv('URL_DATABASE')

engine = create_engine(URL_DATABASE) #db연결을 위한 엔진 객체를 생성. db연결과 쿼리를 db로 전달하는 역할을 함. 

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine) #sessionlocal이라는 이름으로 각 데이터베이스의 세션 인스턴스를 생성하는 데 사용됨. 자동 커밋 = false, 자동 플러시 =false 그리고 bind = engine 을 통해 이 세션이 특정 엔진에 연결되도록 설정. 

Base = declarative_base() #base 라는 기본 클래스를 생성. 이 클래스를 상속받아서 각 데이터베이스에 해당하는 orm 모델 클래스를 정의할 수 있음. 

def get_db():
    db = SessionLocal() # 새 데이터베이스 세션을 생성
    try:
        yield db  # 데이터베이스 세션을 클라이언트에게 반환
    finally:
        db.close()  # 세션을 닫기
