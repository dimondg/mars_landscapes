from flask import render_template
from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/carousel')
def sample_file_upload():
    return render_template('base.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
