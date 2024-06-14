from flask import Blueprint, abort
from data.pieces import *
from data.board.Board import board

routes = Blueprint("routes", __name__, template_folder="templates")
pieces_classes = {
    "bishop": Bishop.Bishop,
    "king": King.King,
    "knight": Knight.Knight,
    "pawn": Pawn.Pawn,
    "queen": Queen.Queen,
    "rook": Rook.Rook,
}


@routes.route("/api/v1/<chess_figure>/<current_field>", methods=["GET"])
def available_moves(chess_figure, current_field):
    available_moves_list = []
    try:
        figure = pieces_classes[chess_figure.lower()](current_field)
    except KeyError:
        return abort(404)

    if board.is_field_valid(current_field):
        available_moves_list = figure.available_moves_list
        error_text = None
        status_code = 200
    else:
        error_text = "Field does not exist."
        status_code = 409

    response = {
        "availableMoves": available_moves_list,
        "error": error_text,
        "figure": chess_figure,
        "currentField": current_field,
    }

    return response, status_code


@routes.route("/api/v1/<chess_figure>/<current_field>/<dest_field>", methods=["GET"])
def is_move_valid(chess_figure, current_field, dest_field):
    figure = pieces_classes[chess_figure.lower()](current_field)
    if figure.validate_move(dest_field):
        move = "valid"
        error_text = None
    else:
        move = "invalid"
        error_text = "Current move is not permitted"

    response = {
        "move": move,
        "figure": chess_figure,
        "error": error_text,
        "currentField": current_field,
        "destinationField": dest_field,
    }

    return response
