import flet as ft

from schemas.WorkspaceSchemas import WorkspaceBase
from services.WorkspaceServices import WorkspaceServices
from utils.form_validator import FormValidator


class RegisterModal:
    def __init__(
        self, page: ft.Page, menu=None, workspace: WorkspaceBase | None = None
    ):
        self.page = page
        self.workspace_services = WorkspaceServices()
        self._menu = menu

        self._workspace = workspace

        if self._workspace:
            self._id: int = workspace.id
            self._name: str = workspace.name
            self._server_type: str = workspace.server_type
            self._host: str = workspace.host
            self._port: int = workspace.port
            self._username: str = workspace.username
            self._password: str = workspace.password

        self.dialog = ft.AlertDialog(
            title=ft.Text("Registrar novo servidor"),
            content=ft.Column(
                controls=self.components(),
                tight=True,
            ),
        )

    def validate_values(self):
        if FormValidator.password(self.password_field.value):
            self.password_field.error = "A senha deve possuir no mínimo 3 caracteres."
            return False

        if FormValidator.name(self.name_field.value):
            self.name_field.error = "Informe o nome"
            return False

        if FormValidator.server_type(self.server_type_field.value):
            self.server_type_field.error_text = "Tipo de servidor inválido"
            return False

        return True

    def save_server(self):
        if not self.validate_values():
            return

        server_data = {
            "name": self.name_field.value,
            "server_type": self.server_type_field.value,
            "host": self.address_field.value,
            "port": int(self.port_field.value) if self.port_field.value else 22,
            "username": self.username_field.value,
            "password": self.password_field.value,
        }

        if self.id_field.value is None or self.id_field.value == 0:
            self.workspace_services.create_workspace(server_data)

        else:
            self.workspace_services.update_workspace(
                int(self.id_field.value), server_data
            )

        self.close_modal()

        if self._menu and hasattr(self._menu, "page") and self._menu.page:
            self._menu.page.clean()
            self._menu.render(self._menu.page)

    def close_modal(self):
        self.dialog.open = False
        self.page.update()

    def render(self):
        self.page.overlay.append(self.dialog)
        self.dialog.open = True
        self.page.update()

    def components(
        self,
    ):
        self.id_field = ft.TextField(
            visible=False, value=str(self._id) if self._workspace else None
        )
        self.name_field = ft.TextField(
            label="Nome do servidor",
            width=300,
            value=self._name if self._workspace else None,
        )
        self.server_type_field = ft.Dropdown(
            label="Tipo de servidor",
            options=[
                ft.dropdown.Option("SFTP"),
                ft.dropdown.Option("FTP"),
            ],
            value=self._server_type if self._workspace else None,
        )
        self.address_field = ft.TextField(
            label="Hostname ou endereço IP",
            width=300,
            value=self._host if self._workspace else None,
        )
        self.port_field = ft.TextField(
            label="Porta",
            width=300,
            value=str(self._port if self._workspace else "22"),
            input_filter=ft.InputFilter(
                allow=True, regex_string=r"^[0-9]*$", replacement_string=""
            ),
        )
        self.username_field = ft.TextField(
            label="Nome de usuário",
            width=300,
            value=self._username if self._workspace else None,
        )
        self.password_field = ft.TextField(
            label="Senha",
            width=300,
            password=True,
            can_reveal_password=True,
            value=self._password if self._workspace else None,
        )
        save_button = ft.ElevatedButton("Salvar", on_click=lambda e: self.save_server())
        cancel_button = ft.ElevatedButton(
            "Cancelar", on_click=lambda e: self.close_modal()
        )

        return [
            self.id_field,
            self.name_field,
            self.server_type_field,
            self.address_field,
            self.port_field,
            self.username_field,
            self.password_field,
            ft.Row(
                alignment=ft.MainAxisAlignment.END,
                controls=[save_button, cancel_button],
            ),
        ]
