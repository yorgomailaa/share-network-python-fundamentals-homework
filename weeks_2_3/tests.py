import unittest
import surfshop
from parameterized import parameterized


class ShoppingCartTests(unittest.TestCase):

    def setUp(self):
        self.cart = surfshop.ShoppingCart()

    def test_add_one_surfboard(self):
        result = self.cart.add_surfboards(1)
        self.assertEqual(result, "Successfully added 1 surfboard to cart!")

    @parameterized.expand([
        (2, "Successfully added 2 surfboards to cart!"),
        (3, "Successfully added 3 surfboards to cart!"),
        (4, "Successfully added 4 surfboards to cart!")
    ])
    def test_add_multiple_surfboards(self, quantity, expected):
        result = self.cart.add_surfboards(quantity)
        self.assertEqual(result, expected)

    @unittest.skip("Skipping max board test")
    def test_add_too_many_surfboards(self):
        with self.assertRaises(surfshop.TooManyBoardsError):
            self.cart.add_surfboards(5)

    def test_apply_locals_discount(self):
        self.cart.apply_locals_discount()
        self.assertTrue(self.cart.locals_discount)


if _name_ == "_main_":
    unittest.main()
