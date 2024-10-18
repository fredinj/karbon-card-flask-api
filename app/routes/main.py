from flask import Blueprint

main_routes = Blueprint('main', __name__)

@main_routes.route('/')
def home():
    return "Welcome to KarbonCard!"

@main_routes.route('/about')
def about():
    return "About KarbonCard"
