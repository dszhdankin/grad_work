from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

import subprocess

import json

app = Flask(__name__)


def translate_to_sql(inpt):
    inpt = inpt.replace('\n', '')

    process = subprocess.Popen(['python', 'eng2sql_translator.py', f'{inpt}'],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout.decode('utf-8')


@app.route("/")
def main_page():
    return render_template('main_page.html')


@app.route("/get_translation/", methods=['POST'])
def translate():
    res = ""

    str_data = request.data.decode("utf-8")
    dict_data = json.loads(str_data)
    inpt = dict_data['dt']

    if not isinstance(inpt, str):
        return "Unexpected data!", 400

    res = translate_to_sql(inpt)

    response = jsonify({'dt': res})
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == '__main__':
    app.run(port=5000)
