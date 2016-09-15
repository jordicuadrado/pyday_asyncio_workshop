from flask import Flask

from currency_sync.client import CurrencyClient

app = Flask(__name__)

@app.route("/convert/<currency>/<amount>")
def convert(currency, amount):
    client = CurrencyClient()
    amount_converted = client.convert(currency, int(amount))
    return "{} {}".format(currency, str(amount_converted))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, threaded=True)
