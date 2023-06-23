"""
Sample unit test "testcase" for LBG API functionality
Tests key functions and API routes in isolation from client-side user interface

For full list of assertions available: https://docs.python.org/3.8/library/unittest.html
"""

import unittest
from lbg import item_builder
from flask_api import status
import requests

PORT = 8080
BASE_URL = f"http://localhost:{PORT}"

class MyLbgApiTestCase(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        requests.post(BASE_URL + '/create', json = {'name': 'Fruit', 'description': 'Orange', 'price': .18})
        requests.post(BASE_URL + '/create', json = {'name': 'Tool', 'description': 'Spade', 'price': 12.85})
        requests.post(BASE_URL + '/create', json = {'name': 'Drink', 'description': 'Lemonade', 'price': 1.99})
        requests.post(BASE_URL + '/create', json = {'name': 'Film', 'description': 'Casablanca', 'price': 19.99})

    def test_item_builder_data(self):
        """
        Test to see if item_builder returns the correctly keyed dictionary object
        based on raw data passed to it
        """
        expected = {'name': 'Tool', 'description': 'Hammer', 'price': 10.5, '_id': 99}
        self.assertEqual(item_builder("Tool", "Hammer", 10.50, 99), expected)

    #@unittest.skip("Skip this test for now using this decorator...")
    def test_item_builder_type(self):
        """
        Test to see if item_builder returns a dictionary object
        """
        self.assertIsInstance(item_builder("Tool", "Hammer", 10.50, 99), dict)

    def test_create_post_request_status(self):
        """
        Test to see if RESTful API returns a 201 (CREATED) status ok for a
        Create (Post) request.  Note.  API will need to be running(!)
        """
        response = requests.post(BASE_URL + '/create', json = {'name': 'Tool', 'description': 'Hammer', 'price': 10.5})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    #@unittest.skip("Skip this test for now using this decorator...")
    def test_create_post_request_type(self):
        """
        Test to see if RESTful API returns an objectfor a simple
        Create (Post) request.  Note.  API will need to be running(!)
        """
        response = requests.post(BASE_URL + '/create', json = {'name': 'Vegetable', 'description': 'Leek', 'price': .7})
        self.assertIsInstance(response, object)

    def test_read_all_get_request_status(self):
        """
        Test to see if RESTful API returns a 200 (OK) status ok for a simple
        Read all (Get) request.  Note.  API will need to be running(!)
        """
        response = requests.get(BASE_URL + '/read')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #@unittest.skip("Skip this test for now using this decorator...")
    def test_read_all_get_request_type(self):
        """
        Test to see if RESTful API returns a list for a simple
        Read all (Get) request.  Note.  API will need to be running(!)
        """
        response = requests.get(BASE_URL + '/read').json()
        print(response)
        self.assertIsInstance(response, list)

    def test_read_one_get_request_status(self):
        """
        Test to see if RESTful API returns a 200 (OK) status ok for a simple
        Read one (Get) request.  Note.  API will need to be running(!)
        """
        response = requests.get(BASE_URL + '/read')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    #@unittest.skip("Skip this test for now using this decorator...")
    def test_read_one_get_request_type(self):
        """
        Test to see if RESTful API returns an object for a simple
        Read one (Get) request.  Note.  API will need to be running(!)
        """
        response = requests.get(BASE_URL + '/read/1').json()
        print(response)
        self.assertIsInstance(response, object)

    def test_update_put_request_status(self):
        """
        Test to see if RESTful API returns a 200 (OK) status ok for an
        Update (Put) request.  Note.  API will need to be running(!)
        """
        response = requests.put(BASE_URL + '/update/1', json = {'name': 'Tool', 'description': 'Spade', 'price': 14.82, '_id': 2})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #@unittest.skip("Skip this test for now using this decorator...")
    def test_update_put_request_type(self):
        """
        Test to see if RESTful API returns an object for an
        Update (Put) request.  Note.  API will need to be running(!)
        """
        response = requests.put(BASE_URL + '/update/2', json = {'name': 'Fruit', 'description': 'Apple', 'price': .18, '_id': 1})
        self.assertIsInstance(response, object)

    def test_delete_delete_request_status(self):
        """
        Test to see if RESTful API returns a 200 (OK) status ok for a
        Delete (Deletet) request.  Note.  API will need to be running(!)
        """
        response = requests.delete(BASE_URL + '/delete/3')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #@unittest.skip("Skip this test for now using this decorator...")
    def test_delete_delete_request_type(self):
        """
        Test to see if RESTful API returns an object for a
        Delete (Delete) request.  Note.  API will need to be running(!)
        """
        response = requests.delete(BASE_URL + '/delete/4')
        self.assertIsInstance(response, object)
    
    @classmethod
    def tearDownClass(cls):
        requests.delete(BASE_URL + '/delete/1')
        requests.delete(BASE_URL + '/delete/2')
        requests.delete(BASE_URL + '/delete/3')
        requests.delete(BASE_URL + '/delete/4')
        requests.delete(BASE_URL + '/delete/5')
        requests.delete(BASE_URL + '/delete/6')

# module import protection
if __name__ == '__main__':
    unittest.main(verbosity=2)
