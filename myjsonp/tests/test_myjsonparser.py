import unittest
import logging

from unittest.mock import patch


from myjsonp.main import json_parser



class TestMyJSONParser(unittest.TestCase):
    
    def test_json_parser_valid_json_step1(self):
        # Validating an empty JSON...
        test_file_path = 'tests/step1/valid.json'
        result = json_parser(test_file_path)
        self.assertEqual(result, 0)
        
    
    def test_json_parser_valid_json_step2(self):
        # Validating a simple JSON object containing string keys and string values...
        test_file_path = 'tests/step2/valid.json'
        result = json_parser(test_file_path)
        self.assertEqual(result, 0)
    
    
    def test_json_parser_valid_json_step2_2(self):
        # Validating a simple JSON object containing string keys and string values...
        test_file_path = 'tests/step2/valid2.json'
        result = json_parser(test_file_path)
        self.assertEqual(result, 0)
    
        
    def test_json_parser_valid_json_step3(self):
        # Validating a simple JSON object containing string, numeric, boolean and null values...
        test_file_path = 'tests/step3/valid.json'
        result = json_parser(test_file_path)
        self.assertEqual(result, 0)
     
        
    def test_json_parser_valid_json_step4(self):
        # Validating a simple JSON object with object and array values...
        test_file_path = 'tests/step4/valid.json'
        result = json_parser(test_file_path)
        self.assertEqual(result, 0)
    
    
    def test_json_parser_valid_json_step4_2(self):
        # Validating a simple JSON object with object and array values...
        test_file_path = 'tests/step4/valid2.json'
        result = json_parser(test_file_path)
        self.assertEqual(result, 0)
        
        
    def test_json_parser_invalid_json_step1(self):
        # Validating an empty JSON...
        test_file_path = 'tests/step1/invalid.json'
        result = json_parser(test_file_path)
        self.assertEqual(result, 1)
    
    
    def test_json_parser_invalid_json_step2(self):
        # Validating a simple JSON object containing string keys and string values...
        test_file_path = 'tests/step2/invalid.json'
        result = json_parser(test_file_path)
        self.assertEqual(result, 1)
    
        
    def test_json_parser_invalid_json_step2_2(self):
        # Validating a simple JSON object containing string keys and string values...
        test_file_path = 'tests/step2/invalid2.json'
        result = json_parser(test_file_path)
        self.assertEqual(result, 1)
    
    
    def test_json_parser_invalid_json_step3(self):
        # Validating an invalid simple JSON object containing string, numeric, boolean and null values...
        test_file_path = 'tests/step3/invalid.json'
        result = json_parser(test_file_path)
        self.assertEqual(result, 1)
        
    
    def test_json_parser_invalid_json_step4(self):
        # Validating an invalid simple JSON object with object and array values...
        test_file_path = 'tests/step4/invalid.json'
        result = json_parser(test_file_path)
        self.assertEqual(result, 1)
    


if __name__ == '__main__':
    unittest.main()