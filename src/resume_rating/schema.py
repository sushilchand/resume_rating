from datetime import date
from typing import Optional
from pydantic import BaseModel

class ExperienceSchema(BaseModel):
    company_name: str
    description: str
    start_date: date
    end_date: Optional[date] = None


class EducationSchema(BaseModel):
    degree: str
    name: str
    start_date: date
    end_date: Optional[date] = None


class ProjectSchema(BaseModel):
    name: str
    description: Optional[str] = None


class ResumeSchema(BaseModel):
    name: str
    current_company_name: str
    skills: list[str]
    experience: list[ExperienceSchema]
    projects: list[ProjectSchema]
    education: Optional[EducationSchema] = None

class MatchResultSchema(BaseModel):
    candidate_name: str
    final_score: float
    reason: str

class JobDescriptionSchema(BaseModel):
    role: str
    min_experience: int
    description: str
    required_skills: list[str]
    preferred_skills: list[str]
