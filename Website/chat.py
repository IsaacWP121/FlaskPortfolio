from flask import Flask, Blueprint, render_template, request, flash
from flask_login import login_required, current_user

chat = Blueprint("chat", __name__)

@chat.route("/", methods=["GET", "POST"])
@login_required
def home():
	return render_template("chat.html", user=current_user)
