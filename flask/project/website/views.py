
from flask import render_template, Blueprint


website_blueprint = Blueprint('website_blueprint', __name__)


@website_blueprint.route('/')
def index():
	return render_template('index.html')
