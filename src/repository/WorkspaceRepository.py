from db.database import SessionLocal
from db.models import Workspace
from schemas.WorkspaceSchemas import WorkspaceCreate
from utils.config import LoggerConfig

logger_config = LoggerConfig()
logger = logger_config.get_logger(__name__)


class WorkspaceRepository:
    def __init__(self):
        self._session = SessionLocal()

    def create(self, workspace: WorkspaceCreate):
        logger.info(f"Creating workspace: {workspace}")
        model = Workspace(**workspace.model_dump())

        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)

        return model

    def get_all(self):
        logger.debug("Returning all workspaces registers")
        return self._session.query(Workspace).all()

    def get_by_id(self, id):
        return self._session.query(Workspace).where(Workspace.id == id).first()

    def get_by_name(self, name):
        return self._session.query(Workspace).where(name in Workspace.name).first()

    def update(self, id):
        return
