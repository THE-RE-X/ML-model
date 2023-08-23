from flask import Flask, render_template, request
import engine

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        height = request.form['height']
        print(height)
        weight = engine.prediction([[float(height)]])
        return render_template('index.HTML',hei=height, wei=weight)


    return render_template('index.HTML')


if __name__ == "__main__":
    app.run(port=3000)
