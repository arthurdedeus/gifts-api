import factory
from factory import LazyAttribute
from faker import Faker

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
