import flet as ft


class Dialog:
    def __init__(self, accept, cancel=None):
        self._accept = accept
        self._cancel = cancel

    def render_dialog(self, message):

        def accept(e):
            self._accept()
            dialog.open = False
            dialog.page.update()

        def cancel(e):
            if self._cancel:
                self._cancel()
            dialog.open = False
            dialog.page.update()

        dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Excluir"),
            content=ft.Text(message),
            actions=[
                ft.TextButton("Não", on_click=cancel),
                ft.ElevatedButton("Sim", on_click=accept),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

        return dialog
