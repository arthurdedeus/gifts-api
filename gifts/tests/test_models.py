from django.test import TestCase

from gifts.factories import CheckoutFactory, CheckoutItemFactory, GiftFactory


class CheckoutTestCase(TestCase):
    def setUp(self):
        self.checkout = CheckoutFactory()

    def test_total(self):
        gift = GiftFactory(amount=5, price=100)
        CheckoutItemFactory(checkout=self.checkout, gift=gift, quantity=2)

        self.assertEqual(self.checkout.total, 200)
