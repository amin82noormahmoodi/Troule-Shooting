# Board Troubleshooting Platform - Backend

A FastAPI-based backend service for the Board Troubleshooting Platform that provides RESTful APIs for managing boards, problems, and solutions.

## 🚀 Features

- **FastAPI Framework**: Modern, fast web framework for building APIs
- **PostgreSQL Database**: Robust relational database with SQLAlchemy ORM
- **CORS Support**: Configured for frontend integration
- **Error Handling**: Comprehensive error handling and validation
- **Sample Data**: Pre-populated with sample troubleshooting data

## 📋 Prerequisites

- Python 3.8+
- PostgreSQL database
- pip (Python package installer)

## 🛠️ Installation

1. **Clone the repository** (if not already done)
   ```bash
   cd backend
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up PostgreSQL database**
   - Create a database named `saffar`
   - Set password to `amin1382` for user `postgres`
   - Or modify the `DATABASE_URL` in `main.py` to match your configuration

5. **Run the sample data script** (optional)
   ```bash
   python sample_data.py
   ```

## 🚀 Running the Server

```bash
python main.py
```

The API will be available at `http://localhost:8000`

## 📚 API Endpoints

### Base URL: `http://localhost:8000`

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API health check |
| GET | `/boards` | Get all boards |
| GET | `/problems/{board_id}` | Get problems for a specific board |
| GET | `/solutions/{problem_id}` | Get solutions for a specific problem |

### Example Responses

**GET /boards**
```json
[
  {
    "id": 1,
    "name": "Arduino Uno"
  },
  {
    "id": 2,
    "name": "Raspberry Pi 4"
  }
]
```

**GET /problems/1**
```json
[
  {
    "id": 1,
    "board_id": 1,
    "problem_text": "Board not detected by computer"
  }
]
```

**GET /solutions/1**
```json
[
  {
    "id": 1,
    "problem_id": 1,
    "solution_text": "Check USB cable connection and try a different USB port."
  }
]
```

## 🗄️ Database Schema

### Tables

- **boards**: `id`, `name`
- **problems**: `id`, `board_id`, `problem_text`
- **solutions**: `id`, `problem_id`, `solution_text`

### Relationships

- One board can have many problems
- One problem can have many solutions
- Foreign key constraints ensure data integrity

## 🔧 Configuration

The database connection is configured in `main.py`:

```python
DATABASE_URL = "postgresql://postgres:amin1382@localhost/saffar"
```

Modify this URL to match your PostgreSQL configuration.

## 📝 Sample Data

The `sample_data.py` script creates:
- 5 different boards (Arduino Uno, Raspberry Pi 4, ESP32, STM32, Arduino Mega)
- 20 problems across all boards
- 60+ solutions for various problems

## 🐛 Troubleshooting

### Common Issues

1. **Database Connection Error**
   - Ensure PostgreSQL is running
   - Verify database credentials
   - Check if database `saffar` exists

2. **Port Already in Use**
   - Change port in `main.py` or kill existing process
   - Use `uvicorn main:app --port 8001` for different port

3. **CORS Issues**
   - Frontend URL is configured in CORS middleware
   - Add your frontend URL to `allow_origins` list

## 📖 API Documentation

Once the server is running, visit:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 🔄 Development

To run in development mode with auto-reload:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## 📦 Dependencies

- **fastapi**: Web framework
- **uvicorn**: ASGI server
- **sqlalchemy**: ORM
- **psycopg2-binary**: PostgreSQL adapter
- **pydantic**: Data validation
