from flask import Blueprint
from controllers.ProductController import index, store, show, update, delete


product_bp = Blueprint('product_bp', __name__)

product_bp.route('/', methods=['GET'])(index)

product_bp.route('/create', methods=['POST'])(store)

product_bp.route('/<int:product_id>', methods=['GET'])(show)

product_bp.route('/<int:product_id>/edit', methods=['POST'])(update)

product_bp.route('/<int:product_id>', methods=['DELETE'])(delete)

