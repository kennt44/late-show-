from flask import Blueprint, jsonify, request
from models import Appearance, db

appearances_bp = Blueprint('appearances', __name__)

@appearances_bp.route('/', methods=['POST'])
def create_appearance():
    data = request.get_json()
    try:
        appearance = Appearance(
            rating=data['rating'],
            episode_id=data['episode_id'],
            guest_id=data['guest_id']
        )
        db.session.add(appearance)
        db.session.commit()
        return jsonify(appearance.to_dict()), 201
    except Exception as e:
        return jsonify({"errors": [str(e)]}), 400
