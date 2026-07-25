from pydantic import BaseModel, ConfigDict


class WorkspaceBase(BaseModel):
    name: str
    host: str
    port: int = 22
    username: str
    remote_path: str | None
    local_path: str | None
    editor: str | None
    favorite: bool = False
    notes: str | None = None


class WorkspaceCreate(WorkspaceBase):
    pass


class WorkspaceUpdate(WorkspaceBase):
    pass


class WorkspaceDelete(WorkspaceBase):
    pass


class WorkspaceResponse(WorkspaceBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
