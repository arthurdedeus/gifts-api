import factory
from factory import LazyAttribute
from faker import Faker

from factories import UserFactory
from gifts.models.checkout import Checkout
from gifts.models.checkout_item import CheckoutItem
from gifts.models.gift import Gift

faker = Faker()


class GiftFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Gift

    name = LazyAttribute(lambda _: faker.word())
    description = LazyAttribute(lambda _: faker.text())
    price = LazyAttribute(lambda _: faker.random_int(min=100, max=100000))
    amount = LazyAttribute(lambda _: faker.random_int(min=1, max=100))
    image = LazyAttribute(lambda _: faker.image_url())


class CheckoutFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Checkout

    user = factory.SubFactory(UserFactory)
    message = LazyAttribute(lambda _: faker.text())
    qr_code = LazyAttribute(lambda _: faker.image_url())


class CheckoutItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CheckoutItem

    checkout = factory.SubFactory(CheckoutFactory)
    gift = factory.SubFactory(GiftFactory)
    quantity = LazyAttribute(lambda obj: faker.random_int(min=1, max=obj.gift.amount))
    total = LazyAttribute(lambda obj: obj.gift.price * obj.quantity)
