from repository.WorkspaceRepository import WorkspaceRepository


class WorkspaceServices:
    def __init__(self, repository):
        self.repository = repository

    def create_workspace(self, workspace_data):
        workspace = self.repository.create(workspace_data)
        return workspace
