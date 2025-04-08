from flask import Blueprint, jsonify
from models import Guest

guests_bp = Blueprint('guests', __name__)

@guests_bp.route('/', methods=['GET'])
def get_guests():
    guests = [guest.to_dict() for guest in Guest.query.all()]
    return jsonify(guests)
