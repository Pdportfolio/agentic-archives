"""Simple file + console logger."""
import os
import logging
from datetime import datetime

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("logs/pipeline.log"),
        logging.StreamHandler(),
    ],
)
_logger = logging.getLogger("ase")


def log(message: str, level: str = "INFO"):
    level = level.upper()
    if level == "ERROR":
        _logger.error(message)
    elif level == "WARNING":
        _logger.warning(message)
    else:
        _logger.info(message)
