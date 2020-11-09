import datetime

from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/<name>/<classroom>')
def display_name_class(name,classroom):
    return "Hello, {0} from the class {1}".format(str(name),str(classroom))


if __name__ == '__main__':    
    app.run(host='127.0.0.1', port=8080, debug=True)