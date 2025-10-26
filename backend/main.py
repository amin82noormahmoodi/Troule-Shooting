from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
from pydantic import BaseModel
from typing import List, Optional
import os

# Database configuration
DATABASE_URL = "postgresql://postgres:amin1382@localhost/saffar"

# Create database engine
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Database Models
class Board(Base):
    __tablename__ = "boards"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    
    # Relationship
    problems = relationship("Problem", back_populates="board")

class Problem(Base):
    __tablename__ = "problems"
    
    id = Column(Integer, primary_key=True, index=True)
    board_id = Column(Integer, ForeignKey("boards.id"))
    problem_text = Column(Text)
    
    # Relationships
    board = relationship("Board", back_populates="problems")
    solutions = relationship("Solution", back_populates="problem")

class Solution(Base):
    __tablename__ = "solutions"
    
    id = Column(Integer, primary_key=True, index=True)
    problem_id = Column(Integer, ForeignKey("problems.id"))
    solution_text = Column(Text)
    
    # Relationship
    problem = relationship("Problem", back_populates="solutions")

# Create tables
Base.metadata.create_all(bind=engine)

# Pydantic models
class BoardResponse(BaseModel):
    id: int
    name: str
    
    class Config:
        from_attributes = True

class ProblemResponse(BaseModel):
    id: int
    board_id: int
    problem_text: str
    
    class Config:
        from_attributes = True

class SolutionResponse(BaseModel):
    id: int
    problem_id: int
    solution_text: str
    
    class Config:
        from_attributes = True

# FastAPI app
app = FastAPI(title="Board Troubleshooting API", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],  # React dev servers
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# API Routes
@app.get("/")
async def root():
    return {"message": "Board Troubleshooting API is running"}

@app.get("/boards", response_model=List[BoardResponse])
async def get_boards(db: Session = Depends(get_db)):
    """Get all boards"""
    try:
        boards = db.query(Board).all()
        return boards
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@app.get("/problems/{board_id}", response_model=List[ProblemResponse])
async def get_problems(board_id: int, db: Session = Depends(get_db)):
    """Get all problems for a specific board"""
    try:
        # Check if board exists
        board = db.query(Board).filter(Board.id == board_id).first()
        if not board:
            raise HTTPException(status_code=404, detail="Board not found")
        
        problems = db.query(Problem).filter(Problem.board_id == board_id).all()
        return problems
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@app.get("/solutions/{problem_id}", response_model=List[SolutionResponse])
async def get_solutions(problem_id: int, db: Session = Depends(get_db)):
    """Get all solutions for a specific problem"""
    try:
        # Check if problem exists
        problem = db.query(Problem).filter(Problem.id == problem_id).first()
        if not problem:
            raise HTTPException(status_code=404, detail="Problem not found")
        
        solutions = db.query(Solution).filter(Solution.problem_id == problem_id).all()
        return solutions
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
