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

    def open_register_modal(self, page: ft.Page, server=None):

        if server != None:
            register_modal = RegisterModal(page, self, server)
            print(server.server_type)
            register_modal.render()
            return

        register_modal = RegisterModal(page, self)
        register_modal.render()
        return

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
        row_list = []

        register = ft.Button(
            "Registrar novo servidor",
            on_click=lambda e: self.open_register_modal(e.page),
            margin=ft.Alignment.CENTER,
        )

        for server in self.get_servers():
            row_list.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(
                            ft.TextButton(
                                server.name,
                                on_click=lambda e, server=server: (
                                    WorkspaceServices.load_ide(server)
                                ),
                            )
                        ),
                        ft.DataCell(
                            ft.IconButton(
                                icon=ft.Icons.EDIT,
                                icon_color="yellow",
                                on_click=lambda e, server=server: self.open_register_modal(
                                    e.page, server
                                ),
                            )
                        ),
                        ft.DataCell(
                            ft.IconButton(
                                icon=ft.Icons.DELETE,
                                icon_color="red",
                                on_click=lambda e, server=server: self.open_delete_dialog(
                                    e.page, server
                                ),
                            )
                        ),
                    ]
                )
            )

        self.render_table()

        return [
            register,
            self.render_table(row_list),
        ]

    def open_delete_dialog(self, page: ft.Page, server):
        def delete_server_callback():
            self.workspace_services.delete_workspace(server.id)
            page.clean()
            self.render(page)

        delete_dialog = Dialog(accept=delete_server_callback, cancel=None)
        dialog_control = delete_dialog.render_dialog(
            f"Deseja realmente excluir o servidor '{server.name}'?"
        )
        page.overlay.append(dialog_control)
        dialog_control.open = True
        page.update()

    def render(self, page: ft.Page):
        self.page = page
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
