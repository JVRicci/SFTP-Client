import flet as ft
from services.WorkspaceServices import WorkspaceServices


class RegisterModal:
    def __init__(self, page: ft.Page):
        self.page = page
        self.workspace_services = WorkspaceServices()

        self.dialog = ft.AlertDialog(
            title=ft.Text("Registrar novo servidor"),
            content=ft.Column(
                controls=self.components(),
                tight=True,
            ),
        )

    def save_server(self):
        name = self.dialog.content.controls[0].value
        server_type = self.dialog.content.controls[1].value
        host = self.dialog.content.controls[2].value
        port = self.dialog.content.controls[3].value
        username = self.dialog.content.controls[4].value
        password = self.dialog.content.controls[5].value

        self.workspace_services.create_workspace(
            {
                "name": name,
                "server_type": server_type,
                "host": host,
                "port": port,
                "username": username,
                "password": password,
            }
        )
        self.close_modal()

    def close_modal(self):
        self.dialog.open = False
        self.page.update()

    def render(self):
        self.page.overlay.append(self.dialog)
        self.dialog.open = True
        self.page.update()

    def components(self):
        name = ft.TextField(label="Nome do servidor", width=300)
        server_type = ft.Dropdown(
            label="Tipo de servidor",
            options=[
                ft.dropdown.Option("SFTP"),
                ft.dropdown.Option("FTP"),
            ],
        )
        address = ft.TextField(
            label="Hostname ou endereço IP",
            width=300,
        )
        port = ft.TextField(label="Porta", width=300, value="22")
        username = ft.TextField(label="Nome de usuário", width=300)
        password = ft.TextField(
            label="Senha", width=300, password=True, can_reveal_password=True
        )
        save_button = ft.ElevatedButton("Salvar", on_click=lambda e: self.save_server())
        cancel_button = ft.ElevatedButton(
            "Cancelar", on_click=lambda e: self.close_modal()
        )

        return [
            name,
            server_type,
            address,
            port,
            username,
            password,
            ft.Row(
                alignment=ft.MainAxisAlignment.END,
                controls=[save_button, cancel_button],
            ),
        ]
