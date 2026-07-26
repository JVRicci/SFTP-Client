from db.database import SessionLocal
from db.models import Workspace
from schemas.WorkspaceSchemas import WorkspaceCreate, WorkspaceUpdate
from utils.config import LoggerConfig

logger_config = LoggerConfig()
logger = logger_config.get_logger(__name__)


class WorkspaceRepository:
    def __init__(self):
        self._session = SessionLocal()

    def create_or_update(self, id: int, workspace: Workspace):
        existing = self._session.query(Workspace).filter(Workspace.id == id)

        if existing:
            return self._update(id, workspace)

        return self._create(workspace)

    def create(self, workspace: WorkspaceCreate):
        logger.info(f"Creating workspace: {workspace}")
        data = {k: v for k, v in workspace.model_dump().items() if k in Workspace.__table__.columns}
        stmt = Workspace(**data)

        self._session.add(stmt)
        self._session.commit()
        self._session.refresh(stmt)

        return stmt

    def delete(self, id):
        stmt = self._session.query(Workspace).filter(Workspace.id == id).first()

        if not stmt:
            return False

        self._session.delete(stmt)
        self._session.commit()
        return True

    def get_all(self) -> list:
        logger.info("Returning all workspace registers")
        return self._session.query(Workspace).all()

    def get_by_id(self, id: int) -> dict:
        workspace = self._session.query(Workspace).where(Workspace.id == id).first()
        logger.info(f"Return: {workspace}")
        return workspace

    def get_by_name(self, name: str) -> dict:
        workspace = self._session.query(Workspace).where(name in Workspace.name).first()
        logger.info(f"Return: {workspace}")
        return workspace

    def update(self, id: int, workspace: WorkspaceUpdate):
        stmt = self._session.get(Workspace, id)

        if stmt is None:
            return

        for key, value in workspace.model_dump(exclude_unset=True).items():
            if key in Workspace.__table__.columns:
                setattr(stmt, key, value)

        self._session.commit()
        self._session.refresh(stmt)

        return stmt
