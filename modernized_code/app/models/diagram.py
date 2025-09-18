from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

from app.core.database import Base

class DiagramType(str, enum.Enum):
    UML = "uml"
    ERD = "erd"
    CLASS_DIAGRAM = "class_diagram"
    FLOWCHART = "flowchart"

class Diagram(Base):
    __tablename__ = "diagrams"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    type = Column(Enum(DiagramType))
    version = Column(String, default="1.0")
    content = Column(Text)  # JSON or XML representation of diagram
    image_path = Column(String, nullable=True)  # Path to rendered image if applicable
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    project_id = Column(Integer, ForeignKey("projects.id"))
    
    # Relationships
    project = relationship("Project", back_populates="diagrams")
    
    def __repr__(self):
        return f"<Diagram {self.name}>"
