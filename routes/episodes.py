from flask import Blueprint, jsonify, request
from models import Episode

episodes_bp = Blueprint('episodes', __name__)

@episodes_bp.route('/', methods=['GET'])
def get_episodes():
    episodes = [episode.to_dict() for episode in Episode.query.all()]
    return jsonify(episodes)

@episodes_bp.route('/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({"error": "Episode not found"}), 404
    return jsonify(episode.to_dict())
