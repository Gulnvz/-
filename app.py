from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Красивая Страница</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(45deg, #f06, #a2c2e1);
                color: white;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                text-align: center;
            }

            h1 {
                font-size: 3rem;
                font-weight: bold;
                margin-bottom: 20px;
            }

            p {
                font-size: 1.5rem;
                line-height: 1.8;
            }

            .container {
                background-color: rgba(0, 0, 0, 0.6);
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
            }

            .highlight {
                color: #FFD700;
            }

            footer {
                position: absolute;
                bottom: 20px;
                left: 50%;
                transform: translateX(-50%);
                font-size: 1rem;
                color: #bbb;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Добро пожаловать!</h1>
            <p>Серик Гульназ Амантаева Каракат</p>
            <p class="highlight">Женіс Орынбек Иб-22</p>
        </div>
        <footer>
            <p>Флешка Flask - Простой проект</p>
        </footer>
    </body>
    </html>
    """
    return render_template_string(html_content)

if name == "__main__":
    app.run(host="0.0.0.0", port=10000)
