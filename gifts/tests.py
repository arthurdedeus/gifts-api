from django.test.testcases import TestCase
from django.urls import reverse
from rest_framework import status

from factories import UserFactory
from gifts.factories import GiftFactory

LIST_VIEW = "gifts:gifts-list"
DETAIL_VIEW = "gifts:gifts-detail"
NEW_NAME = "New name"


class GiftViewSetTestCase(TestCase):
    def setUp(self):
        self.gift = GiftFactory()
        self.user = UserFactory()

    def test_list(self):
        response = self.client.get(reverse(LIST_VIEW))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["count"], 1)
        result = response.json()["results"][0]
        self.assertEqual(result["id"], self.gift.id)
        self.assertEqual(result["name"], self.gift.name)
        self.assertEqual(result["description"], self.gift.description)
        self.assertTrue(result["price"], self.gift.price)
        self.assertEqual(result["amount"], self.gift.amount)
        self.assertTrue(result["image"].endswith(self.gift.image.url))

    def test_retrieve(self):
        response = self.client.get(reverse(DETAIL_VIEW, kwargs={"pk": self.gift.id}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        result = response.json()
        self.assertEqual(result["id"], self.gift.id)
        self.assertEqual(result["name"], self.gift.name)
        self.assertEqual(result["description"], self.gift.description)
        self.assertTrue(result["price"], self.gift.price)
        self.assertEqual(result["amount"], self.gift.amount)
        self.assertTrue(result["image"].endswith(self.gift.image.url))

    def test_patch_authenticated_user_should_return_200(self):
        self.client.force_login(self.user)
        response = self.client.patch(
            reverse(DETAIL_VIEW, kwargs={"pk": self.gift.id}),
            data={"name": NEW_NAME},
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.gift.refresh_from_db()
        self.assertEqual(self.gift.name, NEW_NAME)

    def test_patch_unauthenticated_user_should_return_403(self):
        response = self.client.patch(
            reverse("gifts:gifts-detail", kwargs={"pk": self.gift.id}),
            data={"name": NEW_NAME},
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
