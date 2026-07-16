from db.database import SessionLocal
from db.models import Workspace
from schemas.WorkspaceSchemas import WorkspaceCreate


class WorkspaceRepository:
    def __init__(self):
        self._session = SessionLocal()

    def create(self, workspace: WorkspaceCreate):
        print("Creating workspace:", workspace)
        model = Workspace(**workspace.model_dump())

        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)

        return model

    def get_all(self):
        return self._session.query(Workspace).all()
