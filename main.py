from pytesseract import image_to_string
from PIL import Image
import flask
import os, json, random

app = flask.Flask(__name__)

def extract_text(filename) -> str:
    img_path = './documents'
    img = Image.open(os.path.join(img_path, filename))
    txt =  image_to_string(img, config='-l rus --oem 1 --psm 1')
    return txt

@app.route('/getResponse', methods=['GET'])
def return_text():
    jsreq = flask.request.get_json(silent=True, force=True)
    if flask.request.method=='POST':
        if 'filename' in jsreq:
            resp = extract_text(jsreq['filename'])
            return flask.Response(response=json.dumps({'text':resp}),
                                  content_type='application/json; charset=utf-8')

    filenames = os.listdir('./documents')
    filename = filenames[random.randint(0, len(filenames)-1)]
    resp = extract_text(filename)
    return flask.Response(response=json.dumps({'text':resp}),
                          content_type='application/json; charset=utf-8')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)