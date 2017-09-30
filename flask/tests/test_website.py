
import unittest
from tests.base_website import BaseTestCase


class TestWebsite(BaseTestCase):

    def test_index_page_successful(self):
        with self.client:
            response = self.client.get('/')
            self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
