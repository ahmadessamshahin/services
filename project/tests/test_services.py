import json
import unittest

from project.tests.base import  BaseTestCase

class TestServices(BaseTestCase):
  """ Tests for the Three end points """
  def test_valid_factorial(self):
    response =self.client.get('/factorial',json={
        'number': 4
    })
    data = json.loads(response.data.decode())
    self.assertEqual(response.status_code, 200)
    self.assertIn('24', data['message'])
    self.assertIn('success', data['status'])
  
  def test_invalid_factorial(self):
    response =self.client.get('/factorial',json={
        'number': -4
    })
    data = json.loads(response.data.decode())
    self.assertEqual(response.status_code, 400)
    self.assertIn("Parameter 'number' must be larger than 0.", data['message'])
    self.assertIn('fail', data['status'])

  def test_missing_number_factorial(self):
    response =self.client.get('/factorial')
    data = json.loads(response.data.decode())
    self.assertEqual(response.status_code, 400)
    self.assertIn("Required json parameter 'number' not given.", data['message'])
    self.assertIn('fail', data['status'])

  def test_valid_fibonacci(self):
    response =self.client.get('/fibonacci',json={
        'number': 4
    })
    data = json.loads(response.data.decode())
    self.assertEqual(response.status_code, 200)
    self.assertIn('3', data['message'])
    self.assertIn('success', data['status'])
  
  def test_invalid_fibonacci(self):
    response =self.client.get('/fibonacci',json={
        'number': -4
    })
    data = json.loads(response.data.decode())
    self.assertEqual(response.status_code, 400)
    self.assertIn("Parameter 'number' must be larger than 0.", data['message'])
    self.assertIn('fail', data['status'])

  def test_missing_number_fibonacci(self):
    response =self.client.get('/fibonacci')
    data = json.loads(response.data.decode())
    self.assertEqual(response.status_code, 400)
    self.assertIn("Required json parameter 'number' not given.", data['message'])
    self.assertIn('fail', data['status'])

  def test_valid_ackermann(self):
    response =self.client.get('/ackermann',json={
        'row': 4,
        'column': 4
    })
    data = json.loads(response.data.decode())
    self.assertEqual(response.status_code, 200)
    self.assertIn('5573', data['message'])
    self.assertIn('success', data['status'])
  
  def test_invalid_ackermann(self):
    response =self.client.get('/ackermann',json={
        'row': -4,
        'column': 4
      })
    data = json.loads(response.data.decode())
    self.assertEqual(response.status_code, 400)
    self.assertIn("Parameter 'row' must be larger than 0.", data['message'])
    self.assertIn('fail', data['status'])

  def test_missing_number_ackermann(self):
    response =self.client.get('/ackermann')
    data = json.loads(response.data.decode())
    self.assertEqual(response.status_code, 400)
    self.assertIn("Required json parameter 'row' not given.", data['message'])
    self.assertIn('fail', data['status'])

if __name__ == '__main__':
  unittest.main()