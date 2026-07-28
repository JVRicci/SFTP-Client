import json
import os

from repository.WorkspaceRepository import WorkspaceRepository
from schemas.WorkspaceSchemas import WorkspaceBase, WorkspaceCreate, WorkspaceUpdate


class WorkspaceServices:
    def __init__(self):
        self.repository = WorkspaceRepository()

    def create_workspace(self, workspace_data) -> dict:
        workspace = self.repository.create(WorkspaceCreate(**workspace_data))
        return workspace

    def get_workspace_by_id(self, workspace_id) -> dict:
        workspace = self.repository.get_by_id(workspace_id)
        return workspace

    def get_all_workspaces(self) -> list:
        workspaces = self.repository.get_all()
        return workspaces

    def update_workspace(self, workspace_id, workspace_data) -> dict:
        workspace = self.repository.update(
            workspace_id, WorkspaceUpdate(**workspace_data)
        )
        return workspace

    def delete_workspace(self, workspace_id) -> None:
        self.repository.delete(workspace_id)

    @staticmethod
    def load_ide(workspace: WorkspaceBase) -> None:
        server_json = {
            "name": workspace.name,
            "host": workspace.host,
            "protocol": workspace.server_type,
            "port": workspace.port,
            "username": workspace.username,
            "password": workspace.password,
            # "remotePath": "/var/www/html/allent/wp-content/themes/divi-child",
            "uploadOnSave": True,
            "useTempFile": False,
            "openSsh": False,
        }

        with open(".vscode/sftp.json", "w") as f:
            json.dump(server_json, f)

        os.system("code .")
