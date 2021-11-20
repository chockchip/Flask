from flask import Blueprint, render_template

erros = Blueprint('errors', __name__)

@erros.app_errorhandler(404)
def error_404(error):
    return render_template('errors/404.html'), 404

@erros.app_errorhandler(403)
def error_403(error):
    return render_template('errors/404.html'), 403

@erros.app_errorhandler(500)
def error_500(error):
    return render_template('errors/404.html'), 500