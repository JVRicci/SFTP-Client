import flet as ft

from services.WorkspaceServices import WorkspaceServices


class RegisterModal:
    def __init__(
        self,
        page: ft.Page,
        menu=None,
        id: int | None = None,
        name: str = "",
        server_type="",
        host="",
        port=22,
        username="",
        password="",
    ):
        self.page = page
        self.workspace_services = WorkspaceServices()
        self._menu = menu

        self._id: int = id
        self._name: str = name
        self._server_type: str = server_type
        self._host: str = host
        self._port: int = port
        self._username: str = username
        self._password: str = password

        self.dialog = ft.AlertDialog(
            title=ft.Text("Registrar novo servidor"),
            content=ft.Column(
                controls=self.components(),
                tight=True,
            ),
        )

    def validator(self) -> bool:
        valid = True

        if len(self.password_field.value.strip()) < 3:
            self.password_field.error_text = (
                "A senha deve possuir no mínimo 3 caracteres."
            )
            valid = False
        else:
            self.password_field.error_text = None

        if not self.name_field.value.strip():
            self.name_field.error_text = "Informe o nome."
            valid = False
        else:
            self.name_field.error_text = None

        return valid

    def save_server(self):
        if not self.validator():
            self.dialog.update()
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
            visible=False, value=str(self._id) if self._id is not None else ""
        )
        self.name_field = ft.TextField(
            label="Nome do servidor", width=300, value=self._name
        )
        self.server_type_field = ft.Dropdown(
            label="Tipo de servidor",
            options=[
                ft.dropdown.Option("SFTP"),
                ft.dropdown.Option("FTP"),
            ],
            value=self._server_type,
        )
        self.address_field = ft.TextField(
            label="Hostname ou endereço IP", width=300, value=self._host
        )
        self.port_field = ft.TextField(label="Porta", width=300, value=str(self._port))
        self.username_field = ft.TextField(
            label="Nome de usuário", width=300, value=self._username
        )
        self.password_field = ft.TextField(
            label="Senha",
            width=300,
            password=True,
            can_reveal_password=True,
            value=self._password,
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
