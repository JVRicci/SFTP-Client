import flet as ft

from services.WorkspaceServices import WorkspaceServices
from ui.components.modal_dialog import Dialog
from ui.components.register import RegisterModal


class Menu:
    def __init__(self, width: int, height: int, resizable: bool = False):
        self._title = "SFTP Client for IDEs"
        self._width = width
        self._height = height
        self._resizable = resizable
        self.workspace_services = WorkspaceServices()

    def register_modal(self, page: ft.Page):
        register_modal = RegisterModal(page, self)
        register_modal.render()

    def get_servers(self):
        return self.workspace_services.get_all_workspaces()

    def render_table(self, server_list: list | None = None):
        server_row = []
        if server_list is not None:
            server_row = [x for x in server_list]

        table = ft.DataTable(
            columns=[
                ft.DataColumn("Servidor"),
                ft.DataColumn("Editar"),
                ft.DataColumn("Excluir"),
            ],
            rows=server_row,
        )

        return table

    def components(self):
        # text = ft.Text("Enter a number:", size=20)
        row_list = []

        register = ft.Button(
            "Registrar novo servidor",
            on_click=lambda e: self.register_modal(e.page),
            margin=ft.Alignment.CENTER,
        )

        services = WorkspaceServices()

        for server in self.get_servers():
            print(server)
            delete_dialog = Dialog(services.delete_workspace(server.id))

            row_list.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.TextButton(server.name)),
                        ft.DataCell(
                            ft.IconButton(icon=ft.Icons.EDIT, icon_color="yellow")
                        ),
                        ft.DataCell(
                            ft.IconButton(
                                icon=ft.Icons.DELETE,
                                icon_color="red",
                                on_click=delete_dialog.render_dialog(),
                            )
                        ),
                    ]
                )
            )

        self.render_table()

        return [
            # text,
            register,
            self.render_table(row_list),
        ]

    def render(self, page: ft.Page):
        page.title = self._title

        # page.window.resizable = self._resizable
        page.window.width = self._width
        page.window.height = self._height

        components = self.components()

        page.add(
            ft.Container(
                content=ft.Column(
                    controls=components,
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                alignment=ft.Alignment(0, 0),
                expand=True,
            )
        )
