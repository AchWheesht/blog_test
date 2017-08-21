from flask import Flask, render_template, request, make_response, redirect, session, send_from_directory, make_response

app = Flask(__name__)

@app.route("/")
def blog_index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
