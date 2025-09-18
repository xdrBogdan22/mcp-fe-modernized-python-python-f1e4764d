from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

from app.core.database import Base

class RepositoryType(str, enum.Enum):
    GITHUB = "github"
    GITLAB = "gitlab"
    GOOGLE_DRIVE = "google_drive"

class Repository(Base):
    __tablename__ = "repositories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    repository_link = Column(String)
    type = Column(Enum(RepositoryType))
    language = Column(String)
    last_commit = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    project_id = Column(Integer, ForeignKey("projects.id"))
    
    # Relationships
    project = relationship("Project", back_populates="repositories")
    
    def __repr__(self):
        return f"<Repository {self.name}>"
