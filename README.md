# FastAPI with MySQL Integration

This project demonstrates how to integrate FastAPI with MySQL using SQLAlchemy. The project includes basic CRUD operations for managing users and posts.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Endpoints](#endpoints)

## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
Create a virtual environment:

sh
코드 복사
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install dependencies:

sh
코드 복사
pip install -r requirements.txt
Install MySQL:
Ensure MySQL is installed and running on your machine. You can download it from MySQL Downloads.

Set up the database:
Create a MySQL database named island_database or use an existing one. Make sure to configure the database credentials in the .env file.

Configuration
Create a .env file in the project root directory and add your database URL:

env
코드 복사
DATABASE_URL=mysql+pymysql://username:password@localhost:3306/island_database
Add the .env file to .gitignore to prevent it from being committed to version control:

plaintext
코드 복사
.env
Usage
Run the application:

sh
코드 복사
uvicorn main:app --reload
Access the API documentation:
Open your browser and go to http://127.0.0.1:8000/docs to view the interactive API documentation provided by Swagger UI.

Project Structure
plaintext
코드 복사
my_fastapi_app/
├── main.py
├── database.py
├── models.py
├── .env
├── .env.example
├── .gitignore
└── routers/
    ├── user_routes.py
    └── post_routes.py
main.py: The entry point of the application. Initializes the FastAPI app and includes the routers.
database.py: Configures the database connection, session, and base model for SQLAlchemy.
models.py: Defines the SQLAlchemy models for the application.
routers/: Contains the route definitions for users and posts.
user_routes.py: Contains routes related to user management.
post_routes.py: Contains routes related to post management.
.env: Environment variables for database configuration (not committed to version control).
.env.example: Example environment variables file for configuration.
.gitignore: Specifies files and directories to be ignored by Git.
Endpoints
User Endpoints
Create User

http
코드 복사
POST /users/
Request Body:

json
코드 복사
{
  "username": "john_doe",
  "profile_photo": "https://example.com/photo.jpg"
}
Get User by ID

http
코드 복사
GET /users/{user_id}
Response Body:

json
코드 복사
{
  "id": 1,
  "username": "john_doe",
  "profile_photo": "https://example.com/photo.jpg"
}
Post Endpoints
Create Post

http
코드 복사
POST /posts/
Request Body:

json
코드 복사
{
  "title": "My First Post",
  "content": "This is the content of my first post.",
  "user_id": 1
}
Get Post by ID

http
코드 복사
GET /posts/{post_id}
Response Body:

json
코드 복사
{
  "id": 1,
  "title": "My First Post",
  "content": "This is the content of my first post.",
  "user_id": 1
}
Delete Post by ID

http
코드 복사
DELETE /posts/{post_id}
License
This project is licensed under the MIT License. See the LICENSE file for details.

코드 복사

이 README 파일은 프로젝트 설정, 설치, 사용법 및 주요 엔드포인트에 대한 정보를 제공합
