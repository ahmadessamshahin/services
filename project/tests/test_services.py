import json
import unittest

from project.tests.base import  BaseTestCase

class TestServices(BaseTestCase):
  """ Tests for the Three end points """
  def test_factorial(self):
    response =self.client.get('/users/ping')
    data = json.loads(response.data.decode())
    self.assertEqual(response.status_code, 200)
    self.assertIn('pong!', data['message'])
    self.assertIn('success', data['status'])

if __name__ == '__main__':
  unittest.main()