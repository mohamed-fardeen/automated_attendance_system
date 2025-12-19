import os
from typing import Dict, Any, Tuple

import numpy as np
from deepface import DeepFace

from .config import config
from .utils import load_image, cosine_similarity, similarity_to_confidence


def detect_and_embed(image_path: str) -> Tuple[np.ndarray, Dict[str, Any]]:
    """
    Run face detection + embedding on a single image.

    Returns:
        embedding: np.ndarray
        metadata: dict with basic info (e.g., number of faces)
    """
    img = load_image(image_path)

    # DeepFace handles detection + embedding internally.
    # For week 1 we keep it simple: use default model & backend.
    analysis = DeepFace.represent(
        img_path=image_path,
        model_name="Facenet",
        enforce_detection=True
    )

    # DeepFace.represent can return a list; take first embedding
    if isinstance(analysis, list):
        embedding = np.array(analysis[0]["embedding"], dtype="float32")
        meta = {
            "num_faces": len(analysis),
            "source": image_path,
            "model": analysis[0].get("model_name", "Facenet"),
        }
    else:
        embedding = np.array(analysis["embedding"], dtype="float32")
        meta = {
            "num_faces": 1,
            "source": image_path,
            "model": analysis.get("model_name", "Facenet"),
        }

    return embedding, meta


def compare_two_images(image_path_a: str, image_path_b: str) -> Dict[str, Any]:
    """
    Generate embeddings for two images and compute similarity + confidence.
    """
    emb_a, meta_a = detect_and_embed(image_path_a)
    emb_b, meta_b = detect_and_embed(image_path_b)

    sim = cosine_similarity(emb_a, emb_b)
    conf = similarity_to_confidence(sim)

    return {
        "image_a": meta_a["source"],
        "image_b": meta_b["source"],
        "similarity": sim,
        "confidence": conf,
        "meta_a": meta_a,
        "meta_b": meta_b,
    }


def list_test_images() -> Any:
    """Return list of images inside test_images directory."""
    if not os.path.exists(config.TEST_IMAGES_DIR):
        return []

    return [
        os.path.join(config.TEST_IMAGES_DIR, f)
        for f in os.listdir(config.TEST_IMAGES_DIR)
        if f.lower().endswith((".jpg", ".jpeg", ".png"))
    ]