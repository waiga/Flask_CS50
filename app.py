from flask import Flask, render_template, request

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        return render_template("greet.html", name= request.form.get("name", "world"))
    # name = request.args.get("name", "세계")
    # if "name" in request.args:
    #     name = request.args["name"]
    # else:
    #     name = "세계"
    # return render_template("index.html", name=name)

# @app.route("/greet", methods=["POST"])
# def greet():
#     name = request.args.get("name", "world")
#     return render_template("greet.html", name=name)

app.run()