# py -m unittest test.py -v
# python3 -m unittest test.py -v
from main import *
import unittest 

class TestJson(unittest.TestCase):
	def test_json(self):
		input = '{"a": 1,"b": true,"c": {"d": 3, "e": "test"} }'
		output = '{"a": 1, "b": true, "c.d": 3, "c.e": "test"}'
		self.assertEqual(removeWhitespaces(convert(input)), removeWhitespaces(output))
	def test_empty(self):		
		input = '{}'
		output = '{}'
		self.assertEqual(removeWhitespaces(convert(input)), removeWhitespaces(output))
	def test_nested(self):
		input = '{"a": {"b": {"c": {"d": {"e": {"f": "some text" } } } } } }'
		output = '{"a.b.c.d.e.f": "some text"}'
		self.assertEqual(removeWhitespaces(convert(input)), removeWhitespaces(output))
	def test_inlcudes_array(self):
		input = '{"a": [{"a":"b"},{"a":"b"},{"a":"b"}]}'
		output = '{"a": [{"a": "b"}, {"a": "b"}, {"a": "b"}]}'
		self.assertEqual(removeWhitespaces(convert(input)), removeWhitespaces(output))
	def test_mixture(self):
		input = '{"a": [], "b": {"c": 1, "d": {"e": 399837,\
				"f": ["one", "two", "three"], \
				"g": [["weather", "copenhagen", 30, "d"], \
				["sun", "shinning"]]}},"c": "working"}'
		output = '{"a": [], "b.c": 1, "b.d.e": 399837, \
				"b.d.f": ["one", "two", "three"], \
				"b.d.g": [["weather", "copenhagen", 30, "d"], \
				["sun", "shinning"]], "c": "working"}'
		self.assertEqual(removeWhitespaces(convert(input)), removeWhitespaces(output))
	def test_empty_02(self):
		input = '{"a": {},"c": "working"}'
		output = '{"a": {}, "c": "working"}'
		self.assertEqual(removeWhitespaces(convert(input)), removeWhitespaces(output))
	def test_empty_03(self):
		input = '{"a": {"b": {}},"c": "working"}'
		output = '{"a.b": {}, "c": "working"}'
		self.assertEqual(removeWhitespaces(convert(input)), removeWhitespaces(output))
	def test_random_generated01(self):
		self.maxDiff = None
		input = '{"random":"91","randomfloat":"18.186",\
				"bool":"true","date":"1983-03-03",\
				"regEx":"hellooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooworld",\
				"enum":"generator","firstname":"Ashlee","lastname":"Krystle","city":"Jacksonville",\
				"country":"Somalia","countryCode":"FK","emailusescurrentdata":"Ashlee.Krystle@gmail.com",\
				"emailfromexpression":"Ashlee.Krystle@yopmail.com","array":["Tori","Felice","Lucy","Cecile","Stevana"],\
				"arrayofobjects":[{"index":"0","indexstartat5":"5"},{"index":"1","indexstartat5":"6"},{"index":"2","indexstartat5":"7"}],\
				"Mahalia":{"age":"30"}}'
		output= '{"random": "91", "randomfloat": "18.186", "bool": "true", "date": "1983-03-03", \
				"regEx": "hellooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooworld", \
				"enum": "generator", "firstname": "Ashlee", "lastname": "Krystle", "city": "Jacksonville", \
				"country": "Somalia", "countryCode": "FK", "emailusescurrentdata": "Ashlee.Krystle@gmail.com", \
				"emailfromexpression": "Ashlee.Krystle@yopmail.com", "array": ["Tori", "Felice", "Lucy", "Cecile", "Stevana"], \
				"arrayofobjects": [{"index": "0", "indexstartat5": "5"}, {"index": "1", "indexstartat5": "6"}, \
				{"index": "2", "indexstartat5": "7"}], "Mahalia.age": "30"}'
		self.assertEqual(removeWhitespaces(convert(input)), removeWhitespaces(output))
	def test_random_generated02(self):
		input = '{"voyage":{"produce":"cave","audience":"rule",\
				"political":"carefully","distant":"driven",\
				"spent":true,"while":"habit"}}'
		output = '{"voyage.produce": "cave", \
				   "voyage.audience": "rule", \
				   "voyage.political": "carefully", \
				   "voyage.distant": "driven", \
				   "voyage.spent": true, \
				   "voyage.while": "habit"}'
		self.assertEqual(removeWhitespaces(convert(input)), removeWhitespaces(output))
	def test_random_generated03(self):
		input = '{"task":{"six":-1264053535,"monkey":"what",\
				"temperature":true,"ice":"toy",\
				"production":834140178.8341303},\
				"some":-24662101,"left":true,\
				"when":false,"screen":"men",\
				"calm":false}'
		output = '{	"task.six": -1264053535, \
					"task.monkey": "what",\
					"task.temperature": true,\
					"task.ice": "toy", \
					"task.production": 834140178.8341303, \
					"some": -24662101,"left": true,\
					"when": false, "screen": "men",\
					"calm": false \
				  }'
		self.assertEqual(removeWhitespaces(convert(input)), removeWhitespaces(output))