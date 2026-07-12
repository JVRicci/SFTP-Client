from db.database import Base, engine

# from ui.app import


def create_database():
    Base.metadata.create_all(bind=engine)


def main():
    create_database()
    # app = create_app()
    # app.run()


if __name__ == "__main__":
    main()
