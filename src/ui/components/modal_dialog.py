import flet as ft


class Dialog:
    def __init__(self, accept, cancel: None):
        self._accept = accept
        self._cancel = cancel

    def render_dialog(self, message):

        def accept():
            self._accept()
            dialog.open = False

        def cancel():
            if self._cancel:
                self._cancel()
            dialog.open = False

        dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Excluir"),
            content=ft.Text(message),
            actions=[
                ft.TextButton("Não", on_click=accept),
                ft.ElevatedButton("Sim", on_click=cancel),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

        return dialog
