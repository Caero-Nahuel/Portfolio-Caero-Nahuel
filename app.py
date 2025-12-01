from flask import Flask, render_template
from data import portfolio_data

app = Flask(__name__)

@app.route('/')
def home():
    # Renderizamos el HTML pasando los datos como contexto
    return render_template('index.html', data=portfolio_data)

if __name__ == '__main__':
    app.run(debug=True)