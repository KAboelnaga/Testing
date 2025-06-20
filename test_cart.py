import unittest
import cart

class TestCart(unittest.TestCase):
    def setUp(self):
        self.cart = cart.Cart()

    def test_add_item(self):
        self.cart.add_item(cart.Product('X', 1000))
        self.assertEqual(self.cart.total, 1000)
        self.assertEqual(self.cart.items[0].quantity, 1)
        self.cart.add_item(cart.Product('X', 1000))
        self.assertEqual(self.cart.items[0].quantity, 2)
        self.assertEqual(self.cart.total, 2000)
        self.cart.add_item(cart.Product('Y', 2000))
        self.assertEqual(self.cart.total, 4000)
    
    def test_remove_item(self):
        self.cart.add_item(cart.Product('X', 1000))
        self.cart.add_item(cart.Product('X', 1000))
        self.cart.add_item(cart.Product('Y', 2000))
        self.cart.remove_item(cart.Product('X', 1000))
        self.assertEqual(self.cart.total, 3000)
        self.cart.remove_item(cart.Product('X', 1000))
        self.assertEqual(self.cart.total, 2000)

if __name__ == '__main__':
    unittest.main()