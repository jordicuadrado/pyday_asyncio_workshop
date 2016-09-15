import requests

class CurrencyClient:

    ENDPOINT = "http://api.fixer.io/latest"


    def convert(self, currency, amount):
        """
        Convert a certain `amount` o monet from EUR to a specified `currency`.
        It will use the service behind the `CurrencyClient.ENDPOINT` to get
        the current exchange and do the proper maths.
        """
        response = requests.get(self.ENDPOINT)
        data = response.json()

        assert 'rates' in data

        try:
            exchange = data['rates'][currency]
        except KeyError:
            print("Currency `{}` not found".format(currency))
            raise

        return amount * exchange


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("currency", help="Currency to convert")
    parser.add_argument("amount", help="Amount of money", type=int)
    args = parser.parse_args()

    result = CurrencyClient().convert(args.currency, args.amount)
    print(result)
