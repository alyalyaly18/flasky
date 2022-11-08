from flask import abort, Blueprint, jsonify, make_response, request # put in alphabetical order
from app import db
from app.models.menu import Menu # flask import 
from app.routes.breakfast import get_model_from_id

menu_bp = Blueprint("menu", __name__, url_prefix="/menu")

@menu_bp.route('', methods=['GET'])
def get_all_menus():
    menus = Menu.query.all()
    
    result = []
    for item in menus:
        result.append(item.to_dict())
    return jsonify(result), 200

@menu_bp.route('', methods=['POST'])
def create_one_menu():
    request_body = request.get_json()

    new_menu = Menu(
        restaurant_name=request_body['restaurant_name'],
        meal=request_body['meal']
    )

    db.session.add(new_menu)
    db.session.commit()

    return jsonify({'msg':f'Sucessfully created Breakfast with id = {new_menu.id}'}), 201

@menu_bp.route('/<menu_id>/breakfasts', methods=['GET']) # nested route
def get_breakfasts_for_menu(menu_id):
    menu = get_model_from_id(Menu, menu_id)

    breakfasts = menu.get_breakfast_list()

    return jsonify(breakfasts), 200 
