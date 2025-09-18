from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey, Text, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

from app.core.database import Base

class ProjectStatus(str, enum.Enum):
    DRAFT = "draft"
    NEW = "new"
    ACTIVE = "active"
    ARCHIVED = "archived"

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text)
    programming_language = Column(String)
    status = Column(Enum(ProjectStatus), default=ProjectStatus.NEW)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    owner_id = Column(Integer, ForeignKey("users.id"))
    
    # Dependencies and target environment (stored as JSON in practice)
    dependencies = Column(Text)  # JSON string
    target_environment = Column(Text)  # JSON string
    
    # Relationships
    owner = relationship("User", back_populates="owned_projects")
    repositories = relationship("Repository", back_populates="project", cascade="all, delete-orphan")
    documents = relationship("Document", back_populates="project", cascade="all, delete-orphan")
    diagrams = relationship("Diagram", back_populates="project", cascade="all, delete-orphan")
    members = relationship("ProjectMember", back_populates="project", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Project {self.name}>"
