import aiohttp


class CurrencyClient:

    ENDPOINT = "http://api.fixer.io/latest"


    async def convert(self, currency, amount):
        """
        Convert a certain `amount` o monet from EUR to a specified `currency`.
        It will use the service behind the `CurrencyClient.ENDPOINT` to get
        the current exchange and do the proper maths.
        """
        raise NotImplemented


if __name__ == "__main__":
    import argparse
    import asyncio
    parser = argparse.ArgumentParser()
    parser.add_argument("currency", help="Currency to convert")
    parser.add_argument("amount", help="Amount of money", type=int)
    args = parser.parse_args()

    async def call_and_print():
        result = await CurrencyClient().convert(args.currency, args.amount)
        print(result)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(call_and_print())
