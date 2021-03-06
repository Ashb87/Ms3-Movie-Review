"""Imports used to connect with and use MongoDB,use flask templates
and werkzeug for password security"""
import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# Task manager project from code institute was used a lot to help with the
# build of this project
# https://github.com/TravelTimN/flask-task-manager-project/blob/demo/app.py

# Document supplied by my mentor to help understand and implement error
# handlers
# https://flask.palletsprojects.com/en/2.0.x/patterns/viewdecorators/#login-required-decorator


# ------- Home

@app.route("/")
@app.route("/home")
def home():
    """ returns user to home page """
    return render_template("index.html")


# ------- Movies

@app.route("/movies")
def movies():
    """ movie view , finds all added movies and
        returns them to the template """
    movies = list(mongo.db.movies.find())
    return render_template("movies.html", movies=movies)


# ------- Reviews

@app.route("/review/<movie_id>")
def review(movie_id):
    """ finds review for specific movie and returns
        it to the template """
    review = mongo.db.movies.find_one({"_id": ObjectId(movie_id)})
    return render_template("reviews.html", review=review)


# ------- Search Movies/Genres

@app.route("/search", methods=["GET", "POST"])
def search():
    """ gets user input from the search box and looks
        for a match in the databse """
    query = request.form.get("query")
    movies = list(mongo.db.movies.find({"$text": {"$search": query}}))
    return render_template("movies.html", movies=movies)


# ------- Register function

@app.route("/register", methods=["GET", "POST"])
def register():
    """ creates new user in the database when form is submitted """
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


# ------- Login function

@app.route("/login", methods=["GET", "POST"])
def login():
    """ Looks for users information in database when form is
        submitted. If requirements match user is directed
        to their profile page """
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get(
                    "password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# ------- Profile

@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """ grab the session user's username from db """
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    movies = list(mongo.db.movies.find(
        {"added_by": session["user"]}))

    if session["user"]:
        return render_template(
            "profile.html", username=username, movies=movies)

    return redirect(url_for("login"))


# ------- Logout function

@app.route("/logout")
def logout():
    """ removes the user from session cookie """
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# ------- Add Movie review function

@app.route("/add_movie", methods=["GET", "POST"])
def add_movie():
    """ When form is submiited the information is stored in
        the database and added to the movie page template """
    if request.method == "POST":
        movie = {
            "category_name": request.form.get("category_name"),
            "year_released": request.form.get("year_released"),
            "movie_name": request.form.get("movie_name"),
            "movie_description": request.form.get("movie_description"),
            "movie_review": request.form.get("movie_review"),
            "cover_image": request.form.get("cover_image"),
            "image_url": request.form.get("image_url"),
            "rating": int(request.form.get("rating")),
            "added_by": session["user"]
        }
        mongo.db.movies.insert_one(movie)
        flash("Your Movie Was Successfully Added")
        return redirect(url_for("movies"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_movie.html", categories=categories)


# ------- Edit Movie review function

@app.route("/edit_movie/<movie_id>", methods=["GET", "POST"])
def edit_movie(movie_id):
    """ Allows user to edit information already
        added to the database """
    movie = mongo.db.movies.find_one({"_id": ObjectId(movie_id)})
    if 'user' not in session:
        return render_template("error_pages/404.html")
    if not movie:
        return render_template("error_pages/404.html")
    if movie['added_by'] != session['user'] or session['user'] == 'Admin':
        return render_template("error_pages/404.html")
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "year_released": request.form.get("year_released"),
            "movie_name": request.form.get("movie_name"),
            "movie_description": request.form.get("movie_description"),
            "movie_review": request.form.get("movie_review"),
            "cover_image": request.form.get("cover_image"),
            "image_url": request.form.get("image_url"),
            "rating": int(request.form.get("rating")),
            "added_by": session["user"]
        }
        mongo.db.movies.update({"_id": ObjectId(movie_id)}, submit)
        flash("Movie Successfully Updated")
        return redirect(url_for(
            "profile", username=session["user"]))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_movie.html", movie=movie, categories=categories)


# ------- Delete Movie review

@app.route("/delete_movie/<movie_id>")
def delete_movie(movie_id):
    """ Deletes the chosen movie and all its data from the
        database """
    mongo.db.movies.remove({"_id": ObjectId(movie_id)})
    flash("Movie Successfully Deleted")
    return redirect(url_for('profile', username=session['user']))


# ------- Displays categories

@app.route("/get_categories")
def get_categories():
    """ Pulls the category information from the database
        and returns to the category template """
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


# ------- Add category

@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    """ Admin can add a new category to
        the genre page, which is then addd to the drop
        down field for a user to choose a genre """
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Genre Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


# ------- Edit category

@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    """ Admin can edit the category(genre) selection """
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Genre Successfully Updated")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


# ------- Delete category

@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    """ Admin can delete genres from the category collection
        in the database """
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Genre Successfully Deleted")
    return redirect(url_for("get_categories"))


# ------- Delete user account

@app.route("/delete_user")
def delete_user():
    """ Allows users to delete their own account """
    user_id = mongo.db.users.find_one(
          {"username": session["user"]})["_id"]
    mongo.db.profiles.remove({"user_id": ObjectId(user_id)})
    mongo.db.users.remove({"username": session["user"]})
    session.pop("user")
    flash("Account Successfully Deleted, We're sorry to see you go.")
    return redirect(url_for("home"))


# ------- Error Handlers

@app.errorhandler(404)
def page_not_found(error):
    """ 404 error handling from flask documentation """
    return render_template('404.html', error=error), 404


@app.errorhandler(500)
def internal_server_error(error):
    """ 500 error handling from flask documentation """
    return render_template('error_pages/500.html', error=error), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)