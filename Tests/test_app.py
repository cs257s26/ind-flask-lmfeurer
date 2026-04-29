import json
from app import *
import unittest
import ProductionCode.command_line as command_line

class TestSOMETHING(unittest.TestCase):

    def setUp(self):
        """
        Sets up test client + loads dataset 
        """
        self.app = app.test_client()
        if "literacy" in command_line.datasets:
            command_line.datasets["literacy"].clear()
        load_data()

        
    def test_route(self):
        #sets up a special test app
        self.app = app.test_client() 
        #test app returns TestResponse object
        response = self.app.get('/', follow_redirects=True) 
        #TestResponse has webpage in .data
        self.assertEqual(b'hello, this is the homepage', response.data) 

    def test_growth_correct_input(self):
        """
        tests that when a valid country with sufficient data is entered, 
        the correct response is returned with the correct percentages and country
        """
        response = self.app.get('/growth/Mexico')
        self.assertIn(b'Mexico', response.data)
        self.assertIn(b"22.3", response.data)
        self.assertIn(b"95", response.data)
        self.assertIn(b"326.01%", response.data)

    def test_growth_incorrect_input(self):
        """
        tests that when an invalid country is entered (or a country with no data), 
        a response is returned indicating that there is no data for the country
        """
        response = self.app.get('/growth/bob')
        self.assertEqual(b'No literacy data for this country', response.data)
    
    def test_growth_incomplete_input(self):
        """
        tests that when a country with only one data point is entered, 
        a response is returned indicating that there is not enough data for the country
        """
        response = self.app.get('/growth/Japan')
        self.assertEqual(b'Not enough literacy data found for this country', response.data)

    def test_schooling_years_correct_input(self):
        """
        Tests that the correct data is outputted for a country
        """
        response = self.app.get('/schooling/France/2010/2015')
        data = json.loads(response.data)
        self.assertEqual(len(data), 2)

    def test_schooling_incorrect_input(self):
        """
        Tests that nothing is in the array for nonexistant countries
        """
        response = self.app.get('/schooling/Hi/2010/2015')
        data = json.loads(response.data)
        self.assertEqual(data, [])

    def test_schooling_incorrect_years(self):
        """
        Tests that the program returns empty list for years outside the dataset
        """
        response = self.app.get('/schooling/France/2030/2035')
        data = json.loads(response.data)
        self.assertEqual(data, [])