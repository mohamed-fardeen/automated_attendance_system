import os
import logging
from logging.handlers import RotatingFileHandler
from typing import Tuple

import numpy as np
import cv2

from .config import config


def setup_logging() -> None:
    os.makedirs(config.LOGS_DIR, exist_ok=True)
    log_path = os.path.join(config.LOGS_DIR, "facial_recognition.log")

    handler = RotatingFileHandler(log_path, maxBytes=1_000_000, backupCount=3)
    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s - %(message)s"
    )
    handler.setFormatter(formatter)

    root = logging.getLogger()
    root.setLevel(config.LOG_LEVEL)
    root.addHandler(handler)


def load_image(path: str) -> np.ndarray:
    """Load image as BGR array using OpenCV."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"Image not found: {path}")

    img = cv2.imread(path)
    if img is None:
        raise ValueError(f"Failed to read image: {path}")
    return img


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    """Cosine similarity between two 1D vectors."""
    a = a.flatten().astype("float32")
    b = b.flatten().astype("float32")
    if np.linalg.norm(a) == 0 or np.linalg.norm(b) == 0:
        return 0.0
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))


def similarity_to_confidence(similarity: float) -> float:
    """
    Convert cosine similarity [-1,1] to rough confidence [0,1].
    Very simple mapping for week 1.
    """
    return max(0.0, min(1.0, (similarity + 1.0) / 2.0))
