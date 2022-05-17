from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('bootstrap_table.html', title='Bootstrap Table')


if __name__ == '__main__':
    app.run()
