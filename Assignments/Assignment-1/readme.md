# Calculator API

A small FastAPI app to do basic math operations.

## Features

- Add, Subtract, Multiply, Divide
- Dockerized
- Tested with pytest
- GitHub Actions CI
- Clean structure with environment variables

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/iamisha/Fusemachine.git
cd Assignments/Assignment-1
```
### 2. Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate (mine is linux)
```
### 3.  Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
> **Note:** Create a .env file in the root directory:

### 5. Run the Application Locally
```bash
uvicorn app.main:app --reload
```
> **Note:** Then open your browser or API client to:

```arduino
http://127.0.0.1:8000/docs
```

## Available Endpoints

| Method | Endpoint                       | Description     |
| ------ | ------------------------------ | --------------- |
| GET    | `/calculator/add?a=1&b=2`      | Returns `a + b` |
| GET    | `/calculator/subtract?a=5&b=3` | Returns `a - b` |
| GET    | `/calculator/multiply?a=2&b=4` | Returns `a * b` |
| GET    | `/calculator/divide?a=10&b=2`  | Returns `a / b` |


## Run Tests
Run from the project root:
```bash
PYTHONPATH=./ pytest
```

## Running with Docker
```bash
docker-compose up --build
```

## Pre-commit Hooks
Install and activate pre-commit:
```bash
pip install pre-commit
pre-commit install
pre-commit run --all-files
```

## GitHub Actions (CI)
CI is configured in .github/workflows/ci.yml. It will:

* Install dependencies

* Run tests

* Lint your code

on every push to `main` or `dev`.

## 🙋‍♀️ Author 
Isha Hitang
GitHub: [iamisha](https://github.com/iamisha)
