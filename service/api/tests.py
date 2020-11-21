from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase


class RatingsTests(APITestCase):

    def test_get_ratings(self):
        url = reverse('rating')
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(len(response.data), 2)


    def test_get_ratings_by_user(self):
        url = reverse('rating')
        response = self.client.post(
            url, {"user1": 5}, format='json')
        response = self.client.get(url+"user1/")
        self.assertEqual(response.data.get("value"), 5)
        self.assertEqual(200, response.status_code)

    def test_post_ratings(self):
        url = reverse('rating')
        response = self.client.post(
            url, {"userXYZ": 4}, format='json')
        self.assertEqual(201, response.status_code)

    def test_put_rating(self):
        url = reverse('rating')
        response = self.client.post(
            url, {"user1": 5}, format='json')
        self.assertEqual(201, response.status_code)

        response = self.client.put(
            url, {"user1": 3}, format='json')

        response = self.client.get(url+"user1/")
        self.assertEqual(response.data.get("value"), 3)
        self.assertEqual(200, response.status_code)
