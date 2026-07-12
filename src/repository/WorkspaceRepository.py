from slalchemy.orm import Session

from db.models import Workspace
from src.schemas.WorkspaceSchemas import (
    WorkspaceBase,
    WorkspaceCreate,
    WorkspaceResponse,
)


class WorkspaceRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, workspace: WorkspaceCreate):
        model = Workspace(**workspace.model_dump())

        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)

        return model
