from flask import render_template, request, Blueprint
from flaskblog.models import Post 

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():

    # Sent parameter from url default is 1 (The page that would like to show first)
    page = request.args.get('page', 1, type=int)

    # The varaiable name that we declare here. We will able access it on html
    # posts = Post.query.all()
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    
    return render_template("home.html", posts=posts)

@main.route("/about")
def about():
    return render_template("about.html", title="About")
