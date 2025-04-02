from flask import Flask, render_template, request, redirect, url_for, jsonify
import json

app = Flask(__name__)

# Shared admin password
ADMIN_PASSWORD = "password"

# Load existing data
def load_data():
    try:
        with open("data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"tabs": []}

# Save data to file
def save_data(data):
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

@app.route("/")
def index():
    data = load_data()
    return render_template("index.html", data=data)

@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        # Get the password from the form
        password = request.form.get("password")
        if password == ADMIN_PASSWORD:
            # Redirect to the admin panel if the password is correct
            return redirect(url_for("admin_panel"))
        else:
            # Return an error message if the password is incorrect
            return "Incorrect password!", 403
    # Render the login page for GET requests
    return render_template("login.html")

@app.route("/admin-panel")
def admin_panel():
    # Render the admin panel (you can create an admin.html for this)
    return render_template("admin.html")

@app.route("/update", methods=["POST"])
def update():
    data = load_data()
    new_tab = request.form.get("new_tab")
    new_content = request.form.get("new_content")

    if new_tab and new_content:
        data["tabs"].append({"tab": new_tab, "content": new_content})
        save_data(data)
        return redirect(url_for("admin_panel"))
    return "Invalid input!", 400

if __name__ == "__main__":
    app.run(debug=True)