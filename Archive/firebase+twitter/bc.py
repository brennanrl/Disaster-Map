from flask import Flask
from xecd_rates_client import XecdClient
xe = XecdClient('xe891090202', '8ht3qjhq8vnu0dbb91ai40p44b')

app = Flask(__name__)

@app.route('/convert/<f>/<t>')
def convert(f, t):
    print(f)
    return str(xe.convert_from(f, t, 100)["to"][0]["mid"])

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=3389)
