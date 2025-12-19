from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

from .config import config
from .utils import setup_logging
from .services import list_test_images, compare_two_images


setup_logging()
app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "service": "facial-recognition"}), 200


@app.route("/test-images", methods=["GET"])
def get_test_images():
    """
    Helper endpoint to quickly see what local test images are available.
    Week 1 helper only.
    """
    images = list_test_images()
    return jsonify({"count": len(images), "images": images}), 200


@app.route("/debug/compare", methods=["POST"])
def debug_compare():
    """
    Week 1 debug endpoint:
    Body JSON: { "image_a": "path/to/a.jpg", "image_b": "path/to/b.jpg" }
    Paths should typically be under test_images/.
    """
    data = request.get_json(force=True, silent=True) or {}
    image_a = data.get("image_a")
    image_b = data.get("image_b")

    if not image_a or not image_b:
        return jsonify({"error": "image_a and image_b are required"}), 400

    try:
        result = compare_two_images(image_a, image_b)
        return jsonify(result), 200
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500


@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return e
    return jsonify({"error": "Internal server error", "details": str(e)}), 500


if __name__ == "__main__":
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
