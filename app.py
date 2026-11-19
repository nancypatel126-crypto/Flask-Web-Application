
from flask import Flask, render_template

app = Flask(__name__)


# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# About Page
@app.route("/about")
def about():
    return render_template("about.html")


# Contact Page
@app.route("/contact")
def contact():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Contact Us</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>

        <nav>
            <h2>My Website</h2>
            <div>
                <a href="/">Home</a>
                <a href="/about">About</a>
                <a href="/contact">Contact</a>
            </div>
        </nav>

        <section class="about">
            <h1>Contact Us</h1>

            <p>Have any questions? Feel free to contact us.</p>

            <p>Email: contact@example.com</p>

            <a class="btn" href="/">Back to Home</a>
        </section>

        <footer>
            <p>© 2026 My Flask Website. All Rights Reserved.</p>
        </footer>

    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True, port=5001)
