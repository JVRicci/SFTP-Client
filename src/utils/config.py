import logging
from pathlib import Path


class LoggerConfig:
    def __init__(self, log_path=None, level=logging.DEBUG):
        self._root = Path(__file__).resolve().parent
        self._log_path = Path(log_path) if log_path else self._root / "debug.log"

        self._log_path.parent.mkdir(parents=True, exist_ok=True)

        self._logger_config(level)

    def _logger_config(self, level):
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

        root_logger = logging.getLogger()
        root_logger.handlers.clear()
        root_logger.setLevel(level)

        file_handler = logging.FileHandler(self._log_path, encoding="utf-8")
        file_handler.setFormatter(formatter)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        root_logger.addHandler(file_handler)
        # root_logger.addHandler(stream_handler)

    @staticmethod
    def get_logger(module_name):
        logger = logging.getLogger(module_name)
        logger.setLevel(logging.DEBUG)
        return logger
