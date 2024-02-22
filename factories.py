import factory.django
from django.contrib.auth.models import User
from factory import LazyAttribute
from faker import Faker

faker = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = LazyAttribute(lambda _: faker.user_name())
    email = LazyAttribute(lambda _: faker.email())
    first_name = LazyAttribute(lambda _: faker.first_name())
    last_name = LazyAttribute(lambda _: faker.last_name())
    password = LazyAttribute(lambda _: faker.password())
