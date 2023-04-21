import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """

    """ ------------ Add more unit tests ------------ """


class TestGetDataPoint(unittest.TestCase):

    def test_get_data_point(self):
        quote = {
            'stock': 'TEST',
            'top_bid': {'price': 120.00, 'size': 10},
            'top_ask': {'price': 125.00, 'size': 20}
        }
        stock, bid_price, ask_price, price = getDataPoint(quote)
        self.assertEqual(stock, 'TEST')
        self.assertEqual(bid_price, 120.00)
        self.assertEqual(ask_price, 125.00)
        self.assertEqual(price, 122.50)


class TestGetRatio(unittest.TestCase):

    def test_get_ratio_divide_by_zero(self):
        price_a = 100
        price_b = 0
        self.assertIsNone(getRatio(price_a, price_b))

    def test_get_ratio_valid_prices(self):
        price_a = 250.00
        price_b = 125.00
        expected_ratio = 2.0
        self.assertEqual(getRatio(price_a, price_b), expected_ratio)

    def test_get_ratio_zero_prices(self):
        price_a = 0
        price_b = 0
        self.assertIsNone(getRatio(price_a, price_b))


if __name__ == '__main__':
    unittest.main()
