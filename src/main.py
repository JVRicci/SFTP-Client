import flet as ft

from db.database import Base, engine

# from ui.app import
from ui.screens.menu import Menu

WIDTH = 400
HEIGHT = 500
RESIZABLE = False


def create_database():
    Base.metadata.create_all(bind=engine)


def main():
    create_database()
    MainMenu = Menu(width=WIDTH, height=HEIGHT, resizable=RESIZABLE)
    ft.run(MainMenu.render)  # , view=ft.WEB_BROWSER, port=8080)


if __name__ == "__main__":
    main()
