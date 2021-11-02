from flask import Blueprint
from flask import Response
from flask import jsonify

from saturn_engine.worker_manager.config import config

bp = Blueprint("inventories", __name__, url_prefix="/api/inventories")


@bp.route("", methods=("GET",))
async def get_inventories() -> Response:
    inventories = [i.to_core_object() for i in config().static_definitions.inventories]
    return jsonify({"inventories": inventories})