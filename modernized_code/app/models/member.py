from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

from app.core.database import Base

class MemberRole(str, enum.Enum):
    VIEWER = "viewer"
    EDITOR = "editor"
    OWNER = "owner"

class ProjectMember(Base):
    __tablename__ = "project_members"

    id = Column(Integer, primary_key=True, index=True)
    role = Column(Enum(MemberRole), default=MemberRole.VIEWER)
    pending_access = Column(Boolean, default=True)
    invitation_token = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    project_id = Column(Integer, ForeignKey("projects.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    
    # Relationships
    project = relationship("Project", back_populates="members")
    user = relationship("User", back_populates="memberships")
    
    def __repr__(self):
        return f"<ProjectMember {self.user_id} - {self.project_id}>"
