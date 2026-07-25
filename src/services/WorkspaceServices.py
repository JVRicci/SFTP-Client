from repository.WorkspaceRepository import WorkspaceRepository
from schemas.WorkspaceSchemas import WorkspaceBase


class WorkspaceServices:
    def __init__(self):
        self.repository = WorkspaceRepository()

    def create_workspace(self, workspace_data):
        workspace = self.repository.create(WorkspaceBase(**workspace_data))
        return workspace

    def get_workspace_by_id(self, workspace_id):
        workspace = self.repository.get(workspace_id)
        return workspace

    def get_all_workspaces(self):
        workspaces = self.repository.get_all()
        return workspaces

    def update_workspace(self, workspace_id, workspace_data):
        workspace = self.repository.update(workspace_id, workspace_data)
        return workspace

    def delete_workspace(self, workspace_id):
        self.repository.delete(workspace_id)
