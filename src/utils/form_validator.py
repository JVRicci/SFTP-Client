class FormValidator:
    @staticmethod
    def password(password) -> bool:
        return len(password) < 3

    @staticmethod
    def name(name) -> bool:
        return len(name) < 4

    @staticmethod
    def server_type(server) -> bool:
        return server in ("FTP", "SFTP")
