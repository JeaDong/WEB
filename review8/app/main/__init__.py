from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
from ..models import Permission

@main.app_context_processor#全局作用，但是不知道作用是什么
def inject_permissions():
    return dict(Permission=Permission)